import urllib, http.client
import time
import json
# These modules are needed to generate an API signature.
import hmac, hashlib

# API keys provided by exmo
API_KEY = ''
# notice that a 'b' is added before the line
API_SECRET = b''

# Fine tuning
CURRENCY_1 = 'XRP' 
CURRENCY_2 = 'USD'

CURRENCY_1_MIN_QUANTITY = 0.001 # minimum bid amount - taken from https://api.exmo.com/v1/pair_settings/

ORDER_LIFE_TIME = 4 # after how many minutes to cancel the unfulfilled order to buy CURRENCY_1
STOCK_FEE = 0.002 # Commission, which the exchange takes (0.002 = 0.2%)
AVG_PRICE_PERIOD = 5 # What period to take the average price (min)
AVG_PRICE_LAST=0 # previous average price
CAN_SPEND = 0.5 # How much to spend CURRENCY_2 every time you buy CURRENCY_1
PROFIT_MARKUP = 0.006 # What profit is needed from each transaction? (0.001 = 0.1%)
DEBUG = True # True — show debug information, False — write as little as possible.

STOCK_TIME_OFFSET = 0 # If the time of the exchange diverges from the current

# basic settings
API_URL = 'api.exmo.me'
API_VERSION = 'v1'

# Own exception class
class ScriptError(Exception):
    pass
class ScriptQuitCondition(Exception):
    pass

CURRENT_PAIR = CURRENCY_1 + '_' + CURRENCY_2

# All API calls pass through this function.
def call_api(api_method, http_method="POST", **kwargs):
    # We make a dictionary {key: value} for sending to the exchange
    # so far in it {'nonce': 123172368123}
    payload = {'nonce': int(round(time.time()*1000))}

    # If the parameters are passed to the function in the key: value format
    if kwargs:
        # add each parameter to the payload dictionary
        # It turns out {'nonce': 123172368123, 'param1': 'val1', 'param2': 'val2'}
        payload.update(kwargs)

    # Переводим словарь payload в строку, в формат для отправки через GET/POST и т.п.
    payload =  urllib.parse.urlencode(payload)

    #From the payload line we get "signature", we hash using API secret key
    # sing - the received key that will be sent to the exchange for verification
    H = hmac.new(key=API_SECRET, digestmod=hashlib.sha512)
    H.update(payload.encode('utf-8'))
    sign = H.hexdigest()

    # We form request headers to send a request to the exchange.
    # The public API key and the signature obtained by hmac are transmitted.
    headers = {"Content-type": "application/x-www-form-urlencoded",
           "Key":API_KEY,
           "Sign":sign}

    # We create a connection to the exchange, if during 60 seconds we could not connect, the connection was broken
    conn = http.client.HTTPSConnection(API_URL, timeout=60)
    # After establishing the connection, we request the transmitted address
    # In the header of the request, headers leave, in the body - payload
    conn.request(http_method, "/"+API_VERSION + "/" + api_method, payload, headers)
    # We receive the answer from the exchange and read it into the response variable
    response = conn.getresponse().read()
    # Close the connection
    conn.close()

    try:
        # The resulting answer is translated into a UTF string, and we try to convert from text to a Python object.
        obj = json.loads(response.decode('utf-8'))

        # See if the received object has the "error" key.
        if 'error' in obj and obj['error']:
            # If there is an error, the code will not continue
            raise ScriptError(obj['error'])
        # Return the resulting object as a result of the function f-tion
        return obj
    except ValueError:
        # If failed to translate the response received (not returned JSON)
        raise ScriptError('Помилка аналізу повертаються даних, отримана рядок', response)

# Algorithm implementation
def main_flow():

    try:
        # Get a list of active orders
        try:
            opened_orders = call_api('user_open_orders')[CURRENCY_1 + '_' + CURRENCY_2]
        except KeyError:
            if DEBUG:
                print('Відкритих ордерів немає')
            opened_orders = []

        sell_orders = []
        # Are there any outstanding orders to sell CURRENCY_1?
        for order in opened_orders:
            if order['type'] == 'sell':
                # There are outstanding orders to sell CURRENCY_1, exit
                raise ScriptQuitCondition('Вихід, чекаємо аж до дня виповнення / закриються всі ордера на продаж (один ордер може бути розбитий біржею на кілька і виконуватися частинами)')
            else:
                # Remembering purchase orders CURRENCY_1
                sell_orders.append(order)

        # Check whether there are open orders to buy CURRENCY_1
        if sell_orders: # open orders there
            for order in sell_orders:
                # We check whether there are partially executed
                if DEBUG:
                    print('Перевіряємо, що відбувається з відкладеним ордером', order['order_id'])
                try:
                    order_history = call_api('order_trades', order_id=order['order_id'])
                    # the order is already a partial execution, exit
                    raise ScriptQuitCondition('Вихід, продовжуємо сподіватися докупити валюту за тим курсом, за яким вже купили частину')
                except ScriptError as e:
                    if 'Error 50304' in str(e):
                        if DEBUG:
                            print('Частково виконаних ордерів немає')

                        time_passed = time.time() + STOCK_TIME_OFFSET*60*60 - int(order['created'])

                        if time_passed > ORDER_LIFE_TIME * 60:
                            # The order has been hanging for a long time, nobody needs it, we cancel
                            call_api('order_cancel', order_id=order['order_id'])
                            raise ScriptQuitCondition('Скасовуємо ордер -за ' + str(ORDER_LIFE_TIME) + ' хвилин не вдалося купити '+ str(CURRENCY_1))
                        else:
                            raise ScriptQuitCondition('Вихід, продовжуємо сподіватися купити валюту за вказаною раніше курсу, з часу створення ордера пройшло% s секунд' % str(time_passed))
                    else:
                        raise ScriptQuitCondition(str(e))

        else: # No open orders
            balances = call_api('user_info')['balances']
            if float(balances[CURRENCY_1]) >= CURRENCY_1_MIN_QUANTITY: # Is there a CURRENCY_1 available for sale?
                """
                   Calculate the course for sale.
                    We need to sell all the currency we bought, for the amount for which we bought + a bit of gain and minus commission of the exchange
                    At the same time, it’s important that the currency is less than what we bought - the commission went to the exchange
                    0.00134345 1.5045
                """
                wanna_get = CAN_SPEND + CAN_SPEND * (STOCK_FEE+PROFIT_MARKUP)  # How many want to get for our quantity

                print('sell', balances[CURRENCY_1], wanna_get, (wanna_get/float(balances[CURRENCY_1])))

                #if (avg_price > wanna_get and avg_price < AVG_PRICE_LAST):
