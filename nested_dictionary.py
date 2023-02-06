hari={"anu":{"fname":"anurag",
              "lname":"hari",
             "bike":"xtreme"},
     "abhi":{"fname":"abhinay",
             "lname":"hari",
             "bike":"Apache"}}
for key, value in hari.items():
    print(f"\n Nickname: {key.title()} ")
    full_name=f"{value['fname']} {value['lname']}"
    bike=value['bike']
    print(f" FullName :", full_name.title())
    print(f" Bike :", bike.title())