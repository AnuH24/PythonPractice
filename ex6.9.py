fav_places={"anurag":["lxpt","hyd"],
            "abhinay":["lxpt","hyd","gdk"],
            "satya":["gdk","vangara","hyd","lxpt"]}
for key,value in fav_places.items():
    print(f"\n {key.title()} favorite places are :")
    for i in value:
        print(f"\t {i.title()}")
