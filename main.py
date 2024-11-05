from db import migrate
from app import app,film_router
import uvicorn


if __name__ == "__main__":
    migrate()
    app.include_router(film_router)
    uvicorn.run(app,host="localhost",port=8080)