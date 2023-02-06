while True:
    age=int(input("Please enter your age."))
    if age<3:
        print("the ticket is free.")
    elif age>=3 and age<12:
        print("the ticket is $10.")
    elif age >=12 and age<70:
        print("the ticket is $15.")
    elif age>=70:
        break