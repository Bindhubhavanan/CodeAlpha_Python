import random

def get_random_word():
    # List of words for the Hangman game
    word_list = ['python', 'java', 'hangman', 'computer', 'programming', 'developer', 'algorithm', 'puzzle']
    return random.choice(word_list)

def display_word(word, guessed_letters):
    # Display the word with underscores for unguessed letters
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    # Select a random word
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # You can set the number of allowed incorrect guesses
    
    print("Welcome to Hangman!")
    print("You have to guess the word.")
    print("You can make up to", max_incorrect_guesses, "incorrect guesses.")
    
    while incorrect_guesses < max_incorrect_guesses:
        # Display the current word with guessed letters
        print("\nCurrent word: ", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print("Guessed letters:", ', '.join(sorted(guessed_letters)))
        
        # Get the player's guess
        guess = input("Enter a letter: ").lower()

        # Check if the input is a valid single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.")
            continue
        
        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(guess)
        
        # Check if the guessed letter is in the word
        if guess not in word:
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")
        else:
            print(f"Good guess! '{guess}' is in the word.")
        
        # Check if the player has guessed the word
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        # If the player runs out of guesses
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
