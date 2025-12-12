from datetime import datetime
from random import randint
from fastapi import FastAPI, HTTPException, Response
from typing import Any
from fastapi import Request

app = FastAPI(root_path="/api/v1")

@app.get("/")
async def root():
    return {"message": "Hello world!"}

data : Any = [
    {
        "artist_id": 1,
        "date_added": datetime.now(),
        "name": "Hail The Sun",
        "rating": 10
    },
    {
        "artist_id": 2,
        "date_added": datetime.now(),
        "name": "Dance Gavin Dance",
        "rating": 9
    },
    {
        "artist_id": 3,
        "date_added": datetime.now(),
        "name": "Rings of Saturn",
        "rating": 9
    },
    {
        "artist_id": 4,
        "date_added": datetime.now(),
        "name": "Sianvar",
        "rating": 8.5
    }
]

"""
Artists
- artist_id
- date_added
- name
- rating

Songs
- name
- length
- genre
- rating
- date Added

"""
@app.get("/artists")
async def read_artists():
    return {"Artists": data}

@app.get("/artists/{id}")
async def read_artist(id: int):
    for artist in data:
        if artist.get("artist_id") == id:
            return {"artist": artist}
    raise HTTPException(status_code = 404)

@app.post("/artists")
async def creat_campaign(body: dict[str, Any]):
    new : Any = {
            "artist_id": randint(100, 1000),
            "date_added": datetime.now(),
            "name": body.get("name"),
            "rating": body.get("rating")
    }
    data.append(new)
    return {"artist": new}

@app.put("/artists/{id}", status_code=201)
async def update_artist(body: dict[str,Any], id: int):
    for index, artist in enumerate(data):
        if artist.get("artist_id") == id:
            updated : Any = {
                "artist_id": id,
                "date_added": artist.get("date_added"),
                "name": artist.get("name"),
                "rating": body.get("rating")
            }
    
            data[index] = updated
            return {"artist": updated}
    raise HTTPException(status_code=404)

@app.delete("/artists/{id}")
async def delete_artist(id: int):
    for index, artist in enumerate(data):
        if artist.get("artist_id") == id:
            data.pop(index)
            return Response(status_code=204)
    raise HTTPException(status_code=404)