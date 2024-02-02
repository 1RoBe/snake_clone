# Retro Snake
#### Video Demo:  <URL HERE>

#### Abstract
Retro Snake is based on the game 'Snake' which came presintalled on every Nokia model 6110 in 1998. It features a starting menu, 
the main game which can be paused at any time and a game over screen. The goal is to collect as many 'black squares' as possible without 
colliding with the black border or your own body while the movement of the snake is tile based.

#### Installation
The only requirement for this program is pygame. The required version can be installed via:
```
pip install -r requirements.txt
```

#### Description:
The pygame module was used to obtain a graphical output as well as handle keyboard since it has a big community, thorough documentation and is ideal for simple 
2D games.<br>
The project is composed of five files: `game.py`, `game_world.py`, `scoreboard.py`, `snake.py` and `fruit.py`, each containing a class to achieve sepeartion of concerns and to not repeat certain constants, like `SCREEN_WIDTH`. <br>
<!-- The `snake.py` file contains the `Snake` class which uses attributes and methods of the `Game` class, `game.screen` to render drawings to the display and of the `Game_world` class, which defines the dimensions of the playing field as well as the borders in which the snake can move.
The movement of the snake is tile based making the determination of wall and fruit collisions very easy. The snake is composed of a list named `body` and each entry is a list containing the x and y position in tile coordinates composing each segment of the snake.<br>
The movement of the snake is implemented in the `update` method, which receives the direction of the next movement via user input from the `Game` class. If `can_move` attribute turns true periodically through a timed event in the `Game` class the `update` method rejects movements which is opposite to the movement direction, e.g. north-south, east-west, and checks if the snake would collide with the wall or a segment of its body. Instead of moving to a tile position and then checking if that position is outside the playing field boundray the check happens before the movement, that way the snake stop infront of the barriers, which is visually more pleasing. The snake is drawn using `pygame.draw.rect()` function, depending on the orientation of the "head", `self.body[0]`, a different pair of eyes is drawn. The body is drawn by the same method but the longer it gets the darker the squares get. The reset method puts the snake back into its original position after the game over condition is fullfilled. -->
The `snake.py` file contains the `Snake` class, which utilizes attributes and methods from the `Game` and `Game_world` classes. Specifically, it uses `game.screen` to render drawings to the display and `Game_world` to define the dimensions of the playing field and the borders within which the snake can move.<br>
The snake's movement is tile-based, making it easy to determine collisions with the borders and the fruit object. The snake is made up of a list called 'body', with each entry being a list that contains the x and y positions in tile coordinates for each segment of the snake.
The snake's movement is implemented in the 'update' method, which receives the direction of the next movement via user input from the 'Game' class. If the `can_move` attribute becomes true during a timed event in the `Game` class, the `update` method will reject movements that are in the opposite direction, such as north-south or east-west, and check if the snake would collide with the wall or a segment of its body. The check for whether the snake is moving outside the playing field boundary now occurs before the snake moves to a tile position. This results in the snake stopping in front of the barriers, which is visually more pleasing.<br>
The snake's eyes are drawn using `pygame.draw.rect` function, and the orientation of the head, `self.body[0]`, determines which pair of eyes is drawn. The body is also drawn using the same method, with the squares getting darker as the body gets longer. The reset method returns the snake to its original position after the game over condition is met.<br>
<br>
The `fruit.py` file contains the `Fruit` class, which implements the fruit object. It requires attributes of the `Game` class to render to the screen and from the `Game_world` class to position the fruit inside the playing field and not outside of it. The fruit itself is a minimal design made up of a black rectangle which is slightly smaller than the tile-size.<br>
The class possesses two methods: The `update` method picks a random position in tile coordinates inside of the playing field and converts the tile coordinates to pixel coordinates to create the `pygame.Rect` object. 
The `draw` method then renders this object to the screen. The class lacks the `reset()` methods since the `update` method <br>
<br>
The `game_world.py` file defines the parameters of the playing field, e.g. it's width and height as well as the borders and the margin between screen and playingfield. It also creates the `snake` and `fruit` objects with those parameters to check for border collision and the placement of the fruit. Using the `Game_world` class to define those constants avoid redundancy, a potential update for a later time could include a config file, which defines all those constants in a single place, which would allow modifying those constants without opening the code.<br>
The `draw` method draws the 4 borders to the screen as rectangles via the `pygame.draw.rect` method.<br>
<br>
The `scoreboard.py` file includes the `Scoreboard` class which is used to display the scores and to handle saving and loading the highscore to a file.





If the attribute `can_move` of the snake class is set to true, which is done by a timed userevent in the `Game` class, then 



`game.py` defines `SCREEN_WIDTH` and `SCREEN_HEIGHT` and initializes
pygame. The class also intitializes an instance of the `Scoreboard` and `Game_world` class, to use certain attributes and methods of the `Game` class like the screen dimension, or the `draw_text` method to avoid redundancy. The possible actions a user can do are definded in two dictionaries, `directions_tile_coordinates` and `actions` for easy readibility and in case one wants to add another actions at a later time. The movement of the snake 
Since the game features menus I used the concept of game states. For a this I took inspiration from the implementation of https://github.com/ChristianD37/YoutubeTutorials/blob/master/Game%20States/game.py. To implement it I used multiple loops. The first loop is active as long as the game itself is running, e.g. the user doesn't close the game window
and runs the `game_start()`, `game_loop()` and `game_over()` methods. 

<!-- 
```
int main(void) 
{
    code goes here;
}
```
THen we talk about shit -->
