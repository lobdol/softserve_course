#Given an array of integers.

#Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

#If the input array is empty or null, return an empty array.
#Pushynskyy Kostya

def count_positives_sum_negatives(arr):
    result=[0,0]
    for i in arr:
        if i>0:
            result[0]=result[0]+1
        elif i<0:
            result[1]=result[1]+int(i)
    if len(arr)==0:
        result=[]
        
    return result
    