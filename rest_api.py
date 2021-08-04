from fastapi import FastAPI
from quiz_gen import make_quiz
from pydantic import BaseModel

app = FastAPI()


class TextInput(BaseModel):
    text: str


@app.post("/")
def return_quiz(text: TextInput):
    return make_quiz(text.text)
