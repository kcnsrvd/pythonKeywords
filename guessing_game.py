import random  # 'import' is used to bring the random module into the program to select a random word.

# Global variables
global attempts_left  # 'global' is used to declare attempts_left as a global variable, modifying it inside the function.
attempts_left = 6  # Number of incorrect guesses before the player loses

# Word list for the game
word_list = ["python", "global", "programming", "developer", "challenge", "library", "kyla", "guess", "elephant", "piano", "apple", "cookies",
 "remote", "basketball", "guitar", "chicken", "umbrella", "drink", "beautiful", "white", "wreck", "quiz", "hungry", "board", "sunflower", "singer",
  "dancing", "unicorn", "pirate", "computer", "information", "science", "college", "technology", "invite", "enhypen", "seventeen", "blackpink", "carat", "diamond",
   "quartz", "serenity", "concert", "challenge", "import", "variable", "reason", "recipe", "fragrant", "perfume", "university", "calcium", "sketch", "sneakers"]

# Function to choose a random word
def choose_word():  # 'def' is used to define the function choose_word.
    return random.choice(word_list)  # 'return' is used to send the randomly chosen word from the list.

# Function to display the word with hidden letters
def display_word(word, guessed_letters):  # 'def' is used to define the function display_word.
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])  # 'if' is used in the list comprehension to show letters if guessed.

# Function to play the game
def play_game():  # 'def' is used to define the function play_game.
    global attempts_left  # 'global' is used again to modify the global attempts_left variable.
    word = choose_word()  # Function call to choose_word().
    guessed_letters = set()  # 'set' is used to store guessed letters, ensuring uniqueness.
    guessed_wrong = set()  # 'set' is also used to track incorrect guesses.

    print("Welcome to Guess the Secret Word!")
    print("Try to guess the word. You have 6 attempts.")
    print("The word to guess has", len(word), "letters.")

    while attempts_left > 0:  # 'while' is used to create a loop that runs as long as there are attempts left.
        print(f"\nAttempts left: {attempts_left}")
        print(f"Guessed wrong: {', '.join(guessed_wrong)}")
        print("Current word:", display_word(word, guessed_letters))

        guess = input("Enter a letter: ").lower()  # 'input' collects the user's guess, 'lower' ensures it is lowercase.

        if len(guess) != 1 or not guess.isalpha():  # 'if' checks if the guess is a valid single letter.
            print("Please enter a valid letter.")
            continue  # 'continue' skips the rest of the loop iteration and asks for another guess.

        if guess in guessed_letters or guess in guessed_wrong:  # 'if' checks if the guess is already made.
            print("You already guessed that letter. Try another one.")
            continue  # 'continue' is used to go to the next loop iteration without continuing the game.

        if guess in word:  # 'if' checks if the guessed letter is in the word.
            guessed_letters.add(guess)  # 'add' adds the correct guess to the set of guessed letters.
            print(f"Good guess! '{guess}' is in the word.")
        else:
            guessed_wrong.add(guess)  # 'add' adds the incorrect guess to the set of wrong guesses.
            attempts_left -= 1  # Decreases the number of attempts left by 1.
            print(f"Oops! '{guess}' is not in the word.")

        # Check if the word is fully guessed
        if all(letter in guessed_letters for letter in word):  # 'if' checks if all the letters are guessed.
            print("\nCongratulations! You guessed the word:", word)
            break  # 'break' is used to exit the while loop if the word is fully guessed.

    if attempts_left == 0:  # 'if' checks if the attempts have run out.
        print(f"\nGame Over! You've run out of attempts. The word was '{word}'.")

# Function to reset the game and start over
def restart_game():  # 'def' is used to define the restart_game function.
    global attempts_left  # 'global' is used to reset the attempts_left variable.
    attempts_left = 6  # Reset the number of attempts back to 6.
    play_game()  # Calls play_game() to start the game again.

# Main function to control the game flow
def main():  # 'def' is used to define the main function that controls the game flow.
    while True:  # 'while' is used to loop the game until the user chooses to stop.
        play_game()  # Calls the play_game() function to start the game.
        play_again = input("\nWould you like to play again? (yes/no): ").lower()  # 'input' is used to get user input, 'lower' ensures it's lowercase.

        if play_again == 'yes':  # 'if' checks if the user wants to play again.
            restart_game()  # Calls restart_game() to reset the game.
        elif play_again == 'no':  # 'elif' is used to check if the user wants to exit the game.
            print("Thanks for playing! Goodbye.")
            break  # 'break' exits the while loop and ends the game.
        else:  # 'else' handles invalid inputs.
            print("Invalid input. Please type 'yes' or 'no'.")

# Run the game
if __name__ == "__main__":  # 'if' checks if this script is being run as the main program.
    main()  # Calls the main function to start the game.
