#Rock Paper Scissors(Just allows you to play against the computer)
#Step 1 is to prompt user for their own choice
 #".lower()" will make it easier to compare the values later on due to Python being case sensitive. Don't want code to fail due to inputting invalid vlaues such as ROCK or Rock
#Step 2 is to prompt computer for its own choice by choosing randomly
#Step 3 is to figure out who wins in general
#Step 4 would be to ask player if they want to play again if yes, repeat, if no, then stop program

#This step is to confirm the choices that are allowed to be chosen from for the computer and also allows to catch any errors user might enter
import random
choices=("rock", "paper", "scissors")
#This is to establish the function used during the main game loop so that way we don't have to keep writing code repeatedly 
def determine_winner(player, computer):
    if player==computer:
        return "It's a TIE!!"
    
    elif (player== "rock" and computer== "scissors") or \
         (player== "paper" and computer== "rock") or \
         (player== "scissors" and computer== "paper"):
         return "You win!!"
    
    else:
        return "Computer wins!! :<"
    
    
#Initialize scores
player_score = 0
computer_score = 0
Ties = 0
print("GAME STARTED - SCORES INITIALIZED")

#Main game loop
while True:

    player=input("rock, paper, or scissors:").lower()

    if player not in choices:
        print("Invalid choice: Try again!")
        continue
    
    computer=random.choice(choices)

    print("You chose:", player)
    print("Computer chose:", computer)


    result=determine_winner(player, computer)
    print(result)

    if result=="You win!!":
        player_score +=1
    elif result=="Computer wins!! :<":
        computer_score +=1
    else:
        Ties +=1


    print("Player Score:", player_score)
    print("Computer Score:", computer_score)
    print("Ties:", Ties)

    
    answer=input("Want to play again? Yes/No:").lower()
    if answer=="no":
        print("Thanks for playing!!!")
        break