###############
                deals = call_api('trades', pair=CURRENT_PAIR)
                prices = []
                i=0
                #визначаємо середнє значення для 5 останніх операцій
                for deal in deals[CURRENT_PAIR]:
                    time_passed = time.time() + STOCK_TIME_OFFSET*60*60 - int(deal['date'])
                    i+=1
                    if i<5:
#                    if time_passed < AVG_PRICE_PERIOD:
                        prices.append(float(deal['price']))
                try:
                    avg_price = sum(prices)/len(prices)

                    # buy more because the stock exchange will then pick up a piece
                    my_need_price = avg_price + avg_price * (STOCK_FEE+STOCK_FEE/2)
                    my_amount = CAN_SPEND/my_need_price

                    print('buy', my_amount, my_need_price)

                    # визначаємо умови для продажу
                    global AVG_PRICE_LAST
                    if (avg_price > wanna_get and avg_price < AVG_PRICE_LAST):
                        new_order = call_api(
                            'order_create',
                            pair=CURRENT_PAIR,
                            quantity = my_amount,
                            price=my_need_price,
                            type='sell'
                        )
                        print(new_order)
                        if DEBUG:
                            print('Створено ордер на покупку', new_order['order_id'])

                    else: # we can buy too little for our amount
                        raise ScriptQuitCondition('Вихід, не вистачає грошей на створення ордера1')
                    AVG_PRICE_LAST=avg_price
                except ZeroDivisionError:
                    print('Неможливо обчислити середню ціну', prices)
######################
                """
                new_order = call_api(
                    'order_create',
                    pair=CURRENT_PAIR,
                    quantity = balances[CURRENCY_1],
                    price=wanna_get/float(balances[CURRENCY_1]),
                    type='sell'
                )
                print(new_order)
                if DEBUG:
                    print('Создан ордер на продажу', CURRENCY_1, new_order['order_id'])
                """
            else:
                # CURRENCY_1 no, you need to buy
                # Is there enough money in the balance in the currency CURRENCY_2 (Balance> = CAN_SPEND)
                if float(balances[CURRENCY_2]) >= CAN_SPEND:
                    # Find out the average price for AVG_PRICE_PERIOD for which CURRENCY_1 is sold.

                    deals = call_api('trades', pair=CURRENT_PAIR)
                    prices = []
                    for deal in deals[CURRENT_PAIR]:
                        time_passed = time.time() + STOCK_TIME_OFFSET*60*60 - int(deal['date'])
                        if time_passed < AVG_PRICE_PERIOD*60:
                            prices.append(float(deal['price']))
                    try:
                        avg_price = sum(prices)/len(prices)
                        """
                           Calculate how much currency CURRENCY_1 can buy.
                            For the amount of CAN_SPEND minus STOCK_FEE, and taking into account PROFIT_MARKUP
                            (= lower than the average market price, taking into account the commission and the desired profit)
                       """
                        # buy more because the stock exchange will then pick up a piece
                        my_need_price = avg_price - avg_price * (STOCK_FEE+STOCK_FEE/2)
                        my_amount = CAN_SPEND/my_need_price

                        print('buy', my_amount, my_need_price)

                        # Is it allowed to buy such a quantity of currency (i.e., the minimum transaction amount is not violated)
                        if my_amount >= CURRENCY_1_MIN_QUANTITY:
                            new_order = call_api(
                                'order_create',
                                pair=CURRENT_PAIR,
                                quantity = my_amount,
                                price=my_need_price,
                                type='buy'
                            )
                            print(new_order)
                            if DEBUG:
                                print('Створено ордер на купівлю', new_order['order_id'])

                        else: # we can buy too little for our amount
                            raise ScriptQuitCondition('Вихід, не вистачає грошей на створення ордера !!')
                    except ZeroDivisionError:
                        print('Неможливо обчислити середню ціну', prices)
                else:
                    raise ScriptQuitCondition('Вихід, не вистачає грошей')

    except ScriptError as e:
        print(e)
    except ScriptQuitCondition as e:
        if DEBUG:
            print(e)
        pass
    except Exception as e:
        print("!!!!",e)

while(True):
    main_flow()
    time.sleep(5)
