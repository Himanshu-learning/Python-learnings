fruits=['mango','orange']
print("METHOD 1: APPEND")
fruits.append('pomegranate')
print(fruits)
print("\nMETHOD 2: INSERT")
fruits.insert(1,'grapes')
print(fruits)
print(f"\nMETHOD 3: GRAPES")
fruits.insert(20,'Litchi')
#Add at the end
print(fruits)
print(f"\nMETHOD 4: LIST CONCATENATION: ")
dish=['juice','salid','crunchies']
meal=dish+fruits
print(f"Concatenated data can be seen as: {meal}")
print(f"\nMETHOD 4: EXTENDS METHOD used as concatenation")
fruits.extend(dish)
print(fruits)
print(dish)
print(f"\nMETHOD 5: LIST INSIDE LIST  i.e. NESTED LIST")
fruits.append(dish)
print(f"APPENDED NESTED LIST is:  {fruits}")