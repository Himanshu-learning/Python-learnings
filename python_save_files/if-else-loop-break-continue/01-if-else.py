# age=input("Enter your age: ")
# age=int(age)
# if age >= 14:
#     print("Age greate than 14")
# else:
#     print("Age less than 14")

# Create a random winning number game
win_no=29
choicen=input("Enter a number between 1-100: ")
choicen=int(choicen)
if choicen==win_no:
  print("Bingo! You won")
else:
  if choicen>win_no:
    print("You went away from winning number")
  else:
    print("You went behind the number")
    

# win_no = 29
# choicen = input("Enter a number between 1-100: ")
# choicen = int(choicen)

# if choicen > win_no:
#     print("You are away from the number")
# elif choicen < win_no:
#     print("You are behind the number")
# elif choicen == win_no:
#     print("Bingo! You won")
# else:
#     print("Seems Wrong input")


name='abc'
no=123
if name=='abc' and no==123:
  print("Exact match with 'and' operator")
else:
  print("Not matched")