text="Learning python python with DJangoa and python flask is difficult"
print(text.replace(" ","_"))
print("Method 1:")
print(text.replace("python","Python_scripting"))
print("\nMethod 2:")
print(text.replace("python","Python_scripting",2))
print("\nNow we will use find keyword to get the position of searching words\nSearch 1:")
print(text.find("python"))
text="python Learning python python with DJangoa and python flask is difficult"
print("Search 2:")
print(text.find("python"))
text="on python Learning python python with DJangoa and python flask is difficult"
print("Search 3:")
print(text.find("python"))
text="on python Learning python python with DJangoa and python flask is difficult"
print("Search 4:")
print(text.find("python",5))

print("\nThis time we are finding the second word without knowing the position of first word")
text="python Learning is not that easy but python python with DJangoa and python flask is difficult"
pos=text.find("python")
pos=pos+1
print(text.find("python",pos))
