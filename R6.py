#DICTIONARY--does not stores value by index

info = ["subhuti","kapse",21,11163]

infoB = {
    "firstName":"subhuti",
    "lastName":"kapse",
    "rollNo":11163,
    "age":21
}

# dict does not stores the value by index
#print(infoB[0])

# retrive 
print(infoB["firstName"])
#update
infoB["firstName"]= "sapeksha"
print(infoB)
# add 
infoB['city'] = "pune"
print(infoB)
# delete
infoB.pop("age")
print(infoB)


vehicle = {
    # property:value
    # key:value
    "type":"Audi",
    "model":"a1",
    "companyName":"AAt"
}

# check particular property exist
print("model" in vehicle)

# retrive 
print(vehicle['model'])

#update
vehicle['model'] = "a1"
print(vehicle)

#add 
vehicle['regNo'] = "754"
print(vehicle)

#delete
vehicle.pop("model")
print(vehicle)

#in operator
print("type" in vehicle)

# looping over dictionary

student = {
    "firstName":"subhuti",
    "lastName":"kapse",
    "age":21,
    "rollNo":90
}

for prop in student:
    print(prop,student[prop])


dictA = {
    "firstName":"subhuti",
    "lastName":"kapse",
    "age":21,
    "rollNo":45,
    "phoneNumber":9734547389
}
print(type(dictA))
# dictionary does not stores the value by index
#print(dictA[0])

# program 2
# retrive 
q1 = dictA['firstName']
print(q1)
#update 
print(dictA["lastName"])
dictA["lastName"] = "singh"
print(dictA)
#property:value
dictA['city'] = "banglore"
print(dictA)
#delete
dictA.pop("age")
print(dictA)

# program 2
# do dictionary allow same properties twice
info = {
    "color":"red",
    "type":"BMW",
    "regNo":123,
    "color":"blue"
}
print(info)

# check whether property exist in dictionary
print("Type" in info)

# methods

student = {
    "firstName":"subhuti",
    "lastName":"kapse",
    "age":23,
    "rollNo":12
}
print(student)

# get()
print("hello")
#print(student['Age'])
print(student.get('Age'))
print("bye")

# student.clear()
# print(student)

#copy

info2 = {
    "firstName":"sapeksha",
    "lastName":"singh",
    "age":23
}

# print(info2)
# info3 = info2
# info2['firstName'] = 'sani'
# print(info3)
# print(info2)

info3 = info2.copy()
info3['firstName'] = "tani"
print(info3)
print(info2)
 

info4 = {
    "firstName":"sanuksha",
    "lastName":"jaisingh",
    "rollNo":25
}

print(info4.items())
print(info4.keys())
print(info4.values())

for x in info4.values():
    print(x)

for x in info4.keys():
    print(x)

for x in info4.items():
    print(x)


info5 = {
    "firstName":"subhuti",
    "lastName":"kapse",
    "rollNo":22
}


# print(type(info5))
# e = dict.fromkeys(["firstName","lastName","age","rollNo"])
# print(e)

e = info5.setdefault('city','pune')
print(info5)

#[] ---> list
#{key:value} ---> dictionary
#()          ---> tuple
#{11,22,33}  ---> set





info6 = {
    "firstName":"subhuti",
    "lastName":"kapse",
    "age":21,
    "rollNo":34
}
e = info6.get("rollNo")
info6.clear()
info6.update({"city":"banglore"})
info6.popitem()


for k in  info6.keys():
    print(k)

for v in  info6.values():
    print(v)

for item in  info6.items():
    print(item)

info7 = info6.copy()
print(info7)
info7['firstName'] = "ishita"
print(info7)
print(info6)

e = dict.fromkeys(["color","type","model"])
print(e)

info6.setdefault('language',"marathi")
print(info6)
print(info6)




# retrive 
print(infoB["firstName"])
#update
infoB["firstName"]= "tanmay"
print(infoB)
# add 
infoB['city'] = "pune"
print(infoB)
# delete
infoB.pop("age")
print(infoB)


vehicle = {
    # property:value
    # key:value
    "type":"sedane",
    "model":"G3",
    "companyName":"Audi"
}

# check particular property exist
print("model" in vehicle)

# retrive 
print(vehicle['model'])

#update
vehicle['model'] = "G4"
print(vehicle)

#add 
vehicle['regNo'] = "123"
print(vehicle)

#delete
vehicle.pop("model")
print(vehicle)

#in operator
print("type" in vehicle)

# looping over dictionary

student = {
    "firstName":"subhuti",
    "lastName":"kapse",
    "age":23,
    "rollNo":34
}

for prop in student:
    print(prop,student[prop])


info = ["shalakha","singh",93847549,22,12]

