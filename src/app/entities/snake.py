from random import randint
from typing import List
from .coordinates import Coordinates


class Snake:
    snake_id: str
    name: str
    health: int
    body: List[Coordinates]
    latency: str
    head: Coordinates
    length: int

    def __init__(self, snake_id: str, name: str, health: int, body: List[Coordinates], latency: str, head: Coordinates, length: int):
        self.snake_id = snake_id
        self.name = name
        self.health = health
        self.body = body
        self.latency = latency
        self.head = head
        self.length = length

    @staticmethod
    def from_json(json):
        snake_id = json["id"]
        name = json["name"]
        health = json["health"]
        body = [Coordinates.from_json(body) for body in json["body"]]
        latency = json["latency"]
        head = Coordinates.from_json(json["head"])
        length = json["length"]
        return Snake(snake_id, name, health, body, latency, head, length)
    
    def is_inside_snake(self, coordinate: Coordinates):
        for body in self.body:
            if body == coordinate:
                return True
        return False
    
    def is_near_head(self, coordinate: Coordinates):
        if Coordinates.distance(self.head, coordinate) <= 1:
            return True
        return False
    
    def __eq__(self, other):
        return self.snake_id == other.snake_id and self.name == other.name and self.health == other.health and self.body == other.body and self.latency == other.latency and self.head == other.head and self.length == other.length

    def __repr__(self):
        return f"Snake: {self.name} ({self.snake_id})"