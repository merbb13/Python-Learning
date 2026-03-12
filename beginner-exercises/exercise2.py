print("Enter a number: ")
number = int(input())
total = 0
for i in range(number+1):
    total = i + total
print(f"The sum of numbers from 0 to {number} is {total}.")
