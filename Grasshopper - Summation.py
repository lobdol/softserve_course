#Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
#Pushynskyy Kostya

def summation(num):
    res=0
    while num>0:
        res=num+res
        num-=1
    return res
