# class Person:

#     # fields or properties
#     first_name = "subhuti"
#     last_name = "kapse"

#     # instance
#     def walk(self):
#         print("I am walking")

#     def talk(self):
#         print("I am talking")

# subhuti = Person()
# print(subhuti.first_name)
# print(subhuti.last_name)
# subhuti.walk()
# subhuti.talk()

# sapeksha = Person()
# print(amol.first_name)
# print(amol.last_name)
# sapeksha.walk()
# sapeksha.talk()

# sapeksha.first_name = "amol"
# sapeksha.last_name = "rao"

# print(amol.first_name)
# print(amol.last_name)


# program 2
class PersonB:
    # constructor
    def __init__(self,fn,ln):
        self.first_name  = fn 
        self.last_name = ln 

    def talk(self):
        print("I am talking")
    
    def walk(self):
        print("I am walking")

sapeksha = PersonB("sapeksha","kapse")
subhuti = PersonB("subhuti","singh")

print(sapeksha.first_name)
print(subhuti.last_name)

print(subhuti.first_name)
print(subhuti.last_name)
subhuti.city = "pune"
print(subhuti.city)
#print(amol.city)


#Assignment
# Vehicle 
# type model
# start() , stop()


    