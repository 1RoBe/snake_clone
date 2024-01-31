# Retro Snake
#### Video Demo:  <URL HERE>
#### Abstract
Retro Snake is based on the game 'Snake' which came presintalled on every Nokia model 6110 in 1998. It features a starting menu, 
the main game which can be paused at any time and a game over screen. The goal is to collect as many 'black squares' as possible without 
colliding with the black border or your own body while the movement of the snake is tile based. 
#### Description:
The pygame module was used to obtain a graphical output as well as handle keyboard since it has a big community, thorough documentation and is ideal for simple 
2D games.
The project is composed of five files: `game.py`, `game_world.py`, `scoreboard.py`, `snake.py` and `fruit.py`, each containing a class to achieve sepeartion of concerns and to not repeat certain constants, like `SCREEN_WIDTH`. 
<br>
<br>
The `snake.py` file contains the `Snake` class which uses attributes and methods of the `Game` class, `game.screen` to render drawings to the display and of the `Game_world` class, which defines the dimensions of the playing field as well as the borders in which the snake can move.
The movement of the snake is tile based making the determination of wall and fruit collisions very easy. The snake is composed of a list named `body` and each entry is a list containing the x and y position in tile coordinates composing each segment of the snake.<br>
The movement of the snake is implemented in the `update` method, which receives the direction of the next movement via user input from the `Game` class. If `can_move` attribute turns true periodically through a timed event in the `Game` class the `update` method rejects movements which is opposite to the movement direction, e.g. north-south, east-west, and checks if the snake would collide with the wall or a segment of its body. Instead of moving to a tile position and then checking if that position is outside the playing field boundray the check happens before the movement, that way the snake stop infront of the barriers, which is visually more pleasing. The snake is drawn using `pygame.draw.rect()` function, depending on the orientation of the "head", `self.body[0]`, a different pair of eyes is drawn. The body is drawn by the same method but the longer it gets the darker the squares get. The reset method puts the snake back into its original position after the game over condition is fullfilled.


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
