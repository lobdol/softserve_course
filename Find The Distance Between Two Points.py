#Given two ordered pairs calculate the distance between them. Round to two decimal places. This should be easy to do in 0(1) timing.
#Pushynskyy Kostya

def distance(x1, y1, x2, y2):
    x=x1-x2
    y=y1-y2
    distance=((x**2+y**2)**.5)    
    return float('{:.2f}'.format(distance))