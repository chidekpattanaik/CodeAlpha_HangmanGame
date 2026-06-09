# ============================================================
# CodeAlpha Internship — Task 1: Hangman Game
# Author  : AFREEN FASIHA | ID: CA/DF1/86093
# Domain  : Python Programming
# ============================================================

import random

# ── Word bank with hint sentences ──────────────────────────
WORDS = [
    ("python",      "Hint: I am a popular programming language known for simple syntax."),
    ("hangman",     "Hint: I am the name of the very game you are playing right now."),
    ("coding",      "Hint: I am the act of writing instructions for a computer to follow."),
    ("developer",   "Hint: I am a person who builds software and applications."),
    ("internship",  "Hint: I am a short-term work experience program for students."),
]

# ── Visual stages (0 wrong = safe, 6 wrong = hanged) ──────
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
]

MAX_WRONG = 6


def play_hangman():
    """Main game loop for Hangman."""
    word, hint   = random.choice(WORDS)
    guessed      = set()
    wrong_count  = 0

    print("\n" + "=" * 40)
    print("   Welcome to HANGMAN!")
    print("=" * 40)

    # ── Show the hint sentence before any guessing begins ──
    print(f"\n  {hint}")
    print(f"  The word has {len(word)} letters.\n")

    while wrong_count < MAX_WRONG:
        # ── Display current state ──────────────────────────
        print(HANGMAN_STAGES[wrong_count])
        print(f"\n  Wrong guesses : {wrong_count}/{MAX_WRONG}")
        print(f"  Letters used  : {', '.join(sorted(guessed)) if guessed else 'none'}")

        # Build the display word (revealed + blanks)
        display = " ".join(ch if ch in guessed else "_" for ch in word)
        print(f"\n  Word : {display}\n")

        # ── Check win ─────────────────────────────────────
        if all(ch in guessed for ch in word):
            print(f"  🎉  You WON! The word was '{word}'.")
            break

        # ── Get a valid single letter from the player ──────
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠  Please enter a single letter.")
            continue
        if guess in guessed:
            print("  ⚠  You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print(f"  ✅  '{guess}' is in the word!")
        else:
            wrong_count += 1
            print(f"  ❌  '{guess}' is NOT in the word.")

    else:
        # Loop exited because wrong_count reached MAX_WRONG
        print(HANGMAN_STAGES[MAX_WRONG])
        print(f"\n  💀  Game over! The word was '{word}'.")

    # ── Ask to play again ─────────────────────────────────
    again = input("\n  Play again? (y/n): ").strip().lower()
    if again == "y":
        play_hangman()
    else:
        print("\n  Thanks for playing! Goodbye.\n")


if __name__ == "__main__":
    play_hangman()
