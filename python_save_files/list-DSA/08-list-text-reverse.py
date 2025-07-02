def text(l):
    item=[]
    for i in l:
        item.append(i[::-1])
    return item

def text1(l):
    for i in range(1,len(l)+1):
        print(i)

chars=['abcd','efgh','ijkl']
print(text(chars))

def even_odd(num):
    print("\n..............FILTER ODD EVEN...............\n")
    e_list=[]
    o_list=[]
    for i in num:
        if i%2==0:
            e_list.append(i)
        else:
            o_list.append(i)
    total_list=[e_list,o_list]
    return total_list

number=list(range(1,21))
print(even_odd(number))

def common_num(num1,num2):
    print("\nMatching common values only")
    print(f"Value in Num1: {num1}")
    print(f"Value in Num2: {num2}")
    takeit=[]
    if n1>n2:
        for i in range(len(n2)):
           if i in n1:
              takeit.append(i)
    else:
        for i in range(len(n1)):
           if i in n2:
              takeit.append(i)
    return takeit
        
n1=list(range(1,6))
n2=list(range(2,12))

common_l=common_num(n1,n2)
print(f"Common are:  {common_l}")
print(f"\nMaximun value in Num1 using max()  is : {max(n1)}")
print(f"Minimum value in Num1 using min()  is : {min(n1)}")
print(f"\nMaximun value in Num2 using max()  is : {max(n2)}")
print(f"Minimum value in Num2 using min()  is : {min(n2)}")

