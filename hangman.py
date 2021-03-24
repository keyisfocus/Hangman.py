from random import choice

user_input = input("Guess the word: ")

words = ['python', 'java', 'kotlin', 'javascript']

word = choice(words)

if user_input == word:
    print("You survived!")
else:
    print("You lost!")
