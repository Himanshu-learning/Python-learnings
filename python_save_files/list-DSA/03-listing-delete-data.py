laptop=['dell','lenevo','acer','toshiba','hp']
print(laptop)
laptop.pop()
#This will delete the last element from lists
print("\nMETHOD 1: DELETE ELEMENT USING POP METHOD")
print(laptop)
print("\nMETHOD 2: POSITION WISE ELEMENT DELETE")
laptop.pop(1)
print(laptop)
print("\nMETHOD 3: DELETE LIST ELEMENT USING DELETE OPERATOR")
laptop=['dell','lenevo','acer','toshiba','hp']
print(laptop)
#values assinged again
del laptop[2]
print(f"DEL Operator OP: {laptop}")
print("\nMETHOD 4: SEARCH AND DELETE USING REMOVE OPERATOR")
laptop.remove('dell')
print(f"item 'dell' is deleted: {laptop}")
print(f"\Value renewed : ")
laptop=['dell','lenevo','acer','toshiba','hp','dell']
print(laptop)
laptop.remove('dell')
print(f"Only removes one match: {laptop}")
#Removes only first match not all matches found
