names=["subhuti","ruchali","raju","ajay"]
#print(names)
q1=len(names)
print(q1)

#program 2 append
names=["subhuti","ruchali","raju","ajay"]
names.append("ram")
print(names)

q1=names.append("tanu")
print(names)
print(q1)

city=["nagpur","pune","aurangabad","sitapur"]
#city.append("rampur")
#print(city)
w1=city.append("kamlapur")
print(city)
print(w1)

names=["subhuti","geeta","sita","mita"]
names.append("shiva")
print(names)

names=["subhuti","geeta","sita","mita"]
s1=names.append("aman")
print(names)

# program 3 insert

names=["subhuti","geeta","sita","mita"]
names.insert(2,"hiralal")
print(names)

fruits =["apple","banana","orange","grapes"]
fruits.insert(0,"kivi")
print(fruits)

fruits =["apple","banana","orange","grapes"]
o2 =fruits.insert(0,"kivi")
print(fruits)

#program 4 pop
fruits =["apple","banana","orange","grapes"]
fruits.pop(2)
print(fruits)

fruits =["apple","banana","orange","grapes"]
l1 =fruits.pop(2)
print(fruits)
# program 4 sort
fruits =["apple","banana","orange","grapes"]
fruits.sort()
print(fruits)

fruits =["apple","banana","orange","grapes"]
d2 =fruits.sort()
print(fruits)


#program 5 extend
fruits =["apple","banana","orange","grapes"]
fruits.extend(["strawberry"])
print(fruits)

# program 1
names =["subhuti","kumari","kamla","geeta","sita"]
print(names)
print(names[1])

#

names =["subhuti","kumari","kamla","geeta","sita"]
names.append("jasmine")
print(names)

names =["subhuti","kumari","kamla","geeta","sita"]
q1 =names.append("jasmine")
print(q1)

names =["subhuti","kumari","kamla","geeta","sita"]
names.clear()
print(names)


names =["subhuti","kumari","kamla","geeta","sita"]
o1 =names.clear()
print(o1)
#
names =["subhuti","kumari","kamla","geeta","sita"]
names.count("1")
print(names)

first_name="subhuti"
print(first_name)
last_name="kapse"
print(last_name)
print(first_name + last_name)

w= " I am learning python"
print(w)

city="pune"
print(city[0])
print(city[2])



city3 ="chandrapur"
print(city3)
print(city3[1::])
print(city3[1:6:])
print(city3[1:7:2])
print(city3[-1:-7:-2])


fruits= ["apple","banana","orange","grapes"]

print(fruits)
print(len(fruits))
print(type(fruits))

for x in range(len(fruits)):
    print(x)

for v in fruits:
    print(v)    

    fruits= ["apple","banana","orange","grapes"]
    print("turmeric" in fruits)
    #print(fruits)
    

    cities= ["nagpur","pune","aurangabad","bangalore"]
    cities2=cities
    cities2[2]="mumbai"
    print(cities2)

    fruits= ["apple","banana","orange","grapes"]
    fruits.append("tomato")
    print(fruits)

    


#methods in string
    first_name="subhuti"
    print(first_name)
    last_name="kapse"
    print(last_name)
    print(first_name + last_name)


    first_name="subhuti"
    print(type(first_name))
    print("i" in first_name)

    r=first_name.upper()
    print(r)

    r=first_name.lower()
    print(r)

r=first_name.capitalize()
print(r)



fruit="apple"
h=fruit.startswith("app")
print(h)


fruit="apple"
j=fruit.endswith("ple")
print(j)

fruit="apple"
k=(len(fruit))
print(k)

name="   subhuti"
p=name.lstrip()
print(p)

name="subhuti    "
j=name.rstrip()
print(j)



ani=("      lion     ")
k=ani.strip()
print(k)

name="subhuti"
print(type(name))
print(len(name))
print(name)

strO="1234"
t=strO.isdigit()
print(t)

strtwo="subhuti"
strthree="subhuti123"
strfour="123"
strfive="@123"

print(strtwo.isalnum())
print(strthree.isalnum())
print(strfour.isalnum())
print(strfive.isalnum())


#

info2="subhutikapse678@gmail.com"
info2.split