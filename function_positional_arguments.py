def user(first_name,last_name):
    print(f"\nMy surname is {last_name.title()}.")
    print(f"My full name is {first_name.title()} {last_name.title()}.")

#positional arguments

user("Anuraag","Hari")
user("Abhinay","Hari")

#keyword arguments

user(first_name="satya",last_name="vaduka")
user(last_name="vaduka",first_name="suneetha")