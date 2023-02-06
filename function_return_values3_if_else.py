def name(first,last,middle=""):
    if middle:
        full=f"{first} {middle} {last}"
    else:
        full=f"{first} {last}"
    return full.title()
naam=name("rajendra","hari","prasad")
print(naam)
naam=name("anuraag","hari")
print(naam)