prompt="\nPlease enter the pizza toppings."
prompt +="\n Enter quit to exit."
active= True
while active:
    toppings=input(prompt)
    if toppings == "quit":
        active= False
    else:
        print(f"you have added {toppings} to your pizza.")