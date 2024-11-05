from fastapi import FastAPI


app=FastAPI()

from . import films
from .films import film_router