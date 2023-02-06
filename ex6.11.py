cities={"lxpt":{"country":"india",
                "population":20000,
                "fact":"Good place to live with more greenary."},
        "hyd":{"country":"india",
               "population":80000,
               "fact":"Good place to find lot of work."},
        "gdk":{"country":"india",
               "population":30000,
               "fact":"Satya's hometown which is in peddapalli dist."}}
for key,value in cities.items():
    print(f"\nCity : {key.title()}")
    # country=f"{value['country']}"
    # country['value']= "country"
    # population=f"{value['population']}"
    # fact=f"{value['fact']}"
    # print(f"Country :", country.title())
    # print(f"Population :", population)
    # print(f"Fact :", fact)
    for i,j in value.items():
         print(f"{i.title()} : {j}".title())
    #print(f"{key} {value}".title())