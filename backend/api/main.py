# Rest API to interact with Database and Cache

import services.database as db_api
import services.cache as cache_api

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel


app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False, # Set to True if your frontend needs to send cookies or authorization headers
    allow_methods=["*"],     # Or specify specific methods like ["GET", "POST"]
    allow_headers=["*"],     # Or specify specific headers
)


# class Phrase(BaseModel):
#     content: str


# Routes
@app.get("/api/get-current-phrase")
def get_current_phase():
    current_phrase = cache_api.get_current_phrase()
    if current_phrase is None:
        change_current_phrase()
        return get_current_phase()
    return {"current_phrase":current_phrase}


@app.get("/api/change-current-phrase")
def change_current_phrase():
    new_phrase = db_api.get_random_phrase()
    cache_api.set_current_phrase(new_phrase)
    return {"current_new_phrase":new_phrase}
