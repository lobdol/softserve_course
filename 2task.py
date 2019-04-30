user_number_a=input("Значення змінної а \n")
user_number_b=input("Значення змінної b \n")
user_operation=input("Виберіть операцію \n додавання + \n віднімання -\n множення * \n цілочисельне ділення // \n остача від ділення % \n ")
#print( eval(user_number_a + user_operation + user_number_b) )
if (user_operation=="+"):
    print("резльтат обчислень=" , (float(user_number_a) + float(user_number_b)))
if (user_operation=="-"):
    print("резльтат обчислень=" , (float(user_number_a) - float(user_number_b)))
if (user_operation=="/"):
    print("резльтат обчислень=" , (float(user_number_a) / float(user_number_b)))
if (user_operation=="*"):
    print("резльтат обчислень=" , (float(user_number_a) * float(user_number_b)))
if (user_operation=="//"):
    print("резльтат обчислень=" , (float(user_number_a) // float(user_number_b)))
if (user_operation=="%"):
    print("резльтат обчислень=" , (float(user_number_a) % float(user_number_b)))


