# Hangman https://hyperskill.org/projects/69

## Stage 1 
In this stage, you should write a program that prints the lines shown in the example below.

## Stage 2
Ask the player for a possible word.
1. Print `You survived!` if the user guesses the word.
2. Print `You lost!` if the user guesses incorrectly.
3. By the way, `python` should be the word the player needs to guess to win the game.

## Stage 3
1. Create the following list of words: `'python'`, `'java'`, `'kotlin'`, `'javascript'`.
2. Program the game to choose a word from the list at random. You can enter more words, but let's stick to these four for now.

## Stage 4
1. As in the previous stage, you should use the following word list: `'python', 'java', 'kotlin', 'javascript'`
2. Once the computer has chosen a word from the list, show its first 3 letters. Hidden letters should be replaced with hyphens (`"-"`).

## Stage 5
Now your game should work as follows:

1. A player has exactly 8 tries and enters letters. Nothing changes if a player has more tries left but they have already guessed the word.
2. If the letter doesn't appear in the word, the computer takes one try away – even if the user has already guessed this letter.
3. If the player doesn't have any more attempts, the game should end and the program should show a losing message. Otherwise, the player can continue to input letters.
4. Also, the word should be selected from our list: `'python', 'java', 'kotlin', 'javascript'`, so that your program can be tested more reliably.

## Stage 6