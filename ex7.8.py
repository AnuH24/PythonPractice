sandwitch_orders=["veg", "egg", "chicken"]
finished_sandwitches=[]
while sandwitch_orders:
    current_order=sandwitch_orders.pop()
    print(f"I made your {current_order.title()} sandwitch")
    finished_sandwitches.append(current_order)
print(f"\nThe following sandwitches are made: ")
for items in finished_sandwitches:
    print(f"{items.title()}")