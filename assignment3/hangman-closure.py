# task 4
def make_hangman(secret_world):
    guesses = []
    def hangman_closure(letter):
        nonlocal guesses
        if letter not in guesses:
            guesses.append(letter)
        display = ''.join([char if char in guesses else '_' for char in secret_world])
        print(display)
        return all(char in guesses for char in set(secret_world))
    return hangman_closure

secret = input("Enter the secret word: ").lower()
hangman = make_hangman(secret)

while True:
    guess = input("Continue to guess: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if hangman(guess):
        print('Guess was correct!')
        break

