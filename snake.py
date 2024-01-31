import pygame

class Snake:
    def __init__(self, game, game_world):
        """Class that updates snake position, checks collisions, grows the snake and draws the snake

        Class that creates Snake objects. It updates the snake position in case it may move in the current frame,
        checks if the snake will collide with the game_world borders or itself in the current frame and draws 
        the snake object to the screen.

        Attributes:
            game: Game object for screen object and screen dimensions
            game_world: Game_world object for field dimension and tilesize
            can_move: bool that indicates if snake may move in the current frame
            tile_position_last_segment: list[int] that indicates the last x and y tile position of snake body
            direction: list[int] that indicates the initial direction in tile coordinates
            tile_position_start: list[int]
            WIDTH: int that defines the width of the snake segments rectangle
            HEIGHT: int that defines the height of the snake segments rectangle
            color: dict that defines the colors used in this class
            body: list[list[int]] that describes the tile positions of the snake segments
        """
        # imports from game and game_world classes
        self.game = game
        self.game_world = game_world

        # check if snake can move in that frame
        self.can_move = False

        # position in tile coords
        self.tile_position_last_segment: list[int] = []

        # direction
        self.direction: list[int] = [1, 0]
        self.tile_position_start: list[int] = [4, 7]

        # design of drawing
        self.WIDTH: int = self.game_world.TILE_SIZE
        self.HEIGHT: int = self.game_world.TILE_SIZE
        # self.color: tuple[int, int, int] = (255, 255, 255)
        self.color: dict = {"WHITE": (255, 255, 255), "BLACK": (0, 0, 0)}

        # create list of all snake segments and append head
        self.body = [self.tile_position_start]

        # start with 2 segments + head
        for index in range(1, 3):
            self.body.append(
                [self.tile_position_start[0] - index, self.tile_position_start[1]]
            )

    def update(self, direction: list[int]) -> None:
        """method that in case of collision sets self.game.playing false otherwise updates tile position of snake
        
        Args:
        direction: list[int] that describes the direction determined by user input for each frame
        """
        if self.can_move:
            if [a + b for a, b in zip(self.direction, direction)] != [0, 0]:
                self.direction = direction
            if self.collision_wall() or self.collision_body():
                self.game.playing = False
            else:
                self.update_tile_position()
            self.can_move = False

    def update_tile_position(self) -> None:
        """method that updates the tile positions given a specific direction"""
        self.tile_position_last_segment = self.body[-1][:]

        # save old positions
        old_tile_positions = self.body[:]

        # update position of head of snake
        self.body[0] = [pos1 + pos2 for pos1, pos2 in zip(self.body[0], self.direction)]

        # update body of snake
        for index in range(len(self.body) - 1):
            self.body[index + 1] = old_tile_positions[index]

    def collision_wall(self) -> bool:
        """method for detecting collisions with the game world boundaries

        Returns:
            bool: true if snake will coolide with wall in the current frame, else false
        """
        if (
            self.body[0][0] + self.direction[0] < self.game_world.TILE_DIMENSION[0][0]
            or self.body[0][0] + self.direction[0] > self.game_world.TILE_DIMENSION[0][1]
            or self.body[0][1] + self.direction[1] < self.game_world.TILE_DIMENSION[1][0]
            or self.body[0][1] + self.direction[1] > self.game_world.TILE_DIMENSION[1][1]
        ):
            return True
        return False

    def collision_body(self) -> bool:
        """method for detecting collisions with items of snake.body

        Returns:
            bool: true if snake will collide with itself in current frame, else false
        """
        for tile_position in self.body[1:]:
            if [
                pos1 + pos2 for pos1, pos2 in zip(self.body[0], self.direction)
            ] == tile_position:
                return True
        return False

    def grow(self) -> list[int]:
        """method for determinating the tile coordinates of the new self.body segment

        Returns:
            list[int]: tile coordinates of the new self.body semgent of the snake object
        """
        self.body.append(self.tile_position_last_segment)

    def tile_to_pixel_coordinates(self, tile_x: int, tile_y: int) -> list[int]:
        position_x: int = (
            tile_x * self.game_world.TILE_SIZE + self.game_world.FIELD_DIMENSION[0][0]
        )
        position_y: int = (
            tile_y * self.game_world.TILE_SIZE + self.game_world.FIELD_DIMENSION[1][0]
        )
        return [position_x, position_y]

    def draw(self) -> None:
        """method for execution head and body draw functions"""
        self.draw_body()
        self.draw_face()

    def draw_face(self) -> None:
        """method for drawing the face of the snake by drawing to black rectangles for its eyes"""
        pixel_position: list[int] = self.tile_to_pixel_coordinates(
            self.body[0][0], self.body[0][1]
        )
        position_x = pixel_position[0]
        position_y = pixel_position[1]

        match self.direction:
            case [0, -1]:
                design_eye_1 = pygame.Rect(
                    position_x + 8, position_y + 32 - 18 - 4, 4, 4
                )
                design_eye_2 = pygame.Rect(
                    position_x + 32 - 8 - 4, position_y + 32 - 18 - 4, 4, 4
                )
                pygame.draw.rect(self.game.screen, self.color["BLACK"], design_eye_1)
                pygame.draw.rect(self.game.screen, self.color["BLACK"], design_eye_2)

            case [1, 0]:
                design_eye_1 = pygame.Rect(position_x + 18, position_y + 8, 4, 4)
                design_eye_2 = pygame.Rect(
                    position_x + 18, position_y + 32 - 8 - 4, 4, 4
                )
                pygame.draw.rect(self.game.screen, self.color["BLACK"], design_eye_1)
                pygame.draw.rect(self.game.screen, self.color["BLACK"], design_eye_2)

            case [0, 1]:
                design_eye_1 = pygame.Rect(position_x + 8, position_y + 18, 4, 4)
                design_eye_2 = pygame.Rect(
                    position_x + +32 - 8 - 4, position_y + 18, 4, 4
                )
                pygame.draw.rect(self.game.screen, self.color["BLACK"], design_eye_1)
                pygame.draw.rect(self.game.screen, self.color["BLACK"], design_eye_2)

            case [-1, 0]:
                design_eye_1 = pygame.Rect(position_x + 10, position_y + 8, 4, 4)
                design_eye_2 = pygame.Rect(
                    position_x + 10, position_y + 32 - 8 - 4, 4, 4
                )
                pygame.draw.rect(self.game.screen, self.color["BLACK"], design_eye_1)
                pygame.draw.rect(self.game.screen, self.color["BLACK"], design_eye_2)

    def draw_body(self) -> None:
        """method for drawing all tile positions of self.body"""
        for index, tile_position in enumerate(self.body):
            pixel_position = self.tile_to_pixel_coordinates(
                tile_position[0], tile_position[1]
            )
            position_x = pixel_position[0]
            position_y = pixel_position[1]
            design = pygame.Rect(position_x, position_y, self.WIDTH, self.HEIGHT)
            # pygame.draw.rect(self.game.screen, self.color['WHITE'], design)
            pygame.draw.rect(
                self.game.screen,
                [max(255 - 5 * index, 0), max(255 - 5 * index, 0), max(255 - 5 * index, 0)],
                design,
            )
            
    def reset(self):
        """method to reset self.direction and self.body to initial state after game_over state"""
        self.direction = [1, 0]
        self.body = [self.tile_position_start]
        for index in range(1, 3):
            self.body.append(
                [self.tile_position_start[0] - index, self.tile_position_start[1]]
            )   