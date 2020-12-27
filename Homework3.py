
name = input("Your Name: ")
print("Welcome " + name + "." + "Time to play hangman!\n")

word = "password"
guesses = []
turns = 15

while turns > 0:
    counter = 0
    guess = input("Guess a char: ")
    guesses.append(guess)

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("*")
            counter += 1
    
    if guess not in word:
        turns -= 1
        print("False char")
        print("You have " + str(turns) + " more guesses")

    if turns == 0:
        print("You lost the game..")

    if counter == 0:
        print("Congratulations! You won the game.")
        print("Word: " + word)

        break
