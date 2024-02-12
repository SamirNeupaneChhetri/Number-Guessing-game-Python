import random

def choose_number():
    print("| Choose a range of numbers which you want to select.... |")
    starting_number = int(input("From which number do you want to start: "))
    ending_number = int(input("Up to which number do you want to guess: "))
    random_number = random.randint(starting_number, ending_number)
    return random_number

def play_game():
    print("--------------------------------------------------------------------------")
    print("WELCOME TO THE NUMBER GUESSING GAME ....><.....")
    print("---------------------------------------------------------------------------")
    print()
    random_num = choose_number()
    print()

    attempts = 0
    while True:
        try:
            user_guess = int(input("Choose your number: "))
            attempts += 1
            if user_guess == random_num:
                print("Congratulations! You guessed the correct number.")
                print()
                break  # Exit the loop when the correct number is guessed
            elif user_guess > random_num:
                print("Your number is higher than the random number.")
                print()
            elif user_guess < random_num:
                print("Your number is lower than the random number.")
                print()
        except ValueError:
            print("Oops! You entered an invalid value. Please enter a valid number.")
            print()

    print("-------------------------------------")
    print(f"Number of attempts: {attempts}")
    print()

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        print()
        play_game()
    else:
        print("Thank you for playing!. Have Nice Day...")

if __name__ == "__main__":
    play_game()






#######--------------------------------- About this Programe ------------------------#########
'''
This is a simple number guessing game 

Here are summary of its functionality:

1 . This program prompts the user to choose a range of numbers.
2 . It genarate random number within a range.
3 . The user then attempts to guess the number, 
    receiving feedback on whether their guess is too high or too low.
4 . Once the correct number is guessed, the program displays the number of attempts made.
5 . After the game ends, the user is given the option to play again or exit.
'''
