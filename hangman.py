from random import choice

print(" ".join("hangman".upper()))
print()

words = ['python', 'java', 'kotlin', 'javascript']

word = choice(words)

hidden = list('-' * len(word))

for _ in range(8):
    print(''.join(hidden))
    letter = input("Input a letter: ")
    if letter not in word:
        print("That letter doesn't appear in the word")
    else:
        ind = word.find(letter)
        while ind != -1:
            hidden[ind] = letter
            ind = word.find(letter, ind + 1)
    print()

print("Thanks for playing!")
