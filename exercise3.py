vowels = ('a', 'e', 'i', 'o', 'u')
print("Enter a word: ")
word = input().lower()
count = 0
for char in word:
    if char in vowels:
        count += 1
print(f"The number of vowels in '{word}' is {count}.")
