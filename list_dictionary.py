# puff={"type":"veg", "toppings":["onion","curry","corn"]}
# print(f"you ordered a {puff['type']} puff, with the following toppings: ")
# for items in (puff["toppings"]):
#     print("\t" + items)
chicken={"type":["chicken65","chilliChicken"],"toppings":["extra cheese", "extra garlic", "extra spicy"]}
print("you ordered chicken of following type: ")
for items in (chicken["type"]):
    print(items)
print("with the following toppings :")
for items in (chicken["toppings"]):
    print(items)