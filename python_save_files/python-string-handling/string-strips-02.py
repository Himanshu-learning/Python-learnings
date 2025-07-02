name="       911turbu        "
dots="............................."
print(name,dots)
print("Entry modified")
print(name.lstrip()+dots)
print(name.rstrip()+dots)
print("\nMethod 1:")
print(name.strip()+dots)
print("\nMethod 2:")
print(name.replace(" ","")+dots)
print("\nHere we will try previous program using strip method")
name,char=input("Enter the string and enter counting character separated by comma: ").split(",")
print(f"Occurance of char is : {name.strip().lower().count(char.strip().lower())}")
      