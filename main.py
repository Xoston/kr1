from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from models import User, Feedback
from typing import List
app = FastAPI(title="Kr")
feedback_storage: List[Feedback] = []
@app.get("/")
async def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}
@app.get("/html", response_class=HTMLResponse)
async def get_html():
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)
@app.get("/page", response_class=HTMLResponse)
async def get_page():
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Пример простой страницы html</title>
    </head>
    <body>
        Я ОБОЖАЮ ВСТАВАТЬ К ПЕРВОЙ ПАРЕ :)
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
@app.get("/users", response_model=User)
async def get_user():
    user = User(name="Александр Поскряков", id=1)
    return user
@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    feedback_storage.append(feedback)
    return {
        "message": f"Feedback received. Thank you, {feedback.name}.",
        "total_feedbacks": len(feedback_storage)
    }
@app.get("/feedback", response_model=List[Feedback])
async def get_all_feedback():
    return feedback_storage
@app.get("/test-reload")
async def test_reload():
    return {"message": "Авторелоад действительно работает"}