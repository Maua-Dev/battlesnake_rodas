from fastapi import FastAPI
from mangum import Mangum
from .entities.snake import Snake
from .entities.game_board import GameBoard

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
    print("Start")
    print(request)

    GameBoard = GameBoard.from_json(request["GameBoard"])
    winner_snake = Snake.from_json(request["you"])

    return


@app.post("/move")
def move(request: dict):

    GameBoard = GameBoard.from_json(request["GameBoard"])
    winner_snake = Snake.from_json(request["you"])

    move = GameBoard.where_to_go(winner_snake)

    move = GameBoard.dodge_snake_body(winner_snake, move)

    response = {
        "move": move,
        "shout": Snake.random_shout()
    }

    return response

@app.post("/end")
def end_battle(request: dict):
    return

handler = Mangum(app, lifespan="off")
