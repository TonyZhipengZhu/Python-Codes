Minesweeper

02/12/2019
Written by: Abdul Saboor, Bradley Thomas, Tony Zhu

Highest objective: to create a version of minesweepers with self-generated bombs, interactive graphics, timer, and high score memory.

This program should be run in IDLE.

Rules:

- Enter an integer size for the board. The board will be a square of that size.

- Enter the number of bombs. Typically, standard sizes are 10x10 with 10 bombs, and 16x16 with 40 bombs.

- Begin the game by left-clicking somewhere on the grid. You cannot click right on the first turn of the game.

- Displayed numbers indicate the number of bombs in the immediate 8-square vicinity.

- Right clicking puts a flag down.  Flags appear as green spaces. In order to win the game, all bombs must be flagged, and there can be no unclicked spaces left on the board.

- You cannot put down more flags than the number of bombs you started with.

- When you win the game, the idle window will display that you win and you will have to input a name for the high scores list. The highest score has the lowest time.

- Winning or losing the game will stop the GUI.


Board Class:

The first problem this game faced for coding was that none of the 9 squares including first click and surroundings can be a bomb. To get around this problem, an empty map is generated upon initiation of the board class, using the list of lists method provided in class. When the user clicks the first square, the second problem is encountered: there must be randomly generated maps with no duplicate bomb points. To do this, a while loop is employed to generate 2 random integers within the range of the board size. A dictionary is used to store strings of disallowed points, which initially contains the first clicked point and the surrounding 8.  If an "x,y" pair string is not in the dictionary, the x and y values are added to a list of points, and the "x,y" pair string is added to the dictionary. Using these methods, there can be no duplicate points.  To add the bombs to the map, a while loop scans the list pulling each x and y value out individually and changes the point on the map to a "B" (instead of a ".", which denotes empty space).
	
Next, there needs to be a function to add in the numbers.  This function checks the surrounding 8 points of each point on the map using if statements, and totals the number of surrounding squares containing bombs. This number is then returned through a dictionary as a symbol containing the shift+number symbol (i.e. 1 -> !, 2->@, etc.).  These symbols indicate numbers that exist but the user cannot yet see. When the numbers are revealed, they are run through the opposite dictionary, which converts them back to integers for the GUI to display.

The most important function for the functionality of gameplay is the floodClick function, which automatically opens up all adjacent (up, down, left, and right only) spaces with no bombs, stopping when it hits numbers. To do this it uses recursive statements nested in if statements.  If the square being questioned does not have a bomb, it runs the floodClick function inside of itself and checks the next point.  As new points are detected, the flood click function compiles a list of points (self.floodlist) to send to the GUI to change to open spaces or numbers.

Finally, there are 2 mega functions that control clicks.  When a left click is received, the board.clickCheck function is called. If the board is empty, this generates the map utilizing the addBombs and bombNumber functions. If the space is marked as "B", the function prints "YOU LOSE" and closes the GUI.  If the space is a flagged space, "F" or "P", it does nothing. If the space is a blank space, it empties the floodlist, runs the flood click function, and checks the open spaces on the board. clickCheck's final function is to test for the winning conditions. If the number of points ("P" on the board, and self.points in the class) is equal to the initial number of bombs, and the remaining unclicked spaces (self.opens) is equal to 0, clickCheck runs the youWin function, which prints "YOU WIN!!!!", requests a name for the high score list, and closes the GUI.

When a right click is received, the addFlag function tests a number of conditions to decide whether to add an "F" or a "P", remove an "F" or "P", add points, remove points, add remaining flags, remove remaining flags, and retest a spot for its bomb number using the bomb number function. In addition, if the last empty space in the game is flagged, the you win function is run, and the GUI is closed.



GUI Class:

The main functionality of the GUI class is to display the information of a board instance. It first generates a board with all gray squares that the user can click on. It has two separate functions to respond to left click and right click, which are bound to each square of the board. When the user clicks, the clickCheck function will be activated and determine the status of the game. Another important component is the seeSpace function. The seeSpace function takes information from the board instance every time the user clicks and labels the open spaces to the originally gray squares. We used to scan the whole 2D array every time the user clicks and label them accordingly. However, the “scanning” method was causing the program to be very slow and it would eventually crash. The seeSpace function perfectly solve that problem since it only takes a list of coordinates from the board instance every time the click happens, instead of scanning the whole board.


App Class:  
This class takes care of the timer and the high-score. The high-score module was relatively easy to make, it basically uses ‘shelve’ to create a data file and then store the input in a list. Every time after the first, whenever you run the code, it then opens the same data file so that all the previous data is already there.

The timer was a little more complicated as it had a lot of if, else and elif statements. We used map to setup the seconds and the minutes. Once this was set up, we worked on the graphics.

We wrote the highscore and the timer code separately and we were having some issues integrating them together. Since we made the timer separately, we had to put in a start and a stop button on it but when we had to integrate it into the the larger code for the game we needed to figure out how to remove the start and the stop button and get it to do that as the game starts for the former and when the game end for the latter. Getting rid of the start button was easy as we programmed the timer to start when the program starts running. Removing the stop button was a little harder as when we did it the first time 
 The main issue was to get the program to only save the time for the win and disregard the loss time. We overcame this by incorporating the ‘shelve’ function into the ‘YouWin’ function and if the user loses, the timer self destroys.
 
