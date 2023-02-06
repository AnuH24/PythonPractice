sandwitch_orders= ["veg", "chicken","pastrami","mutton", "pastrami","egg", "pastrami"]
finished_sandwitches=[]
print("the deli has run out of pastrami")
while "pastrami" in sandwitch_orders:
    sandwitch_orders.remove("pastrami")
print(sandwitch_orders)
while sandwitch_orders:
    current_order = sandwitch_orders.pop()
    print(f"I made your {current_order.title()} sandwitch")
    finished_sandwitches.append(current_order)
print(f"\nThe following sandwitches are made: ")
for items in finished_sandwitches:
    print(f"{items.title()}")