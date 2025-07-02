def add_two(a,b):
    return a+b
total=add_two(5,7)
print(total)
print(add_two(7,2))

print("Method 2:")
def two_add(num1,num2):
    return num1+num2
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
print(f"Sum of {a} and {b} is {two_add(a,b)}")

print(f"\nMethod 3:")
name1=input("Enter first name: ")
name2=input("Enter second name: ")
print(f"You full name is : {two_add(name1,name2)}")

print("Method 4:")
def add_three(a,b,c):
    print(a+b+c)
add_three(5,6,7)