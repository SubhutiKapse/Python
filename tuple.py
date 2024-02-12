name=["subhuti","shruti","kamla","vimla"]
print(name)
print(type(name))
print(len(name))
name.append("sati")
print(name)
name[0]="shyli"
print(name)


name2=["jhaplu","taplu","jay","veeru"]
print(name2)
print(type(name))
name2[2]="sallu"
print(name2)


#program 2

tupleA=(11,22)
tupleB=("subhuti","shruti")
tupleC=(["abdul","sameer"],["sikandar","shameer"])
tupleD=11,56
print(tupleA)
print(tupleB)
print(tupleC)
print(tupleD)


#program 3
names=["shibra","abdullah","faisalbaksh","gauhar"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])



#using range

for x in range(len(names)):
    print(x)
    print(names[0])


#without range
for item in names:
    print(item)        

 #program 4
tupleZ=(11,22,33,44,55,11,11,34)   
q1=tupleZ.count(11)
print(q1)


