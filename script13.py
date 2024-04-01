# list / dictionary 

# program 1
# upper()
first_name = "subhuti"
print(len(first_name))
e = first_name.upper()
print(e)


# lower()
last_name = "kapse"
e2 = last_name.lower()
print(e2)


middle_name = "BRIJESH"
e3 = middle_name.isupper()
print(e3)

e4 = e2.islower()
print(e4)

# lower(), upper() , islower() ,isupper()
# program 2

city = "pune"
e5 = city.startswith("pu")
e6 = city.startswith("P")
print(e5)
print(e6)

e7 = city.endswith('e')
e8 = city.endswith('une')
print(e7)
print(e8)

city2 = "chandrapur"
e9 = city2.count('a')
print(e9)

# program 3

city3 = " wardha"
print(len(city3))
e10 = city3.lstrip()
print(e10)
print(len(e10))

city4 = " wardha "
print(len(city4))
e11 = city4.rstrip()
print(len(e11))

city5 = " wardha "
e12 = city5.strip()
print(len(e12))

# program 4
info = "I am learning javascript"
e13 = info.replace("javascript","python")
print(e13)
print(info)


# program 5
e14 = "123".isdigit() #  0 - 9
print(e14)

e15 = "1233#"
e16 = e15.isalpha()
print(e16)

e17 = e15.isalnum()
print(e17)

e18 = "hello"
e19 = "1234"
e20 = "h123"
e21 = "h12#"
print(e19.isalnum())
print(e20.isalnum())
print(e21.isalnum())


# revision
first_name = "chinmay"

# print(first_name.upper())
# print(first_name.lower())
# print(first_name.isupper())
# print(first_name.islower())


# program 2
first_name = " chinmay "
print(len(first_name))
#print(len(first_name.rstrip()))
#print(len(first_name.lstrip()))
#print(len(first_name.strip()))

#program 3
last_name = "deshpande"
print(last_name.startswith("d"))
print(last_name.startswith("de"))
print(last_name.startswith("De"))

print(last_name.endswith('e'))
print(last_name.endswith('de'))
print(last_name.endswith('Nde'))


# program 4
marks  = "123"
print(marks.isdigit()) # 0-9
print(marks.isalpha()) # A-Z a -z
print(marks.isalnum())
print(type(marks))

# program 5
full_name = " a"
e3 = full_name.isspace()
print(e3)

# program 6
firstN =  "subhuti"
e4 = firstN.capitalize()
print(e4)

e4 = "I Am Learning Javascript"
print(e4.istitle())

# program 7
info = ["subhuti","kapse","9047357945"]
e5 = "@".join(info)
print(e5)

# program 8

email = "subhuti@gmail.com"
e6 = email.split('@')  # ["subhuti","gmail.com"]
print(e6)


#find()
emailaddress = "sapeksha"
print(emailaddress.find('a',6))
#print(emailaddress.find('a',8))

#removeprefix()
email2 = "gmail.com@sapek"
email3 = "gmail.com@sha"
email4 = "gmail.com@sapeksha"

#print(email4.removeprefix('gmail.com@'))
# ["subhuti","kapse","sapeksha"]
students = [email2,email3,email4]
lista = []
for x in students:
  q1 = x.removeprefix("gmail.com@")
  lista.append(q1)
print(lista)

students = {
    "1":"shubhiadmin",
    "2":"apoorvaceo",
    "3":"shamlicustomer",
    "4":"meghamanager"
}

roles = ["admin","ceo","customer","manager"]
names = []
#names =["shubhi","apoorva","shamli","megha"] 
for name in students.values():
  for role in roles:
    if role in name:
      q2 = name.removesuffix(role)
      names.append(q2)
print(names)

#swapcase()
a = "hellO"
print(a.swapcase())

#zfill()
name = "subhuti"
name2 = "sanu"

print(name2.zfill(10))
print(name.zfill(10))