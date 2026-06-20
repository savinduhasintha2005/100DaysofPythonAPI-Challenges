from fastapi import FastAPI
import random

app = FastAPI()

secret_number = random.randint(1, 100)
attempts = 0


@app.get("/")
def home():
    return {
        "message": "Welcome to Number Guess API"
    }


@app.get("/guess")
def guess(number: int):
    global attempts

    attempts += 1

    if number < secret_number:
        return {
            "result": "Too low",
            "attempts": attempts
        }

    elif number > secret_number:
        return {
            "result": "Too high",
            "attempts": attempts
        }

    return {
        "result": "Correct!",
        "attempts": attempts
    }


@app.post("/reset")
def reset_game():
    global secret_number
    global attempts

    secret_number = random.randint(1, 100)
    attempts = 0

    return {
        "message": "New game started"
    }