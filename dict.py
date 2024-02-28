# fruits=["apple","banana","orange","pineapple"]
# print(fruits)
# print(type(fruits))
# print(len(fruits))

# #retrive
# print(fruits[0])
# #update
# fruits[0]="strawberry"
# #add
# fruits.append("kamlesh")
# print(fruits)
# #delete
# fruits.remove("banana")
# print(fruits)

# #program 2
# info2 = {
# "firstname":"subhuti",
# "lastname":"kapse",
# "age":21,
# "rollno":44

# }
# print(info2)
# print(type(info2))
# print(info2["firstname"])


# #retrive
# print(info2["lastname"])
# print(info2)

# #update
# info2["lastname"]="singh"
# print(info2)
# #delete
# info2.pop("age")
# print(info2)

# info2.popitem()
# print(info2)

# #revision
# vehicle={
#   "color":"red",
#   "type":"range rover",
# }

# print(vehicle)
# print("color" in vehicle)

# info=["subhuti","kapse",21,34]
# print(info)
# print(type(info))
# print(len(info))

# print(info[0])
# (info[0])= "sapeksha"
# print(info)
# info.append("pune")
# print(info)
# info.remove("sapeksha")
# print(info)
# info.pop()
# print(info)



# vehicle={
#     "color":"blue",
#     "type":"fararri",
#     "no":45
# }


# #retrive
# print(vehicle["color"])
# #update
# vehicle["color"]= "motion"
# print(vehicle)



# #delete
# vehicle.pop("no")
# print(vehicle)

# fruits =["apple","banana","pineapple","grapes"]
# print(fruits)
# print(fruits[0])
# fruits[0]="chickoo"
# print(fruits)
# fruits.insert(0,"mogra")
# print("fruits")

# fruits.pop()
# print(fruits)


# info2 = {
# "firstname":"subhuti",
# "lastname":"kapse",
# "age":21,
#   "rollno":44
# }


# print(info2["firstname"])
# info2["firstname"]="sanu"
# print(info2)

# info2.pop("age")
# print(info2)

# first_name="subhuti"
# last_name="kapse"
# print(type(first_name))
# q1=first_name.upper()
# print(first_name)
# w2=first_name.lower()
# print(first_name)
# e3=first_name.startswith("S")
# print(e3)
# r4=first_name.endswith("I")
# print(r4)
# p0=last_name.capitalize()
# print(p0)

# o9=last_name.isupper()
# print(o9)

# info="I am learnig javascript"
# o0=info.split('a')
# print(o0)



# info="I am learnig javascript"
# p1=info.replace("javascript","python")
# print(p1)
  
# first_name="chandrapur"
# w2=first_name.count('a')
# print(w2)



# listA=["subhuti","kapse",21,45]
# info={
#     #property :value
#     "firstName":"subhuti",
#     "lastName":"kapse",
#     "age" : 21,
#     "rollno": 45
# }


# #retrive
# print(info["firstName"])
# #update
# info["lastName"]="singh"
# print(info)

# print("rollno" in info)

# print(info["age"])

# vehicle={
#     "color":"black",
#     "type" :" range rover",
# }

# print(type(vehicle))
# print(len(vehicle))





# #program 1
# names=["subhuti","shruti","ishita","tanu"]
# print(type(names))
# print(len(names))
# print(names)

# student = {
#     "firstname":"kamlesh",
#     "lastname":"birbal",
#     "age":21,
#     "rollno" : 49
# }


# for key in  student:
#     print(key)

# for prop in student:
#     print(prop,student[prop])    

# animal ={
#     "color": "red",
#     "legs": "four",
#     "name":"tiger"
# }

# print(animal["color"])
  

# for key in animal:
#     print(key,animal[key])  


# #keys()
# for key in animal.keys():
#     print(key) 

# #values()
# for val in animal.values():
#     print(val)
       

#        #items()
# for k,v in animal.items():
#     print(k,v)   


# subject ={
#     "subone":"english",
#     "subtwo":"hindi",
#     "subthree":"marathi",
#     "subfour":"sanskrit",

# }     

# for key in subject.keys():
#     print(key)


# for val in subject.values():
#     print(val)    

# for k,v in subject.items():
#     print(k,v) 



# student={
#     "firstName":"subhuti",
#     "lastName":"kapse",
#     "rollno":22,
#     "age":21
# }       

# for key in student.keys():
#     print(key)

# for value in student.values():
#     print(value)    


# for k,v in student.items():
#     print(k,v)


# subjects={
#     "subone":"english",
#     "subtwo":"hindi",
#     "subthree":"maths",
#     "subfour":"marathi"
#     }



# subjects.pop("subone")
# print(subjects)

# subject.popitem()
# print(subjects)




# subject2 ={
#     "subone":"english",
#     "subtwo":"hindi",
#     "subthree":"maths",
#     "subfour":"marathi"
#     }
# subject3 = subject2
# print(subject3)


# subject3= subject2.copy()
# subject2["subone"]="civics"
# print(subject3)
# print(subject2)

# students3={
#     "firstName":"subhuti",
#     "lastName":"kapse"
# }
# print("hello")
# print(students3.get('firstName'))
# print('bye')


# a=students3.get('firstName')
# b=students3['firstName']
# print(a)
# print(b)

#
info1={
    "firstName":"subhuti",
    "lastName":"subhuti",
    "rollno":21,
    "age":1164
}

print(info1['firstName'])
print(info1.get('firstName'))
y=info1.setdefault('city',"pune")
print(y)
print(info1)

#info1=dict.fromkeys(["keyone","keytwo","keythree"])
#print(info1)

students=[
    {
       "firstname":"subhuti",
       "lastname":"kapse",
       "age":21,
       "skills":["html","js","python",]
    },
    {
       "firstname":"sapeksha",
       "lastname":"raichand",
       "age":21,
       "skills":["html","js","python","css"]
    },
    {
      "firstname":"shanu",
       "lastname":"singh",
       "age":21,
       "skills":["html","js","python",]
    }
]

#print(students[2]['firstname'])


# for x in students:
#     print(x['firstname'])

#program 2 #user with python skill
for x  in students:
    print(x['skills'])
    if "python" in x['skills']:
        print(x['firstname'])

#program 3 user with python skills and age >30
        for x in students:
            print(x['skills'])
            if x['age']>30 and "python" in x['skills']:   
                print(x['firstname'],x ['age'],x["skills"])     


#program 4 name and number of skills
for x in students:
 print(x['firstname']+":"+ str(len(x['skills'])))


 #average age of all students
 total=0
 for x in students:
    total=total+ x['age']
    print(total/len(students))