import random

class Player():
    def __init__(self, playerName):
        self.name = str(playerName)
        self.won = 0
        self.lost = 0
        self.RPSValue = ""
        
    def __str__(self):
        return self.name.upper() + ':' + self.RPSValue

class Bart(Player):
    def __init__(self):
        Player.__init__(self, "Bart")

    def generateRoshambo(self): 
        self.RPSValue = "rock"
        
class Lisa(Player):
    def __init__(self):
        Player.__init__(self, "Lisa")

    def generateRoshambo(self):
        self.RPSValue = random.choice(["rock","scissors","paper"])


def play(player1, player2, gamesPlayed):
    if(player1.RPSValue == "rock" and player2.RPSValue == "scissors"):
        print(f"---> {player1.name} wins!")
        player1.won += 1
        player2.lost += 1
    if(player1.RPSValue == "paper" and player2.RPSValue == "rock"):
        print(f"---> {player1.name} wins!")
        player1.won += 1
        player2.lost += 1
    if(player1.RPSValue == "scissors" and player2.RPSValue == "paper"):
        print(f"---> {player1.name} wins!")
        player1.won += 1
        player2.lost += 1
    if(player2.RPSValue == "rock" and player1.RPSValue == "scissors"):
        print(f"---> {player2.name} wins!")
        player2.won += 1
        player1.lost += 1
    if(player2.RPSValue == "paper" and player1.RPSValue == "rock"):
        print(f"---> {player2.name} wins!")
        player2.won += 1
        player1.lost += 1
    if(player2.RPSValue == "scissors" and player1.RPSValue == "paper"):
        print(f"---> {player2.name} wins!")
        player2.won += 1
        player1.lost += 1
    if(player1.RPSValue == player2.RPSValue):
        print("---> Draw!")

    print(f"{player1.name} total wins: {player1.won}/{gamesPlayed} total losses: {player1.lost}/{gamesPlayed}")
    print(f"{player2.name} total wins: {player2.won}/{gamesPlayed} total losses: {player2.lost}/{gamesPlayed}")
    return
def main():
    gamesPlayed = 0
    print("Roshambo Game\n")
    user = input("Enter your name: ")
    playerUser = Player(user)
    playerBot = ""
    print("\nHint: Bart's Roshambo is always rock")
    print("Hint: Lisa's Roshambo is selected by random\n")
    while(True):
        opponent = input("Would you like to play against Bart or Lisa? (b/B or l/L): ")
        if opponent.lower() == "b":
            playerBot = Bart()
            break
        elif opponent.lower() == "l":
            playerBot = Lisa()
            break
        else:
            print("Invalid choice. Please try again!")
            continue
    while(True):
        playerRPS = input("\nRock, paper, or scissors? (r/p/s): ")
        print()
        if(playerRPS.lower() == 'r'):
            playerUser.RPSValue = "rock"
            playerBot.generateRoshambo()
            print(playerUser)
            print(playerBot)
            gamesPlayed += 1
            play(playerUser, playerBot, gamesPlayed)

            again = input("\nPlay again? (y/n): ").lower()
            if(again == "n"):
                print("\nThanks for playing!")
                break
            elif(again == "y"):
                continue
            else:
                print("Invalid choice. Playing again!")
                continue







            
        elif(playerRPS.lower() == 'p'):
            playerUser.RPSValue = "paper"
            playerBot.generateRoshambo()
            print(playerUser)
            print(playerBot)
            gamesPlayed += 1
            play(playerUser, playerBot, gamesPlayed)


            again = input("\nPlay again? (y/n): ").lower()
            if(again == "n"):
                print("\nThanks for playing!")
                break
            elif(again == "y"):
                continue
            else:
                print("Invalid choice. Playing again!")
                continue











            
        elif(playerRPS.lower() == 's'):
            playerUser.RPSValue = "scissors"
            playerBot.generateRoshambo()
            print(playerUser)
            print(playerBot)
            gamesPlayed += 1
            play(playerUser, playerBot, gamesPlayed)



            again = input("\nPlay again? (y/n): ").lower()
            if(again == "n"):
                print("\nThanks for playing!")
                break
            elif(again == "y"):
                continue
            else:
                print("Invalid choice. Playing again!")
                continue







            
        else:
            print("Invalid choice. Please try again!")
            continue
        
        #while(True):
            #again = input("\nPlay again? (y/n): ").lower()
            #if(again == "n"):
                #print("\nThanks for playing!")
                #break
            #elif(again == "y"):
                #continue
            #else:
                ##print("Invalid choice. Playing again!")
                #continue

main()
