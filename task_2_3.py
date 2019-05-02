#Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
user_number_a=input("enter number a=")
user_number_b=input("enter number b=")
user_number_a, user_number_b = user_number_b, user_number_a
print ("number a=",user_number_a,"number b=",user_number_b)
