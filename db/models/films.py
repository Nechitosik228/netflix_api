from . import Config
from sqlalchemy.orm import Mapped,mapped_column
from datetime import datetime


Base=Config.BASE


class Film(Base):
    __tablename__="films"

    
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    director:Mapped[str]
    release_year:Mapped[datetime]
    rating_imbd:Mapped[float]


