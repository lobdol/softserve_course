def count_sheeps(arrayOfSheeps):
    count_sheep=0
    for i in arrayOfSheeps:
        if i==True:
            count_sheep=count_sheep+1
    return count_sheep