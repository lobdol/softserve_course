In this kata you will create a function that takes in a list and returns a list with the reverse order.
#Pushynskyy Kostya

def reverse_list(l):
    result=l.copy()
    x=int(len(l))
    for i in l:       
        x-=1
        result[x]=i
        
    return result