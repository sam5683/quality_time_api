from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException


app = FastAPI() 
# Make QuizQuestion class so we can inheritie propertys from BaseModel
class QuizQuestion(BaseModel):
    question: str
    options: list[str]
    answer: str
    

# Empty list to store quiz questions  
quiz_questions = []

@app.post("/quiz/add")
def add_quiz_question(q: QuizQuestion):
    quiz_questions.append(q)
    return {"message": "Quiz question added successfully"}

@app.get("/quiz/all")
def get_all_quiz():
    return quiz_questions

import random

@app.get("/quiz/random")
def get_random_quiz():
    if not quiz_questions:
        return {"message": "No quiz questions found"}
    return random.choice(quiz_questions)

@app.delete("/quiz/delete/{index}")
def delete_quiz(index: int):
    if index < 0 or index >= len(quiz_questions):
        return {"error": "Invalid index"}
    quiz_questions.pop(index)
    return {"message": "Deleted successfully", "remaining": len(quiz_questions)}


@app.put("/quiz/update/{index}")
def update_quiz_question(index:int, q:QuizQuestion):
    if index <0 or index >= len(quiz_questions):
        raise HTTPException(status_code = 404, detail = "invalid index")
    else:
        quiz_questions[index] = q
        return {"message": "Quiz question updated successfully", "index": index}
