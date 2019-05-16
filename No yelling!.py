#Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing. String should be capitalized and properly spaced. Using re and string is not allowed.
#Pushynskyy Kostya

def filter_words(st):
    myString= st[:1].upper() + st[1:].lower()
    return myString