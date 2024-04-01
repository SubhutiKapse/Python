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
# print(sapeksha.first_name)
# print(sapeksha.last_name)
# sapeksha.walk()
# sapeksha.talk()

# sapeksha.first_name = "sapeksha"
# sapeksha.last_name = "kapse"

# print(sapeksha.first_name)
# print(sapeksha.last_name)


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

subhuti = PersonB("subhuti","kapse")
sapeksha = PersonB("sapeksha","singh")

print(subhuti.first_name)
print(subhuti.last_name)

print(sapeksha.first_name)
print(sapeksha.last_name)
sapeksha.city = "pune"
print(sapeksha.city)
#print(subhuti.city)


#Assignment
# Vehicle 
# type model
# start() , stop()