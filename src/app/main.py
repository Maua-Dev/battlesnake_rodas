from fastapi import FastAPI
from mangum import Mangum
from .entities.snake import Snake
from .entities.board import Board

app = FastAPI()

@app.get("/")
def read_root():
    response = {
        "apiversion": "1",
        "author": "Rodas",
        "color": "#40E0D0",
        "head": "tiger-king",
        "tail": "nr-booster",
        "version": "1.0.0"
        }
    return response


@app.post("/start")
def start_battle(request: dict):

    print(request)

    board = Board.from_json(request["board"])
    winner_snake = Snake.from_json(request["you"])

    return


@app.post("/move")
def move(request: dict):

    board = Board.from_json(request["board"])
    winner_snake = Snake.from_json(request["you"])
    move = Board.next_position(winner_snake)
    move = Board.dodge_snake_body(winner_snake, move)

    response = {
        "move": move
    }

    return response

@app.post("/end")
def end_battle(request: dict):
    return

handler = Mangum(app, lifespan="off")
