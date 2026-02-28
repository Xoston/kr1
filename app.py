from fastapi import FastAPI
my_awesome_app = FastAPI()
@my_awesome_app.get("/")
async def root():
    return {"message": "Авторелоад работает"}