def name(first,last):
    full=f"{first} {last}"
    return full.title()
while True:
    print(f"\nPlease tell ur name: ")
    print("enter q to quit")
    f_name=input("First Name: ")
    if f_name == "q":
        break
    l_name=input("Last Name: ")
    if l_name == "q":
        break
    new_name=name(f_name,l_name)
    print(f"\n{new_name}")