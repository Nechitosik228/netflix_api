from sqlalchemy import select
from db import Config,Film
from ..schemas import CreateFilm
from fastapi import APIRouter


Session=Config.SESSION

film_router=APIRouter(prefix="/films", tags=["Film"])


@film_router.get("/all",summary="See all films")
def all_films():
    """
    See all films
    """
    with Session() as session:
        films=session.scalars(select(Film)).all()
        return films
    
    
@film_router.post("/create",summary="Create a film")
def create_film(data:CreateFilm):
    """
    Create a film with all the information:

    - **name**: each film must have a name
    - **director**: each film should have a director
    - **release year**: every film has a release year but it shouldn't be in future
    - **rating imbd**: every film has a rating and it should be greater than 0 and less than 10
    """
    with Session.begin() as session:
        film= Film(**data.model_dump())
        session.add(film)
        return "Successfully created"
    

@film_router.get("/{id}",summary="See one specific film")
def one_film(id:int):
    """
    See more details about specific film:

    - **id**: you should enter id of the film
    
    """
    with Session() as session:
        film = session.scalar(select(Film).where(Film.id==id))
        if film:
            return film
        else:
            return "Film with this id doesn't exist"
    

@film_router.delete("/{id}",summary="Delete a film")
def del_film(id:int):
    """
    Delete a film:

    - **id**: you should enter id of the film
    
    """
    with Session.begin() as session:
        film = session.scalar(select(Film).where(Film.id==id))
        if film:
            session.delete(film)
            return film
        else:
            return "Film with this id doesn't exist"