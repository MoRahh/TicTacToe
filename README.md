# Tic Tac Toe with Minimax AI
This is a simple implementation of the classic Tic Tac Toe game, with an unbeatable AI player based on the Minimax algorithm.

# How to use
To use this program, you will need to have Python 3 and Pygame installed on your machine. Once you have them, you can clone this repository and run the tictactoe.py file. The game will open in a new window, and you can start playing against the AI or against another human player by changing the gamemode to 'pvp'. The rules are the same as the traditional Tic Tac Toe game: each player takes turns to place their symbol (X or O) on the board, and the first player to get three in a row wins.

# AI player
The AI player in this game is unbeatable, thanks to the Minimax algorithm. This algorithm recursively evaluates all possible moves and outcomes to determine the best move for the AI player. The algorithm works by assigning a score to each possible move, and choosing the move with the highest score. With this implementation, the AI player will always either win or tie the game, but never lose.

# Easy mode
If you want to play against an easier opponent, you can choose to play against the AI player in easy mode to do this change the level to 0 instead of 1. In this mode, the AI player makes random moves instead of using the Minimax algorithm.

# PVP mode
In addition to playing against the AI player, you can also play against another human player in PVP mode. To start a new game in multiplayer mode, Simply change the gamemode to 'pvp' instead of 'ai'

# Future improvements
There are several possible improvements to this game that I'm considering, such as:

Adding support for online multiplayer, so that players can play against each other over the internet.
Adding more advanced AI algorithms, such as Monte Carlo Tree Search or Alpha-Beta pruning.
Adding sound effects and animations to make the game more engaging.


Thank you for checking out my project! If you have any questions or feedback, feel free to reach out to me.