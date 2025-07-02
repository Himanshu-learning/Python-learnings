print("STUDYING LIST")
numbers=[1,2,3,4]
print(numbers)
words=["word1","word2","word3","word4"]
print(words)
mixed=[1,2,567,"Hundreds","Billion",3.45334,-7]
print(mixed)
print(numbers[1:2])
mixed[1]=1001
print(mixed)
mixed[1:]='arbitrary`'
print(mixed)
mixed[1:]=[24,"Dinanath",56.785]
print(mixed)

print(f"\nMethod 2:")
fruits=['mango','Guava','Coconut']
fruits.append("Pomegranate")        
#append always adds in the end of the list
print(fruits)
print("\nMETHOD 3: ")

cars=[]
cars.append('911turbo')
cars.append('Mitsubhishi')
print(cars)