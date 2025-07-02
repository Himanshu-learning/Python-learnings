# Break loop when value is 9
print("Usage 1: Break keyword")
for i in range(11):
    if i==9:
        print("Breaking your loop since value reached 9")
        break
    else:
        print(i)

# Print 1 - 10 but not 5  so we need to apply a skip method which continue keyword does properly

print("Usage 2: continue keyword")
for i in range(1,11):
    if i==5:
        continue    
                   # when continue condition matches it directly goes to condition checking again leaving all rest work
    print(i)

