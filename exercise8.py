word = input("Enter a word: ")

counts = {}

for char in word:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

for letter, count in counts.items():
    if count > 1:
        print(letter)