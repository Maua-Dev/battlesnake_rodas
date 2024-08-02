from typing import List, Optional, Tuple
from .snake import Snake
from .coordinates import Coordinates


class GameBoard:
    height: int
    width: int
    food: List[Coordinates]
    snakes: List[Coordinates]
    hazards: List[Snake]

    def __init__(self, height: int, width: int, food: List[Coordinates], snakes: List[Coordinates], hazards: List[Snake]):
        self.food = food
        self.height = height
        self.width = width
        self.snakes = snakes
        self.hazards = hazards

    @staticmethod
    def from_json(json):
        height = json["height"]
        width = json["width"]
        food = [Coordinates.from_json(food) for food in json["food"]]
        snakes = [Snake.from_json(snake) for snake in json["snakes"]]
        hazards = [Coordinates.from_json(hazard) for hazard in json["hazards"]]
        return GameBoard(height, width, food, snakes, hazards)

    @staticmethod
    def navigate(start: Coordinates, end: Coordinates) -> str:
        if start.x < end.x:
            return "right"
        elif start.x > end.x:
            return "left"
        elif start.y < end.y:
            return "up"
        elif start.y > end.y:
            return "down"
        else:
            return "up"
        
    def next_position(self, me: Snake) -> str:
            
        near_snake, move = self.get_near_snake_head(me)
           
        if len(self.food) > 0 and near_snake is None:
            move = self.navigate(me.head, self.get_food(me))
        elif near_snake is not None:
            move = self.navigate(me.head, near_snake.head)
        else:
            move = self.navigate(me.head, me.body[0])
        
        return move

    def get_food(self, snake: Snake):
        food = self.food[0]
        for food in self.food:
            if Coordinates.distance(snake.head, food) < Coordinates.distance(snake.head, food):
                food = food
        return food
    
    def is_snake(self, move: str, head: Coordinates):
        Coordinates = head.move_command(move)
        for snake in self.snakes:
            if snake.is_inside_snake(Coordinates):
                return snake
        return False
    
    def is_hazard(self, move: str, head: Coordinates):
        Coordinates = head.move_command(move)
        for hazard in self.hazards:
            if hazard == Coordinates:
                return True
        return False

    def dodge_snake_body(self, me: Snake, old_move: str):
        if  self.can_move(old_move, me):
            return old_move

        for move in ["up", "down", "left", "right"]:
            if self.can_move(move, me):
                return move
        return old_move
    
    def is_out_of_bounds(self, move: str, head: Coordinates):
        Coordinates = head.move_command(move)
        if Coordinates.x < 0 or Coordinates.x >= self.width or Coordinates.y < 0 or Coordinates.y >= self.height:
            return True
        return False
    
    def can_move(self, move: str, me: Snake):
        head = me.head
        snake, move_returned = self.get_near_snake_head(me, move)

        if not self.is_out_of_bounds(move, head) and not self.is_snake(move, head) and not self.is_hazard(move, head) and not (snake is not None and snake.length >= me.length):
            return True
        return False

    def is_near_snake_head(self, move: str, me: Snake):
        snake, move = self.get_near_snake_head(me, move)

        if snake is not None:
            return True
        return False
    
    def get_near_snake_head(self, me: Snake, move: str = None) -> Tuple[Optional[Snake], Optional[str]]:
        if move is not None:
            Coordinates = me.head.move_command(move)
            for snake in self.snakes:
                if snake.is_near_head(Coordinates) and snake.snake_id != me.snake_id:
                    return snake, move
            return None, None
        
        for move in ["up", "down", "left", "right"]:
            Coordinates = me.head.move_command(move)
            for snake in self.snakes:
                if snake.is_near_head(Coordinates) and snake.snake_id != me.snake_id:
                    return snake, move
        return None, None
    
    def __eq__(self, other):
        return self.height == other.height and self.width == other.width and self.food == other.food and self.snakes == other.snakes and self.hazards == other.hazards
    
    def __repr__(self):
        return f"GameBoard: {self.width}x{self.height}"
        