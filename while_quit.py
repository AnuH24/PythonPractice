prompt="\nTell me something. i will repeat it back."
prompt +="\nPlease enter quit to exit."
message=""
while message != "quit":
    message = input(prompt)
    # print(message)
    if message != "quit":
        print(message)
        #break
    # else:
    #     print(message)