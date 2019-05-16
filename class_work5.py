# #cmd: pip install pyowm
# import pyowm
# city=input("What city you are interested:")
# owm = pyowm.OWM(' your-API-key ef2206ff5da67de63306d0b143e20872')    # You MUST provide a valid API key
# # Have a pro subscription? Then use:
# # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
# # Search for current weather in the city

# observation = owm.weather_at_place(city)
# w = observation.get_weather()
# temperature=w.get_temperature('celsius')['temp']
# print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature) + " for the Celsius")
# print("In this city "+ w.get_detailed_status())



# #1. Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 і пропонує користувачу вгадати це число. Програма зчитує числа, які вводить користувач і видає користувачу підказки про те чи загадане число більше чи менше за введене користувачем. Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, тоді друкує повідомлення привітання. (для виконання завдання необхідно імпортувати модуль random, а з нього функцію randint())

# import random
# a=random.randint(1,100)
# #print(a)
# b=0
# while (a!=b):
#     b=int(input("guess the number"))
#     if (a>b):
#         print("too small")
#     elif (a<b): 
#         print("too big")
# print("your win")
            

            
#2. Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. (для виконання завдання необхідно імпортувати модуль math, а з нього функцію pow() та значення змінної пі).

import math
chois=int(input("enter number(1-3). Select a figure to calculate 1-circle 2-rectangle 3-triangle isosceles  \n"))
if chois==1:
    radius=int(input(" radius = " ))
    square1=math.pi*radius**2
    print("circle area=",square1)
elif chois==2:
    a2=int(input("side a="))
    b=int(input("side b="))
    square2=a2*b
    print("rectangle area = ", square2)
elif chois==3:
    h=int(input("height h="))
    a3=int(input("base a="))
    square3=a3*h*0.5
    print("triangle area = ", square3)