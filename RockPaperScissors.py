#Rock Paper Scissors(Just allows you to play against the computer) 

#Choices for computer to randomly choose from and for player to choose from
choices=("rock", "paper", "scissors")

#Import module that allows computer to randomly choose from selected list
import random

#Computer choice function
def get_computer_choice():
    computer=random.choice(choices)
    return computer

#Player choice function
def get_player_choice():
    while True: 
        player=input("Choose rock, paper, or scissors:").lower()
        if player in choices:
            return player
        else:
            print("Invalid Choice:Try Again!!")

#Compare choice anc determine winner function
def determine_winner(player, computer):
    if player==computer:
        return "It's a TIE!!"
    
    elif (player== "rock" and computer== "scissors") or \
         (player== "paper" and computer== "rock") or \
         (player== "scissors" and computer== "paper"):
         return "You win!!"
    
    else:
        return "Computer wins!!"

#Function to show scores 
def display_scores(round_Count,player_score,computer_score,ties):
    print("Round:", round_Count)
    print("Player Score:", player_score)
    print("Computer Score:", computer_score)
    print("Ties:", ties)


#Initialize scores and rounds
player_score = 0
computer_score = 0
Ties = 0
round_Count=0
print("GAME STARTED - SCORES INITIALIZED")

#Main game loop
while True:
    player=get_player_choice()
    computer=get_computer_choice()

    print("You chose:",player)
    print("Computer chose:",computer)

    result=determine_winner(player,computer)
    print(result)
        
    if result=="You win!!":
        player_score +=1
    elif result=="Computer wins!!":
        computer_score +=1
    else:
        ties +=1
    round_Count +=1

    Scores=display_scores(round_Count,player_score,computer_score,ties)
    print(Scores)
    
    answer=input("Want to play again? Yes/No:").lower()
    if answer=="yes":
        continue
    elif answer=="no":
        print("Thanks for playing!!!")
        exit()
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


