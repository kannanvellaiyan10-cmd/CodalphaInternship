import random
words = ["apple", "tiger", "house", "robot", "water"]
word = random.choice(words)
display = []
for letter in word:
    display.append("_")
attempts = 6
print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
while attempts > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Attempts Left:", attempts)
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")
if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)