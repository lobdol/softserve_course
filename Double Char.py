#Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
#Pushynskyy Kostya

def double_char(s):
    l=len(s)
    string=""
    i=0
    while i<l:
        print(i)
        string+=s[i]*2
        i+=1
    return string