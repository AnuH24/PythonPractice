def name(first_name, last_name,age=None):
    full={"first":first_name,"last":last_name}
    if age:
        full["age"]=age
    return full
naam=name("anurag","hari",age=28)
print(naam)