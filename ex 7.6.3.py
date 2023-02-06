prompt="\nplease enter pizza toppings."
prompt+="\nenter quit to exit."
while True:
    toppings=input(prompt)
    if toppings == "quit":
        break
    else:
        print(f"you have added {toppings} to your pizza")