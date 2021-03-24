from random import choice


def __play():
    lives = 8
    while lives > 0:
        print()
        print(''.join(hidden))

        if '-' not in hidden:
            print("You guessed the word!")
            print("You survived!")
            print()
            break

        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if not letter.isalpha() or not letter.islower():
            print("Please enter a lowercase English letter")
            continue
        if letter in guesses:
            print("You've already guessed this letter")
            continue

        guesses.add(letter)
        if letter not in word:
            print("That letter doesn't appear in the word")
            lives -= 1
        else:
            ind = word.find(letter)
            while ind != -1:
                hidden[ind] = letter
                ind = word.find(letter, ind + 1)
    else:
        print("You lost!")
        print()


words = ['python', 'java', 'kotlin', 'javascript']
word = choice(words)
hidden = list('-' * len(word))
guesses = set()

print(" ".join("hangman".upper()))

while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')

    if choice == "play":
        __play()

    if choice == "exit":
        break
