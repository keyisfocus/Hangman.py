from random import choice

print(" ".join("hangman".upper()))

words = ['python', 'java', 'kotlin', 'javascript']

word = choice(words)

hidden = list('-' * len(word))

lives = 8
guesses = set()

while lives > 0:
    print()
    print(''.join(hidden))

    if '-' not in hidden:
        print("You guessed the word!")
        print("You survived!")
        break

    letter = input("Input a letter: ")

    if letter not in word:
        print("That letter doesn't appear in the word")
        lives -= 1
    elif letter in guesses:
        print("No improvements")
        lives -= 1
    else:
        guesses.add(letter)
        ind = word.find(letter)
        while ind != -1:
            hidden[ind] = letter
            ind = word.find(letter, ind + 1)

if lives == 0:
    print("You lost!")
