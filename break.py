prompt= "\nTell me which city you would like to go?"
prompt += "\nEnter quit to exit."
while True:
    city= input(prompt)
    if city == "quit":
        break
    else:
        print(f"i would like to go to {city.title()}")