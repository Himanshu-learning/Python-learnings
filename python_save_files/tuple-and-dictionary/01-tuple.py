mixed=(1,2,3,4,5.67,2.34)
for i in mixed:
    print(i)

print(f"\nDECLARING TUPLE: METHOD 1")

nums=(1)
words=('word1')
print(type(nums))
print(type(words))
print(type(mixed))

nums=(1,)
words=('word89',)
print(f" Integer type tuple: {type(nums)}")
print(f" String declared in tuple:  {type(words)}")

print(f"\nDECLARING TUPLE: METHOD 2")
music_in='tabla','harmonium','piano','xylophone'
print(f"{music_in} is of type: {type(music_in)}")

print(f"\n..........UNPACKINH TUPLE............")
music_in=('tabla','harmonium','piano','xylophone')
instru1,instru2,instru3,instru4=(music_in)
print(instru1)

print(f"\n.............LIST INSIDE A TUPLE.............")
tuple1=('mixed','tuple',['with','list','data_type'])
tuple1[2].pop()
print(tuple1)
tuple1[2].append("New data assinged")
print(tuple1)

print("\nData type conversion among string, list and tuple................")
txt=tuple(range(1,11))
print(txt)
print(type(txt))
txt1=list(txt)
print(type(txt1))
txt2=str(txt1)
print(type(txt2))