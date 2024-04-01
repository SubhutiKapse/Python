# # list
#            0        1       2         3
names = ["chinmay","sarika","poorva","chinmay"]
# retrive 
print(names[0])
# update 
names[0] = "tanmay"
# add 
names.append("ajay")
names.insert(2,"ninad")
# delete
names.pop()
names.pop(1)
names.remove("chinmay")
# in 
print("tanmay" in  names)

# program 2



info = ["chinmay","deshpande",34,55]

info2 = {
    #"key":value
    # property:value
    "firstName":'chinmay',
    "lastName":"deshpande",
    "age":34,
    "rollNo":55
}
#
# print(info2[0])
#retrive 
e = info2['firstName']
print(e)

# update 
info2['firstName']= "poorva"
print(info2)

# add
info2['city'] = "pune"
print(info2)

# delete 
info2.pop('firstName')
print(info2)


# program 2

vehicle = {
    "color":"red",
    "type":"sedane",
    "color":"blue"
}
print(type(vehicle))

# len()
print(len(vehicle))

#in
print("Color" in vehicle)

# duplicate keys
print(vehicle)

# retrive 
vehicle['color']
vehicle['color'] = "red"
vehicle['regNo'] = "123"
del vehicle 





















