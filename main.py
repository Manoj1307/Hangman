import random
import hangman_words
import hangman_art

print(hangman_art.logo, "\n")
chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)

guess_list = []
for i in range(0, len(chosen_word)):
    guess_list.append("_")
print("".join(guess_list))

lives = len(hangman_art.stages) - 1
while "_" in guess_list:
    guess = input("\nGuess a letter: ").lower()
    if guess in guess_list:
        print("Sorry you guessed the word already try a new one")
        continue
    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            guess_list[i] = guess
    guess_word = "".join(guess_list)
    print(guess_word)
    if guess_word == chosen_word:
        print("Congratulations, you guessed it!")
    if guess not in chosen_word:
        print(f"Sorry, that's wrong Lives left {lives}.")
        print(hangman_art.stages[lives])
        print(guess_word)
        if lives == 0:
            print("You failed to guess it GAME OVER the word was: " + chosen_word)
        else:
            lives-=1