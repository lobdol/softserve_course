# # 1. Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел.
# def average  ( *args):
#     x=0
#     z=0
#     for i in args:
#        x=i+x
#        z+=1
#        rez=x/z
#     return rez
      


# #print(average(12, 23, 23, 32))

##2. Написати функцію, яка повертає абсолютне значення числа
# def absolute (x):
#     if x>0:
#         return x
#     else:
#         return -x
# print (absolute(8)) 


# #3. Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings.
# def max_number(x,z):
#     """max number"""
#     if (x<z):
#         print(z)
#     else:
#         print(x)

# max_number(34,53)
# print (max_number.__doc__)


#4. Написати програму, яка обчислює площу прямокутника, трикутника та кола (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)

def circle()
    radius=int(input(" radius = " ))
    square1=math.pi*radius**2
    print("circle area=",square1)
def rectangle()
    a2=int(input("side a="))
    b=int(input("side b="))
    square2=a2*b
    print("rectangle area = ", square2)

def triangle ()
    h=int(input("height h="))
    a3=int(input("base a="))
    square3=a3*h*0.5
    print("triangle area = ", square3)

chois=int(input("enter number(1-3). Select a figure to calculate 1-circle 2-rectangle 3-triangle isosceles  \n"))

if chois==1:
    circle()
elif chois==2:
    rectangle()
elif chois==3:
    triangle ()
