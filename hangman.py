from random import choice


words = ['python', 'java', 'kotlin', 'javascript']

word = choice(words)
i = slice(3)
user_input = input(f"Guess the word {word[0:3] + '-' * (len(word) - 3)}: ")

if user_input == word:
    print("You survived!")
else:
    print("You lost!")
