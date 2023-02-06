age=0
while age<70:
    age = int(input("\nPlease enter your age?"))
    if age <3:
        print("the ticket is free.")
    elif age >=3 and age <12:
        print("the ticket is $10.")
    else:
        print("the ticket is $15.")