import random
import re
import hangman_art as art
import hangman_words as words
import utils

print(art.hangman_game_title)
chosen_word = random.choice(words.word_list)
chosen_word_len = len(chosen_word)
word_to_guess = "_" * chosen_word_len
lives = len(art.stages) # Adjust lives dynamically
game_over = False
guess_history = []

while not game_over:
    print(f"Word to guess:{word_to_guess}")
    user_guess = utils.get_valid_guess()

    if user_guess in guess_history:
        print(f"⚠ You've already guessed '{user_guess}'. Try again.")

    elif user_guess in chosen_word:
        print(f"You guessed Right,{user_guess} is in the word")

        # replace the all the blank with the guess letter
        word_to_guess = ""
        for letter in chosen_word:
            if letter == user_guess:
                word_to_guess += letter
            elif letter in guess_history:
                word_to_guess += letter
            else:
                word_to_guess += "_"

        print(f"Word to guess: {word_to_guess}")

        # if all the letter in the word_to_guess are not equal to '_' ,means the user successfully guess the word
        if "_" not in word_to_guess:
            game_over = True
            print(f"🎉 Congratulations! You guessed the word: {chosen_word}")
            continue
    else:
        lives = lives - 1
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("You lose!")

    guess_history.append(user_guess)

    # print hangman
    print(art.stages[lives])
    print(f"****************************{lives}/{7} LIVES LEFT****************************")

print(f"💀 GAME OVER! The word was: {chosen_word}")
