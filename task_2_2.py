#Задано чотирицифрове натуральне число. 

number=input("enter four-digit positive integer=")

#Знайти добуток цифр цього числа.
dobutok=int(number[0])*int(number[1])*int(number[2])*int(number[3])
print("product of numbers=",dobutok)

#Записати число в реверсному порядку.
number_revers=number[-1:-5:-1]
print (number_revers)

#Посортувати цифри, що входять в дане число
number_sortet="".join(sorted(number))
print(number_sortet)
