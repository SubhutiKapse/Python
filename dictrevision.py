info = ["subhuti","kapse",21,11163]
print(info)
print(type(info))
print(len(info))


info2={
    "firstName":"Subhuti",
    "lastName":"kapse",
    "age":21,
    "rollno":2334
}
#retrive
print(info2['firstName'])
#update
info2['firstName']='Sapeksha'
print(info2)
#add
info2['city']='pune'
print(info2)
#delete
info2.pop('firstName')
print(info2)
#in
print("firstName" in info2)

#Dictionary
vehicle ={
    'color':"red",
    'type':'RangeRover'
}

print(vehicle)
print(type(vehicle))
print(len(vehicle))

#get()
q1=vehicle.get('color')
print(q1)

#program 2
vehicle ={
    'color':"red",
    'type':'RangeRover'
}
vehicle.clear()
print(vehicle)

#pop()
#vehicle.pop('color')
#w2=vehicle.popitem()
#print(w2)

#program 3

animals={
    "legs":4,
    "color":"black"
}
animals.update({"city":'nagpur'})
print(animals)


#program
info3={
    "firstName":"Subhuti",
    "lastName":"kapse",
    "age":21,
    "rollno":2334
}
for key in info3.keys():
    print(key)

for val in info3.values():
    print(val)    

for k,v in info3.items():
    print(k,v)    


print(info3['firstName'])
for x in info3:
    print(x,info3[x])    