dictA = {
    "firstName":"shalakha",
    "lastName":"singh",
    "age":22,
    "rollNo":12,
    "phoneNumber":93847549
}
print(type(dictA))
# dictionary does not stores the value by index
#print(dictA[0])

# program 2
# retrive 
q1 = dictA['firstName']
print(q1)
#update 
print(dictA["lastName"])
dictA["lastName"] = "dani"
print(dictA)
#property:value
dictA['city'] = "pune"
print(dictA)
#delete
dictA.pop("age")
print(dictA)

# program 2
# do dictionary allow same properties twice
info = {
    "color":"red",
    "type":"sedane",
    "regNo":123,
    "color":"blue"
}
print(info)

# check whether property exist in dictionary
print("Type" in info)

# methods

student = {
    "firstName":"sanvi",
    "lastName":"singh",
    "age":23,
    "rollNo":34
}
print(student)

# get()
print("hello")
#print(student['Age'])
print(student.get('Age'))
print("bye")

# student.clear()
# print(student)

#copy

info2 = {
    "firstName":"subhuti",
    "lastName":"kapse",
    "age":23
}

# print(info2)
# info3 = info2
# info2['firstName'] = 'sapeksha'
# print(info3)
# print(info2)

info3 = info2.copy()
info3['firstName'] = "sanu"
print(info3)
print(info2)
 

info4 = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "rollNo":23
}

print(info4.items())
print(info4.keys())
print(info4.values())

for x in info4.values():
    print(x)

for x in info4.keys():
    print(x)

for x in info4.items():
    print(x)


info5 = {
    "firstName":"sapeksha",
    "lastName":"kapadia",
    "rollNo":23
}


# print(type(info5))
# e = dict.fromkeys(["firstName","lastName","age","rollNo"])
# print(e)

e = info5.setdefault('city','pune')
print(info5)

#[] ---> list
#{key:value} ---> dictionary
#()          ---> tuple
#{11,22,33}  ---> set


# revision 


info6 = {
    "firstName":"subhu",
    "lastName":"prakash",
    "age":23,
    "rollNo":34
}
#e = info6.get("rollNo")
#info6.clear()
#info6.update({"city":"pune"})
#info6.popitem()
#info6.pop("age")
# for k in  info6.keys():
#     print(k)

# for v in  info6.values():
#     print(v)

# for item in  info6.items():
#     print(item)

# info7 = info6.copy()
# print(info7)
# info7['firstName'] = "veena"
# print(info7)
# print(info6)

# e = dict.fromkeys(["color","type","model"])
# print(e)

info6.setdefault('language',"marathi")
print(info6)
print(info6)


# names = ["subhuti","sapi","sanu","sanvi"]
# print(names)
# # retrive 
# print(names[0])
# # add 
# names.append("sayli")
# names.insert(2,"hello")
# #update 
# names[0] = "shamli"
# # delete
# names.pop()
# names.pop(1)
# names.remove("subhuti")

#          0            1     2   3
info = ["subhuti","kapse",22,66]
print(info)
info = {
    "firstName":"subhuti",
    "lastName":"kapse",
    "age":22,
    "rollNo":66
}
print(info)
print(type(info))

info = {
    "firstName":"subhuti",
    "lastName":"kapse",
    "age":21,
    "rollNo":66,
    "lastName":"singh"
}
# retrive 
print(info['firstName'])
print(info['lastName'])
# update
info['firstName'] = "sapeksha"
print(info)
# does dictionary stores duplicate key-value / property-value?
#no

# how to find specfic key/ property exist in dictionary
print("age" in info)
print("city" in info)
# add the property
info['city'] = "pune"
print(info)


# how to loop over dictionary 
vehicle = {
    "color":"black",
    "type":"bmw",
    "regNo":123
}
print(vehicle)
for key in vehicle:
    print(key,vehicle[key])


for prop in vehicle:
    print(prop,vehicle[prop])

# how to find total number of properties in dictionary
q2 = len(vehicle)
print(q2)



info6 = {
    "firstName":"subhuti",
    "lastName":"kapse",
    "age":23,
    "rollNo":34
}
#e = info6.get("rollNo")
#info6.clear()
#info6.update({"city":"pune"})
#info6.popitem()
#info6.pop("age")
# for k in  info6.keys():
#     print(k)

# for v in  info6.values():
#     print(v)

# for item in  info6.items():
#     print(item)

# info7 = info6.copy()
# print(info7)
# info7['firstName'] = "sapeksha"
# print(info7)
# print(info6)

# e = dict.fromkeys(["color","type","model"])
# print(e)

info6.setdefault('language',"marathi")
print(info6)
print(info6)




#print(info6)