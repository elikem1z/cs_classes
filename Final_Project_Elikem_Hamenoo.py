import random

# Function Definitions

# Funtion to print "scissors" art
def print_scissors():
    scissors = r'''
        ____
  / __ \\
 ( (__) |___ ___
  \\________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----"""
 ( (__) |
  \\____/
    '''
    print(scissors)


# Funtion to print "Paper" art
def print_paper():
    paper = r'''
    | '_ \ / _` | '_ \ / _ \ '__|
    | |_) | (_| | |_) |  __/ |   
    | .__/ \__,_| .__/ \___|_|   
    | |         | |              
    |_|         |_|
    '''
    print(paper)


# Funtion to print "Rock" art

def print_rock():
    rock  = r''' 
                     _    
                   | |   
     _ __ ___   ___| | __
    | '__/ _ \ / __| |/ /
    | | | (_) | (__|   < 
    |_|  \___/ \___|_|\_\    

    '''

    print(rock)

# Function to display the choice made

def print_choice(choice):
    if choice == 0:
        print_rock()
    elif choice == 1:
        print_paper()
    elif choice == 2:
        print_scissors()


# Function to determine the winner

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "The game is tied"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "You lose!"


# The Game logic
def game():
    # Input Validation
    while True:
        try:
            user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
            if user in [0, 1, 2]:
                break
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Print 
    print_choice(user)

    computer = random.randint(0,2)

    print("Computer chose")

    print_choice(computer)

    print(determine_winner(user, computer))

#Play the game
game()