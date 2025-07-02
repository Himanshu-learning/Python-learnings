#import random
#win_no=random.randint(1,100)
win_no=87
attempt=1
num=int(input("Enter a number between 1-100: "))
game_over=False
while not game_over:
    if num==win_no:
        print(f"Bingo! You won the game in attempt: {attempt}")
        game_over=True
    else: 
        if num>win_no:
           print("Too high")
           attempt+=1
           num=int(input("Try again! Enter number:"))
        else:
           print("Too low")
           attempt+=1
           num=int(input("Try again! Enter number:"))
