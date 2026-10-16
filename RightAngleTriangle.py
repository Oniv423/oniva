print("Half Pyramids Patterns of Star (*): ")
n  = int(input("enter the numbers of rows: "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()