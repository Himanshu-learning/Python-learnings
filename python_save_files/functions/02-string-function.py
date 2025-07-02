def last_char(name):
    return name[-1]
print(last_char("Himanshu Sharma"))

print(f"\nPython program Even-Odd:")
def even_odd(num):
    if num%2==0:
        return "Even Number"
    else:
        return "Odd Number"
print(even_odd(97))    

print(f"\nMethod 2:")
def even_odd1(num):
    if num%2==0:
        return "Even number"
    return "Odd Number"
print(even_odd1(87))
    
print("\nMethod 3:")
def is_even(num):
    return num%2==0
print(is_even(45))

print("\nMethod 4:")
def song():
    return "Happy Birthday Song"
print(song())