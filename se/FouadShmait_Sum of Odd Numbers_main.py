number = int(input("Enter a number: "))
sum = 0  # Initialize sum outside the loop

for i in range(1, number + 1):
  if(i%2!=0):
    sum += i  # Add i to sum

print("The sum of numbers from 1 to", number, "is:", sum)
  