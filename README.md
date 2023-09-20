# RoshamboRivals
#Roshambo Rivals
Play the classic game of Rock-Paper-Scissors against two iconic computer players: Bart, who always throws rock, and Lisa, who makes a random choice each round. Dive into a session of strategic play and see if you can outsmart them!

##*Description
Roshambo Rivals is an object-oriented Python module designed to offer a straightforward yet engaging Rock-Paper-Scissors gaming experience. It provides a simplistic inheritance-based structure without the complexities of class attributes, object compositions, or property methods. This ensures a neat and tidy codebase perfect for those who are delving into OOP.

##*Features
Player Class: Represents a player, with attributes for the player's name, their choice of Roshambo, and counters for their wins and losses during the gaming session.
Bart Class: A derived class from Player, representing Bart who always chooses rock.
Lisa Class: Another derived class from Player, representing Lisa who makes a random choice between rock, paper, and scissors each round.
Game Count: Keeps track of the games played during the session.
Game Result: A function that determines the winner of each round and displays the outcome, as well as the updated score.
Replay Option: After each round, players can decide to continue playing or end the session.

##*Gameplay
Start the Game: Upon launching roshambo.py, the game title is displayed, and you'll be prompted to enter your name.

Choose Your Opponent: Play against Bart or Lisa. Each has a unique strategy!

Make Your Move: Choose from rock (r/R), paper (p/P), or scissors (s/S). If an invalid choice is made, you'll get a chance to re-enter your choice.

Game Outcome: After each round, the choices of both players are revealed, and the result of the game is displayed.

Scoreboard: Keep track of your wins, losses, and the total games played.

Play Again: After each round, decide if you'd like another go at beating your computer opponent. If not, the game will end with a friendly message.

##*Running the Game
To play Roshambo Rivals, execute the roshambo.py file in your Python environment.
