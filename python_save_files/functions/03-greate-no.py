def heavy(a,b):
    if a>b:
        return "Firsst number is greater number"
    return "Second number is greater number"
print(heavy(451,67))

print("\nMethod 2:")
# def greater(a,b):
#     if a>b:
#         return a
#     return b
# num1=input("Enter number1: ")
# num2=input("Enter number2: ")
# gr=greater(num1,num2)
# print(f"{gr} is greater number")

# print("\nMehhod 3:")
# def three_num(a,b,c):
#     if a>b and a>c:
#         return a
#     else:
#         if b>a and b>c:
#             return b
#         else:
#             return c
# gre=three_num(4,78,23)
# print(f"\n{gre} is greater among three numbers.")

def three_check(a,b,c):
    if a==b:
        if a==c:
            return "All are same numbers!"
        else:
            if a>c:
                return a
            else:
                return c
    else:
        if b==c:
            if a>b:
                return a
            else:
                return b
        else:
            if a>b and a>c:
                return a
            else:  
                if b>a and b>c:
                    return b
                else:
                    return c
store=three_check(3,3,20)
print(f"{store} is greater no.")