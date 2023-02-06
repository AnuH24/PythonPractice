# Databricks notebook source
print("Hello Anuraag")

# COMMAND ----------

first_name = "Anuraag"
last_name = "Hari"
print(first_name + last_name)

# COMMAND ----------

a = "Anuraag"
print (a)
a = "Abhinay"
print (a)

# COMMAND ----------

a = "anuraag hari"
print(a.title())
print(a.upper())
print(a.lower())

# COMMAND ----------

first_name = "Anuraag"
last_name = "Hari"
full_name = f"{first_name} {last_name}"
fullName = "{} {}".format(first_name, last_name)
print(full_name)
print(fullName)
print(f"hello, {first_name} {last_name}".title())

# COMMAND ----------

print("hello \t welcome \n to python")

# COMMAND ----------

name = " Anuraag "
print(name)
print(name.rstrip())
print(name.lstrip())


# COMMAND ----------

a=8
b=2
c=4.0
print("add=",a+b)
print("sub=",a-b)
print("mul=",a*b)
print("div=",a/b, "output will be float")
print("power=",a**b)
print("float_div=",a/c)
print("float_mul",b*c)

# COMMAND ----------

print("add=",5+3)
print("sub=",10-2)
print("mul=",4*2)
print("div=",16/2, "output will be float")
print("power=",2**3)

# COMMAND ----------

hari= ['suni', 'raj', 'abhi', 'anu']
print(hari)
print(hari[3].title()) #title case will work only for a single item at a time in a list
print(hari[0])
print(hari[2])
print(hari[-1]) #alternate to access last item
a=f"head of the family is {hari[1].title()}"
print(a)
print(f"head of the family is {hari[1].title()}")
print(f"Hello {hari[0].title()}, Have a Nice Day.")
print(f"Hello {hari[1].title()}, Have a Nice Day.")
print(f"Hello {hari[2].title()}, Have a Nice Day.")
print(f"Hello {hari[3].title()}, Have a Nice Day.")
hari[0]="raj"
print(hari)
hari[1]="suni"
print(hari)
hari.append("satya")
hari.append("vijaya")
print(hari)
hari.insert(0, "narayana")
print(hari)
del hari[6]
print(hari)

# COMMAND ----------

print(hari)
hari.append("vijaya")
print(hari)
popped_name=hari.pop(6)
print(popped_name)
print(hari)
hari.append("vijaya")
print(hari)
hari.remove("vijaya")
print(hari)
print(f"we lost {hari[7]}")
hari.sort()
print(hari)
hari.sort(reverse=True)
print(hari)

# COMMAND ----------

hari= ['suni', 'raj', 'abhi', 'anu', 'narayana', 'vijaya']
print(hari)
print(sorted(hari))
hari.append("satya")
print(hari)
hari.reverse()
print(hari)
print(len(hari))

# COMMAND ----------

for harizz in hari:
  print(harizz)
for harizz in hari:
  print(f"have a nice day {harizz.title()}")
print(f"thank you {harizz.title()}")

# COMMAND ----------

for value in range(0,5):
  print(value)
numbers= list(range(0,6))
print(numbers)
even_numbers=list(range(0,13,2))
print(even_numbers)

# COMMAND ----------

squares=[]
for value in range (1,10):
  square=value ** 2
  print(square)
  squares.append(square)
print(squares)
Squares=[value**2 for value in range (0,10)]
print(Squares)

# COMMAND ----------

digits=[0,1,2,3,4,5,6,7,8,9]
print(min(digits))
print(max(digits))
print(sum(digits))

# COMMAND ----------

values=[]
for value in range (1,1000001):
  values.append(value)
print(min(values))
print(max(values))
print(sum(values))

# COMMAND ----------

for value in range (1,20,2):
  print(value)

# COMMAND ----------

multiple_3=[]
for values in range (3,30,3):
  multiple_3.append(values)
print(multiple_3)

# COMMAND ----------

cubes=[]
for values in range(1,10):
  value=values**3
  cubes.append(value)
print(cubes)
  

# COMMAND ----------

cubes=[value**3 for value in range (1,10)]
print(cubes)

# COMMAND ----------

print(hari)
print(hari[0:3])
print(hari[1:4])
print(hari[:4])
print(hari[0:])
print(hari[-3:])

# COMMAND ----------

for members in hari[:4]:
  print(members.title())


# COMMAND ----------

new_hari=hari[:]
print(new_hari)
new_hari.append("boy")
hari.append("girl")
print(hari)
print(new_hari)

# COMMAND ----------

a=(10,20)
print(a[0])
print(a[1])

# COMMAND ----------

a

# COMMAND ----------

for value in a:
  print (value)
a=(30,40,50)
print("\nnew a values is: ")
for value in a:
  print(value)

# COMMAND ----------

tiffins=("dosa", "poori")
for items in tiffins:
  print(items)
new_tiffins=("poori", "idli", "wada", "upma")
print("\nnew foods added: ")
for items in new_tiffins:
  print(items)

# COMMAND ----------

cars=("maruti800", "terrano", "wagonr", "brezza", "grand vitara")
for car in cars:
  if car == "terrano":
    print(car.upper())
  else:
    print(car.title())

# COMMAND ----------

starters="chicken65"
if starters != "egg65":
  print("Hold your balls n wait")

# COMMAND ----------

a=42
if a!=30:
  print("this is not the a value, try again!")

# COMMAND ----------

age=28
age==28

# COMMAND ----------

age>=30

# COMMAND ----------

age_0=28
age_1=30
age_0==28 and age_1==31

# COMMAND ----------

age_0>=29 or age_1==30

# COMMAND ----------

