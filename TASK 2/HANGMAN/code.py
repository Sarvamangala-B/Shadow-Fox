import random

# Hangman stages (ASCII art)
HANGMANPICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# Step 1: Word list with categories (word, hint)
words = [
    ("python", "Programming Language"),
    ("elephant", "Animal"),
    ("pizza", "Food"),
    ("guitar", "Musical Instrument"),
    ("india", "Country")
]

# Step 2: Randomly choose a word
word, hint = random.choice(words)
word = word.upper()
guessed = ["_"] * len(word)

# Step 3: Game variables
lives = len(HANGMANPICS) - 1
used_letters = []

print("🎮 Welcome to Hangman!")
print(f"Hint: {hint}")

# Step 4: Game loop
while lives >= 0 and "_" in guessed:
    print(HANGMANPICS[len(HANGMANPICS) - 1 - lives])
    print("Word:", " ".join(guessed))
    print("Used letters:", ", ".join(used_letters))
    print(f"Lives left: {lives}\n")

    guess = input("Enter a letter: ").upper()

    # Check if already used
    if guess in used_letters:
        print("⚠️ You already guessed that letter.\n")
        continue
    used_letters.append(guess)

    # Correct guess
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("✅ Correct!\n")
    else:
        lives -= 1
        print("❌ Wrong guess!\n")

    # Win/Loss check
    if "_" not in guessed:
        print("🎉 Congratulations! You guessed the word:", word)
        break
    elif lives < 0:
        print(HANGMANPICS[-1])
        print("💀 Game Over! The word was:", word)
        break
