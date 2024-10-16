from pydantic import BaseModel,model_validator,field_validator,Field
from datetime import datetime
from db import Config,Film
from sqlalchemy import select


Session=Config.SESSION


class CreateFilm(BaseModel):
    name:str = Field(max_length=100)
    director:str
    release_year:datetime
    rating_imbd:float = Field(gt=0,le=10)

    @model_validator(mode="after")
    def check_year(self):
        if self.release_year > datetime.now():
            raise ValueError("Release year cannot be in future")
        with Session.begin() as session:
            film = session.scalar(select(Film).where(Film.name==self.name))
            if film:
                raise ValueError("Film with this name already exists") 
        return self