i=["chicken65", "veg65", "chicken manchuria", "veg manchuria"]
print(i)
if i == "chilli chicken":
  print("enjoy")
elif i == "chicken650":
  print("enjoy chicken65")
else:
  print("sorry not available.\nplease select the startes from the above menu")

# COMMAND ----------

a=["b", 'c', 'd']
m='n'
if m not in a:
  print("no")
else:
  print("bye")

# COMMAND ----------

name="abhi"
sur_name="hari"
full_name="{} {}".format(name,sur_name)
print(full_name)

# COMMAND ----------

age=18
if age>=18:
  print("you are eligible for a driving licence")
else:
  print("you can apply after 18 years")

# COMMAND ----------

age=70
if age<2:
  print("you are a baby")
elif age>=2 and age<4:
  print("you are a toddler")
elif age>=4 and age<13:
  print("you are a kid")
elif age>=13 and age<20:
  print("you are a teenager")
elif age>=20 and age<65:
  print("you are an adult")
else:
  print("you are an elder")

# COMMAND ----------

starters=["chicken65", "veg65", "chicken manchuria", "veg manchuria"]
for item in starters:
  print(f"adding {item}")
print("\nyour order is complete")

# COMMAND ----------

available_starters=["chicken65", "veg65", "chicken manchuria", "veg manchuria", "gobi65", "prawns65"]
requested_starters=["chilli chicken", "prawns65", "mushroom65", "gobi65"]
for requested_starter in requested_starters:
  if requested_starter in available_starters:
    print(f"Adding {requested_starter}")
  else:
    print(f"Sorry {requested_starter} is not available")
print("\nYour order is complete ")

# COMMAND ----------

import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder\
                    .appName('SparkByExamples.com') \
                    .getOrCreate()
spark.range(1000 * 1000 * 1000).count()

# COMMAND ----------

anu={"name":"Anuraag", "height":5.6}
print(anu["name"])
print(anu["height"])

# COMMAND ----------

a={"x":0,"y":2,"speed":"medium"}
print(f"the original position is : {a['x']}")
if a["speed"]== "slow":
  x_a=1
elif a["speed"]== "medium":
  x_a=2
else:
  x_a=3
a['x']=a['x']+ x_a
print(f"new position is: {a['x']}")

# COMMAND ----------

a={"name":"anurag", "colour":"white", "height":5.6}
print(a)
del a["height"]
print(a)

# COMMAND ----------

a={"name":"anurag", "colour":"white", "height":5.6, "bike":"xtreme"}
print(a)
colour=a["colour"].title()
print(f"the colour of anurag is {colour}")

# COMMAND ----------

b=a.get("bikeColour","no colour mentioned")
print(b)
print(a)

# COMMAND ----------

person={'first_name':'abhinay','last_name':'hari','age':30, 'city':'hyderabad'}
print(person)
for key,value in person.items():
  #print(f"{key}:{value}")
  print('{}:{}'.format(key,value))
# for details in person.items():
#   print(details)

# COMMAND ----------

persons={'anurag':1024, 'abhi':1105, 'raj':3272, 'suni':2906}
print(persons)
for key, values in persons.items():
  print(f"{key.title()} : {values}")

# COMMAND ----------

fav_cars={'abhi':'audi', 'anu':'vitara', 'raj':'wagonr', 'suni':'maruti800'}
for name, cars in fav_cars.items():
  #print(f"\n{name.title()}'s favorite car is {cars.title()}")
  print("\n{}'s favorite car is {}".format(name.title(),cars.title()))
for name in fav_cars.keys():
  #print(f"\n{name.title()}")
  print("\n{}".format(name.title()))

# COMMAND ----------



# COMMAND ----------

fav_cars={'abhi':'audi', 'anu':'vitara', 'raj':'wagonr', 'suni':'maruti800'}
bros=['abhi', 'anu']
for name in fav_cars.keys():
  print(f"\n {name.title()}")
  if name in bros:
    cars=fav_cars[name].title()
    print(f"\t {name.title()} loves {cars.title()} car")
if "satya" not in fav_cars:
  print(f"\nSatya, what is your favorite car?")

# COMMAND ----------

fav_cars={'abhi':'audi', 'anu':'vitara', 'raj':'wagonr', 'suni':'maruti800'}
for names in sorted(fav_cars.keys()):
  print(f"\n {names.title()}, Thank You")
for key,value in fav_cars.items():
  print(f"\n {key.title()}'s favorite car is {value.title()}, Thank You")

# COMMAND ----------

fav_cars={'abhi':'audi', 'anu':'vitara', 'raj':'wagonr', 'suni':'maruti800', 'satya':'audi'}
print("The cars are :")
for cars in set(fav_cars.values()):
  print(cars.title())

# COMMAND ----------

fav_cars={'abhi':'audi', 'anu':'vitara', 'raj':'wagonr', 'suni':'maruti800'}
bros=['abhi', 'anu','satya','moni']
for i in bros:
  if i not in fav_cars:
    print(f"{i.title()}, what is your favorite car?")
  else:
    print(f"{i.title()}, Thanks for participating")

# COMMAND ----------

a={'hero':2,'honda':1,'tvs':1}
b={'nissan':1, 'maruti':1, 'xtreme':1}
c={'activa':1, 'apache':1, 'glamour':1}
d=[a,b,c]
for items in d:
  print(items)

# COMMAND ----------

details=[]
for i in range(7):
  new_details={'hero':2,'honda':1,'tvs':1}
  details.append(new_details)
  print(details)
for i in details[:3]:
  print(i)
print(f"\n total number of items created are :{len(details)}")
for i in details[:3]:
  if i['hero']==2:
    i['hero']=3
    i['honda']=4
    i['tvs']=5
print(details)
