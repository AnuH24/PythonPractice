prompt = "\nTell me something, i will repeat it back."
prompt +="\nEnter quit to end the program."
active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)