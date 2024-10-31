star = int(input("Enter the number of rows: "))

for i in range(1, star + 1):
    if i % 2 != 0:  # Check if the row number is odd
        for x in range((star - i)):
            print(' ', end='')
        for s in range(i):
            print('* ', end="")
        print()
##            print("*", end=' ')  # Print a star
# Move to the next line after finishing the row

for j in range(star - 2, 0, -1):
    if j % 2 != 0:  # Check if the row number is odd
        for x in range((star - j)):
            print(' ', end='')
        for s in range(j):
            print('* ', end="")
        print()
