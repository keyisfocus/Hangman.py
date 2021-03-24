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
The player starts the game with 8 "lives", which is to say, our player can input a wrong letter 8 times.

1. Print `That letter doesn't appear in the word` and reduce the number of remaining attempts if the word selected by the program doesn't contain this letter.
2. Print `No improvements` and reduce the attempts count if the selected word contains this letter but the user has already tried guessing it.
3. The number of remaining attempts should be decreased only if there are no letters to uncover

## Stage 7
1. If the user enters the same letter twice, then the program should output `You've already guessed this letter` . This message should also be printed if the user inputs a letter that doesn't appear in the word. The number of attempts shouldn't be decreased in this case.
2. Also, you should check to make sure the player entered an English lowercase letter. If not, the program should print `Please enter a lowercase English letter` .
3. You should also check if the player entered exactly one letter. If not, the program should print `You should input a single letter` . Remember that zero is also not one!
4. Note that none of these three errors should reduce the number of remaining attempts!

## Stage 8

1. The game starts with a menu where a player can choose to either play or exit.
2. Print `Type "play" to play the game, "exit" to quit:` and show this message again if the player inputs something else.
3. If the user chooses to play, the game begins.