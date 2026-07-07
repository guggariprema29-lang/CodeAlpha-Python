import random

# List of predefined words
words = ["apple", "banana", "python", "computer", "flower"]

# Select a random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("===== Welcome to Hangman Game =====")

while incorrect_guesses < max_incorrect:
    display_word = ""

    # Display guessed letters and underscores
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", max_incorrect - incorrect_guesses)

# If player loses
if incorrect_guesses == max_incorrect:
    print("\n💀 Game Over!")
    print("The correct word was:", word)