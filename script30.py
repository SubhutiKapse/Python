
#three modes ---read write append

# text--write

# f=open("mytext.txt",'w')
# text=input("enter text name : ")
# f.write(text) # file mein write kiya text
# f.close()

f=open("mytext.txt","r")
text=f.read()
print(text)
f.close()

#program 2  ---using try catch
f=None
try:
    filename=input('enter the filename')
    f=open(filename,'r')
    text=f.read()
    print(text)
except FileNotFoundError:
    print("File not found")
finally:
    if f is not None:
        f.close()
print("bye")                

#opening the file
