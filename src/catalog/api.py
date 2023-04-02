from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get():
    return "Under construction"


@app.get("/games/{game_id}")
def fetch_game(game_id):
    return f"Game id: {game_id}"
