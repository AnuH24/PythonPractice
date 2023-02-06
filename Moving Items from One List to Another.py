unconfirmed=["abhi", "anu", "satya"]
confirmed=[]
while unconfirmed:
    current_user=unconfirmed.pop()
    print(f"verifying User: {current_user.title()}")
    confirmed.append(current_user)
print("\nThe following users have been confirmed: ")
for user in confirmed:
    print(user.title())
print(confirmed)