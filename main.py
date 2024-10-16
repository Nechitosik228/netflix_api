from db import migrate
from app import app
import uvicorn


if __name__ == "__main__":
    migrate()
    uvicorn.run(app,host="localhost",port=8080)