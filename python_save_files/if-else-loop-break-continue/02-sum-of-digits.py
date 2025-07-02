num1=input("Enter a number: ")
length=len(num1)
i=0
sum=0
while i<length:
    sum=int(num1[i])+sum
    i+=1
print(f"\nSum of digits: {sum}")