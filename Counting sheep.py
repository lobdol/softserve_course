#Consider an array of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
#Pushynskyy Kostya

def count_sheeps(arrayOfSheeps):
    count_sheep=0
    for i in arrayOfSheeps:
        if i==True:
            count_sheep=count_sheep+1
    return count_sheep