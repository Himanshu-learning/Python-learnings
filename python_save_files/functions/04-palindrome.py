def is_palindrom(text):
    if text==text[::-1]:
        return "Palindrome text"
    return "NOT Palindrome"

def is_palin(text):
    return text==text[::-1]

text1=input("Enter your name: ")
print(is_palindrom(text1))
print("\nMethod 2: ")
print(is_palin(text1))