
import requests
import json
import os
from datetime import datetime
import time
import random

dateend = int(time.time())
#datestart = dateend - 60*60*24
user_date_end=int(input("введіть кількість денів від сьогодні. З коли починаємо отримувати данні ="))
user_date_start=int(input("скільки днів аналізуємо(кількість днів) ="))
datestart = dateend - 60*60*24*user_date_end
dateend=datestart+60*60*24*user_date_start
#
#datestart = int(dateend - 60*60*24*user_date_start)

sum_price=0

#комісія
fee=0.002

##def f_time_start(user_date_end=1, time_long=1):
##    """Визначаємо интервал початку часу отримання торгових данних і до коли """
##    time_now=int(time.time())#поточний час
##    time_start= int(time_now - 60*60*24*time_start)
##    time_long= (time_start-60*60*24*time_long)
##    return (time_start, time_long)
        
def buy():
    pass
def sell():
    pass
def trade_data(datestart, dateend,currencyPair="USDT_BTC"):
    r = requests.get('https://poloniex.com/public?command=returnTradeHistory&currencyPair={currencyPair}&start={datestart}&end={dateend}'.format(currencyPair=currencyPair, datestart=datestart, dateend=dateend))
    #print (" ' https://poloniex.com/public?command=returnTradeHistory&currencyPair={currencyPair}&start={datestart}&end={dateend}'.format(currencyPair=currencyPair, datestart=datestart, dateend=dateend))")
    obj = json.loads(r.text)
    #print(obj)
    return (obj)

#datestart, dateend=f_time_start(user_date_start,user_date_end)
all_data=trade_data(datestart,dateend)
feepay=fee*float(all_data[1]["rate"])
i=0
z=0
n=1
sum_time=0
all_data_count=len(all_data)

countnumber=[1,2,4,8,16]
sumacountnumber=[1,3,7,15,24]

while(i<all_data_count):
    if (i>0):
        z=i-1
    diferent_price=float(all_data[i]["rate"])- float(all_data[z]["rate"]) # різниця між останніми цінами
    time_before=all_data[z]["date"]#знаходимо в данних час
    time_now=all_data[i]["date"]
    t1=datetime.strptime(time_before, "%Y-%m-%d %H:%M:%S")
    t2=datetime.strptime(time_now, "%Y-%m-%d %H:%M:%S")
    time_diferent=float(t1.timestamp())-float(t2.timestamp()) #розраховуємо різницю часу в секундах
    sum_time=time_diferent+sum_time
    sum_price=diferent_price+sum_price  #сума різниць ціни

 #   znach= float(obj[i]["rate"])
 #   ws.cell(row=n, column=1).value = znach
 #   ws.cell(row=n, column=2).value = obj[i]["date"]
 #   ws.cell(row=n, column=3).value = proc


    if (sum_price>feepay or sum_price<-feepay ):
        print(" комісія",sum_price, "ціна",all_data[z]["rate"],"час",time_diferent, "порядковий номер", i, "номер", n)
        n+=1
        sum_price=0
        sum_time=0
    i+=1



#змінні
i=0
z=0
proc=0
riznicy=0
n=0
mycountbuy=0
countbuy=0
countnumber=[1,2,4,8,16]
sumacountnumber=[1,3,7,15,24]
mysuma=0
mymoney=0
# trailingstop=0
# trailingstopprice=0




for element in all_data:
    if (i>0):
     z=i-1
    proc=float(all_data[i]["rate"])- float(all_data[z]["rate"]) # різниця між останніми цінами
    riznicy=int(proc)+riznicy  #сума різниць
#продаємо
    if (riznicy>fee*float(all_data[z]["rate"])*4 ):
##        x=1
##        y=float(obj[z]["rate"])
##        mybuy(x,y)
        print("одна комісія",riznicy, "ціна",all_data[z]["rate"], "рахунок", i, "номер", n,"продаэмо")
        n+=1
        riznicy=0
        mycountbuy=0
        if countbuy!=0:
            mymoney=float(all_data[z]["rate"])*sumacountnumber[(countbuy-1)]-mysuma+mymoney
            print("залишок -  ",mymoney,"mysuma=",mysuma)
            tralingstop=all_data[z]["rate"]
            tralingstopcountbuy=countbuy
        mysuma=0
        countbuy=0



#купуємо
    if ( riznicy<-fee*float(all_data[z]["rate"])*4 ):
##        x=-1
##        y=float(obj[z]["rate"])
##        mybuy(x,y)
        print("одна комісія",riznicy, "ціна",all_data[z]["rate"], "рахунок", i, "номер", n,"кууємо")
        n+=1
        riznicy=0
        mycountbuy=mycountbuy+countnumber[countbuy]
        mysuma=mysuma+float(all_data[z]["rate"])*countnumber[countbuy]
        countbuy+=1
        print("mysuma сума на тепер",mysuma)
#    t=all_data[i]["date"]
    i+=1
