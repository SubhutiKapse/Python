#inheritance
#single inheritance  --- single parent single child
class Father:
    def __init__(self,fn,ln):
        self.firstName=fn
        self.lastName=ln

    def displayName(self):
        print(self.firstName+self.lastName)


class Son(Father):
    def __init__(self, fn, ln,sn):
        super().__init__(fn, ln)  
        self.sname    =sn

    def   displayName(self):
        print(self.sname+self.lastName)   
 
Ram= Son("kamlesh","ramraj","sapeksha")
print(Ram.firstName)
print(Ram.lastName)
Ram.displayName()
Ram.displayName()


# #multi-level inheritance 
# class GrandFather:
#     def __init__(self,fn,ln):
#         self.firstName=fn
#         self.lastName=ln

#     def displayGname(self):
#             print(self.firstName + self.lastName)

# class Father(GrandFather):
#     def __init__(self,fn,ln):
#         super().__init__(fn,ln)
#         self.fname= ffn
    

#     def displayFname(self):
#         print(self.fname + self.lastName)


# Ram=Son("ajay","kapse","rama","subhuti")

# print(Ram.firstName)
# print(Ram.lastName)
# print(Ram.fname)
# print(Ram.lastName)

# Ram.displayFname()
# Ram.displayGname()
# Ram.displaySname()

#herarchial inherirance
class Mother:

    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 

    def displayMName(self):
        print(self.firstName + self.lastName)


class Son(Mother):
    def __init__(self, fn, ln ,ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def displaySName(self):
        print(self.sname + self.lastName)

class Daughter(Mother):
      def __init__(self, fn, ln ,ddn):
        super().__init__(fn, ln)
        self.dname = ddn

      def displayDName(self):
         print(self.dname + self.lastName)

siddharth = Son("shivmala","kapse","siddharth")
subhuti = Daughter("shivmala","kapse","surya")

print(siddharth.firstName)
print(siddharth.lastName)
print(siddharth.sname)
siddharth.displayMName()
siddharth.displaySName()

print(subhuti.firstName)
print(subhuti.lastName)
print(subhuti.dname)
subhuti.displayMName()
subhuti.displayDName()

        
#multiple inheritance two parent one child
class Mother:
    def __init__(self,fn,ln):
        print("mother constructor called")
        self.firstName=fn
        self.lastName=ln


def displayName(self):
    print(self.firstName + self.lastName)


class Father:
    def __init__(self,fn,ln):
        print("father constructor called...")
        self.firstName=fn
        self.lastName=ln

    def displayName(self):
        print(self.firstName + self.lastName)    


class Son(Mother,Father):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)        
        self.sname=ssn


    def displayName(self):
        print(self.firstname + self.lastName)  

siddharth=Son("brijesh","kamble","siddharth")          