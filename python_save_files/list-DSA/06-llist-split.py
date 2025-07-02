print("\nSPLIT FUNCTION: ")
user_info='Himanshu 29'.split()
print(user_info)
user_info='Himanshu, 29, nocar'.split(',')
print(user_info)
print(f"\nJOIN METHOD: ")
user_info=['Himanshu','29']
print(','.join(user_info))
print("===========================================================================")
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(f"\n.........MATRIX............")
for i in matrix:
    print(i)
print("Matrix elements are:")
for sublist in matrix:
    for i  in sublist:
        print(i)

print(type(matrix))
