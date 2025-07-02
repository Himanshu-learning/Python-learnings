num=list(range(1,11))
print(f"LIST AUTO VALUES:  {num}")
poped_num=num.pop()
print(f"Poped value from num: {poped_num}")
print(f"Position of '5' in list is : {num.index(5)}")         
# Find the position of your value

num1=[1,2,3,4,5,6,7,8,2,1,5,8]
print(f"Position of '5' in list is : {num1.index(5,6)}")
# Starts searching the item 5 from position 6

#print(f"Position of '5' in list is : {num1.index(5,6,8)}")   NOT WORKING
# Starts searching the item 5 from position 6 and till position 10

print("\nASSIGNING NEGATIVE VALUE IN EMPTY LIST ")
def negative_list(l):
    negative_num=[]
    for i in l:
        negative_num.append(-i)
    return negative_num
print(negative_list(num1))

print("\nCREATING A LIST IN A FUNCTION THAT WILL RETURN ITEM SQUARE VALUE\n")
print("METHOD 1: WRONG METHOD WRONG OUTPUT")
print(num1)
def list_square(l):
    l_sq=[]
    for i in l:
        l_sq.append(l[i]*l[i])
    return l_sq
print(list_square(num1))

print("\nMETHOD 2:")
def list_sq(l):
    emp_list=[]
    for i in l:
        emp_list.append(i**2)
    return emp_list
num2=list(range(1,11))
print(num2)
print(list_sq(num2))

print("\nREVERSING A LIST USING POP AND APPEND METHOD")

def reverse1(l):
    print("\nMETHOD 1:")
    l.reverse()
    return l

def reverse2(l):
    print("\nMETHOD 2:")
    return l[::-1]


def reverse3(l):
    print("\nMETHOD 3: USING POP and APPEND METHOD")
    rev=[]
    for i in range(1,len(l)+1):
        tmp=l.pop()
        rev.append(tmp)
    return rev
number=list(range(1,11))
number1=list(range(1,11))
print(f"Number is:  {number}")
print(f"Reversed No is: {reverse1(number)}")
print(f"Reversed No is: {reverse2(number1)}")
print(f"Reversed No is: {reverse3(number1)}")    