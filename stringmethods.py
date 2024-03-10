#string --methods

first_name= "subhuti"
print(type(first_name))
print("i" in first_name)

e=first_name.upper()
print(e)

name= "subhuti"
q=name.upper()
print(q)


name= "subhuti"
e=name.lower()
print(e)



name= "subhuti"
r=name.capitalize()
print(r)

name= "subhuti"
t=name.startswith("sub")
print(t)


name= "subhuti"
o=name.endswith("uti")
print(o)


name= "  subhuti"
y=name.lstrip()
print(y)

name= "subhuti "
i=name.rstrip()
print(i)


name= "  subhuti "
o=name.strip()
print(o)


name= "subhuti"
print(len(name))
l=name.rstrip()
print(l)


name= "subhuti"
ma= len(name)
i= name.strip()
print(i)


#program 1
#upper()
first_name="sapeksha"
print(len(first_name))
print(type(first_name))
print(first_name)
q1=first_name.upper()
print(q1)

#lower
last_name="kapse"
q2=last_name.lower()
print(q2)
#isupper
middle_name="ajay"
q3=middle_name.isupper()
print(q3)
#islower
middle_name="ajay"
q4=middle_name.islower()
print(q4)
#startswith()
middle_name="ajay"
q3=middle_name.startswith('a')
print(q3)
#endswith()
middle_name="ajay"
q3=middle_name.endswith('y')
print(q3)
#count()
middle_name="ajay"
q3=middle_name.count('a')
print(q3)
#rstrip()
middle_name="ajay  "
q3=middle_name.rstrip()
print(q3)
#lstrip()
middle_name="   ajay"
q3=middle_name.lstrip()
print(q3)
#strip()
middle_name="ajay"
q3=middle_name.strip()
print(q3)
#replace()
middle_name="I am subhuti"
q3=middle_name.replace("subhuti","subhi")
print(q3)
#isdigit()
w1="12333".isdigit()
print(w1)
#isalpha()
y1="12#43"
u1=y1.isalpha()
print(u1)
#isalnum()
f1=y1.isalnum()
print(f1)
#isalpha()
marks="1234"
print(marks.isalpha())

#isalnum()
marks="apple"
print(marks.isalpha())
#islower()
name="Subhuti"
name.islower()
print(name)
#startswith()
name="Subhuti"
q1=name.startswith('S')
print(q1)
#endswith()
name="Subhuti"
q1=name.startswith('ti')
q2=name.startswith('TI')
print(q1)
print(q2)
#isdigit()
rollno="123"
q1=rollno.isdigit()
print(q1)
#isalpha()
rollno="abc"
q1=rollno.isalpha()
print(q1)

#isalnum()
rollno="abc"
q1=rollno.isalpha()
print(q1)
#iscapitalize()
rollno="abc"
q1=rollno.capitalize()
print(q1)
#istitle()
q1="I Am Learning Javascript"
i1=q1.istitle()
print(i1)
#join()
info=["subhuti","kapse","8625329093"]
q1="@".join(info)
q1=",".join(info)
print(q1)
#split()
email="subhuti@gmail.com"
q1=email.split('@')
print(q1)

#find()

emailaddress="subhuti"
print(emailaddress.find('u',3))
#removeprefix()
# students=[email2,email3,email4,email5]
# listA=[]
# for x in students:
#     q1=x.removeprefix("gmail.com@")
#     listA.append(q1)
#     list(listA)
#remocesuffix()
student1={
    "1":"subhuticeo",
    "2":"shamcustomer",
    "3":"premadmin",
    "4":"agnisalesmanager"
}
roles=["ceo","manager","admin","salesmanager"]
names=[]
for name in student1.values():
    for role in roles:
        if role in name:
            w1=name.removesuffix(role)
            names.append(w1)
            print(names)

#swapcase()
            s="hell0"
            print(s.swapcase())
#zfill()
            
            name1="subhuti"
            name2="sapeksha"
            print(name1.zfill(10))
            print(name2.zfill(10))






