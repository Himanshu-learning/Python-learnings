# 0 1 1 2 3 5 8 13 21 34 55 89

a=sum=0
b=1
print(a)
print(b)
for i in range(8):
    sum=a+b
    print(sum)
    a=b
    b=sum
