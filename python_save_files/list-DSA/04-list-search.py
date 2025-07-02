laptop=['dell', 'lenevo','SAMSUNG', 'acer', 'toshiba', 'hp','Xiomi','dell']
if 'toshiba' in laptop:
    print("Toshiba as input found")
else:
    print("Element not in list")
print(f"\n'dell' occurance in list: {laptop.count('dell')}")
laptop.sort()
print(f"\nMETHOD 1: SORTING THE LIST USING SORT FUNCTION :")
print(laptop)
number=[12,7,18,8,2,20,11,12]
print(f"\nNumbers list is : {number}")
number.sort()
print(f"Sorted numbers are:  {number}")
number=[12,7,18,8,2,20,11,12]
print("\nMETHOD 2: SORTED FUNCTION TO SORT LIST ITEMS")
print(f"\nAgain assinged Numbers list is : {number}")
print(f"Sorted list is  : {sorted(number)}")
print("\nMETHOD 4:COPYING A LIST: ")
number_copy=number.copy()
print(f"Copied new list is number_copy with items:  {number_copy}")
print("\nMETHOD 5: DELETING ELEMENTS OF LIST: ")
number.clear()
print(f"Number list after using clear function: {number}")