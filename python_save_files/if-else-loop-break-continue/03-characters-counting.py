# METHOD 1
# name=input("Enter your name: ")
# length=len(name)
# i=0
# j=0

# while j<length: 
#    while i<length:
#        char=name[i]
#        value=name.count(char)
#        i+=1
#        print(f"Count of {char} is: {value}")
#    j+=1

# METHOD 2
name=input("Enter a name: ")
temp=""
for i in range(len(name)):
    if name[i] not in temp:
       print(f"{name[i]} has count: {name.count(name[i])}")
       temp+=name[i]


