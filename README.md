# TTT-Python | This is a follow along with the video "Python for absolute beginners 2019 - TIC TAC TOE project (+Special Appearance!)"
Which can be found here: https://youtu.be/BHh654_7Cmw

A brief explanation: 

As the game starts a blank board is displayed using "-"s as empy spaces and prompts the user that it's X's turn and to "Choose a number between 1-9:" here the user does so and after some basic input verification that insures that spot they selected isn't taken and the input is valid an X is placed in the given position. It replaces the "-" character since the board is simply a list of characters. The new board is then printed and another prompt for O to select a spot is printed.

After each turn the program will check each row, column, and diagnol to see if there is a winner. After we will check if there are any more blank spaces on the board if there are none the game is a tie. If niether is the case we will switch the current player in this case from X to O. The process repeats until there is a win or a tie in which a trigger will be set off that gets the program out of the while loop that keeps the game going. 

The resulting outcome is printed to the screen and the program is terminated. 
