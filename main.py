import random
import hangman_words
import hangman_art
from colorama import Fore, Style, just_fix_windows_console

# Enable colors on Windows
just_fix_windows_console()

name = input("Enter your name player: ")


def play_game():

    word_list = hangman_words.word_list
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    lives = 6
    guessed_letters = []
    display = ["_"] * word_length

    print(Fore.WHITE + hangman_art.logo)
    print(Fore.MAGENTA + "=" * 55)
    print(Fore.YELLOW + f"🎮 Welcome to Hangman Game, {name}! 🎮")
    
    print(Fore.GREEN + "           Made by Deepanshi Sharma")
    print(Fore.MAGENTA + "=" * 55)

    while True:

        print()
        print(Fore.CYAN + f"❤️  Lives Remaining : {lives}")

        if guessed_letters:
            print(Fore.BLUE + " Guessed Letters : " + " ".join(sorted(guessed_letters)))
        else:
            print(Fore.BLUE + " Guessed Letters : None")

        print(Fore.WHITE + "\nWord : " + " ".join(display))

        guess = input(Fore.MAGENTA + "\n * Guess a letter *: ").lower().strip()

        # Input Validation
        if len(guess) != 1 or not guess.isalpha():
            print(Fore.RED + "❌ Please enter ONLY one alphabet.")
            continue

        # Already guessed
        if guess in guessed_letters:
            print(Fore.YELLOW + f"⚠️ You already guessed '{guess}'.")
            continue

        guessed_letters.append(guess)

        # Correct Guess
        if guess in chosen_word:

            print(Fore.GREEN + f"✅ Nice! '{guess}' is in the word.")

            for position in range(word_length):
                if chosen_word[position] == guess:
                    display[position] = guess

        # Wrong Guess
        else:

            lives -= 1

            print(Fore.RED + f"❌ '{guess}' is NOT in the word.")

            print(Fore.RED + hangman_art.stages[lives])

        # Win
        if "_" not in display:

            print(Fore.GREEN)
            print("=" * 55)
            print(f"🎉 CONGRATULATIONS {name}! 🎉")
            print(f"You guessed the word: {chosen_word.upper()}")
            print("🏆 YOU WIN!")
            print("=" * 55)

            break

        # Lose
        if lives == 0:

            print(Fore.RED)
            print("=" * 55)
            print(" GAME -- OVER ")
            print(f"The correct word was: {chosen_word.upper()}")
            print("Better luck next time!")
            print("=" * 55)

            break


# -------------------------
# Play Again
# -------------------------

while True:

    play_game()

    again = input(
        Fore.CYAN + "\n🔄 Do you want to play again? (y/n): "
    ).lower().strip()

    if again != "y":
        print(Fore.MAGENTA)
        print("=" * 55)
        print(f"👋 BYE {name}! Thank you for playing Hangman!")
        print("❤️ MADE WITH LOVE by Deepanshi Sharma")
        print("=" * 55)
        break

    print("\n" * 3)