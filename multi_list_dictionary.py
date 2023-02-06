Anu={"bikes":["hero","honda","tvs"],
     "cars":["maruti","nissan"],
     "computers":["dell","acer","asus","hp"],
     "phones":["redmi","apple","iqoo","tecno","samsung"]}
for key, value in Anu.items():
     print(f"\n Anurag is having {key.title()} with companies:")
     for items in value:
          print(f"\t {items.title()}")