from sqlalchemy import select
from db import Config,Film
from ..schemas import CreateFilm
from . import app


Session=Config.SESSION


@app.get("/films")
def all_films():
    with Session() as session:
        films=session.scalars(select(Film)).all()
        return films
    
    
@app.post("/films")
def create_film(data:CreateFilm):
    with Session.begin() as session:
        film= Film(**data.model_dump())
        session.add(film)
        return "Successfully created"
    

@app.get("/film/{id}")
def one_film(id:int):
    with Session() as session:
        film = session.scalar(select(Film).where(Film.id==id))
        if film:
            return film
        else:
            return "Film with this id doesn't exist"
    

@app.delete("/film/{id}")
def del_film(id:int):
    with Session.begin() as session:
        film = session.scalar(select(Film).where(Film.id==id))
        if film:
            session.delete(film)
            return film
        else:
            return "Film with this id doesn't exist"