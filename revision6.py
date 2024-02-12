#list methods
animals=["tiger","lion","deer","monkey","rabbit","tiger"]
q=animals.append("giraffe")
print(animals)
print(q)
no=[11,22,33,44,11,31,11,43]
q1=no.count(11)
print(q1)

no.clear()
print(no)

names=["subhuti","shruti","manika","shyli"]
names.extend("rama")
print(names)

names.insert(0,"kamla")
print(names)

names.pop(1)
print(names)

names.reverse()
print(names)

names.remove("shyli")
print(names)

# q1=names.index("manika")
# print(q1)

q1=names.copy()
print(q1)

names.extend("manvika")
print(names)

listA=[11,12,13]
listB=listA
listB[0]=65
print(listA)
print(listB)

city=["nagpur","pune","mumbai","hyderabad"]
city2=city.copy()
city[1]="surat"
print(city)
print(city2)



#string
greet= "hello"
greet2='hi'
print(greet)

for x in range(len(greet)):
    print(x)


for x in greet:
    print(greet)    
#string methods
first_name="subhuti"
q1=first_name.upper()
print(q1)


q1=first_name.lower()
print(q1)

q1=first_name.capitalize()
print(q1)

q1=first_name.isupper()
print(q1)

q1=first_name.islower()
print(q1)


q1=first_name.startswith('s')
print(q1)

q1=first_name.endswith('i')
print(q1)

#dictonary 

info=["subhuti","kapse",21,45]
#retrive
print(info[0])
#update
info[0]="sapeksha"
print(info)
#delete
info.remove("kapse")
print(info)
#add
info.append("pune")
print(info)



name=["subhuti","kapse",21,56]
#retrive
print(name[0])
#update
name[0]="sapeksha"
#print(names)
#delete
name.remove("kapse")
print(name)
#add
name.append("pune")
print(name)

#program 2
info={
    "first_name":"subhuti",
    "last_name":"kapse",
    "age":21,
    "rollno":1116
}

print(info)
print(type(info))
print(info["first_name"])


print(info['first_name'])

#info['last_name']="shanu"

info['city']="pune"
print(info)

info['city']="mumbai"
print(info)

info.pop("age")
print(info)

info.popitem()
print(info)

vehicle={
    "color":"red",
    "type":"rangerover"
}
#retrive
print(vehicle['color'])
#update
vehicle['type']="mercedes benz"
print(vehicle)
#delete
vehicle.pop('type')
#print(vehicle)
#add
vehicle['reg no']=124
print(vehicle)

for x in vehicle:
    print(x)


subject={
    "subOne":"english",
    "subtwo":"hindi",
    "subthree":"marathi",
    "subfour":"sanskrit",
}    

for key in subject.keys():
    print(key)

for val in subject.values():
    print(val)    

for k,v in subject.items():
    print(k,v)    

#tuple vs list
listname=["subhuti","kamla","jamla","vimla"]
print(listname)        
print(type(listname))
print(len(listname))

listname.append("sapeksha")
print(listname)

listname[0]="shanu"
print(listname)

listname2=("zimba","sikandar","fatima","shibra")
print(listname2)

#using range
for x in range(len(listname2)):
    print(x)

for x in range(len(listname2)):
    print(listname2[x])

#without range
for item in listname2:
    print(item)        


#program 
    
tupleD =(11,22,33,11,44,55,11)
q = tupleD.count(11)    
print(q)

w2=tupleD.index(22)
print(w2)