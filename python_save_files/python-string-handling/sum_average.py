num1=input("Enter num 1: ")
num2=input("Enter num 2: ")
num3=input("Enter num 3: ")
sum=(int(num1)+int(num2)+int(num3))

print("sum = ", sum)
print("Average is : ",((sum)/3))
print(f"Average is : {(int(num1)+int(num2)+int(num3))/3}")

print("\nAnother input method\n")
num1,num2,num3=input("Enter three numbers separated by comma: ").split(",")
print(f"Sum of new three numbers is {int(num1)+int(num2)+int(num3)}")
print(f"Average of new three numbers : {(int(num1)+int(num2)+int(num3))/3}")