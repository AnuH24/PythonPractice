prompt= "\nPlease enter the Pizza Toppings."
prompt += "\nEnter quit to exit."
toppings= ""
while toppings != "quit":
    toppings= input(prompt)
    if toppings !="quit":
        print(f" U have added {toppings} to your Pizza")