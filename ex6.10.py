fav_num={"anurag":[24,10,1994],
         "abhinay":[11,5,1992],
         "satya":[27,12,1995]}
for key, value in fav_num.items():
    print(f"\n {key.title()}'s favorite numbers are: ")
    for i in value:
        print(f"\t {i}")