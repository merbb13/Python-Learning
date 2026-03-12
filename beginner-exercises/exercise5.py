print("Input a word: ")
reversed_word = ""
word = input()
for char in word:
    reversed_word = char + reversed_word
print(reversed_word)