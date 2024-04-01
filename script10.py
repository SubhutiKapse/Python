info3 = {

    "firstName":"subhuti",
    "lastName":"kapse",
    "rollNo":21,
    "age":4523

}

print(info3['firstName'])
print(info3.get('firstName'))
y = info3.setdefault('city',"pune")
print(y)
print(info3)



# info4 = dict.fromkeys(["keyone","keytwo","keythree"])
# print(info4)

students = [
    {
        "firstName":"sapeksha",
        "lastName":"singh",
        "age":23,
        "skills":["html","css","js"]
    },
    {
        "firstName":"sanvi",
        "lastName":"kumar",
        "age":32,
        "skills":["html","css","js","python"]
    },
    {
        "firstName":"sakshi",
        "lastName":"kamble",
        "age":23,
        "skills":["html","css","js"]

    }

]
#print(students[2]['firstName'])

# for x in students:
#     print(x['firstName'])

# program 2 # user with python skill
for x in students:
   # print(x['skills'])
    if "python" in x['skills']:
        print(x['firstName'])

# program 3 user with python skills and age > 30
        
for x in students:
    if x['age'] > 30 and "python" in x['skills']:
        print(x['firstName'],x['age'],x["skills"])

# program 4 name and number of skills 
for x in students:
    print(x['firstName']+":"+ str(len(x['skills'])))

# average age of all students 
total = 0
for x in students:
    total = total + x['age']

print(total/len(students))

# loops , list , dictionary