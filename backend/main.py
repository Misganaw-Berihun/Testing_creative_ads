import os
from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from app import crud, models, schemas
from scripts.event_extractor import extract_events

load_dotenv(override=True)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Adjust to match the origin of your frontend application
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/adunits", response_model=list[schemas.GameResponse])
def read_adunits(db: Session = Depends(get_db)):
    adunits = crud.get_adunits(db)
    return adunits

@app.get("/api/events", response_model=list[schemas.Event])
def read_events(db: Session = Depends(get_db)):
    events = crud.get_events(db)
    return events

@app.get("/api/adunits/{game_id}/{game_version}", response_model=schemas.GameResponse)
def read_adunit(game_id: str, game_version:str, db: Session = Depends(get_db)):
    game_key = f"{game_id}/{game_version}"
    adunit = crud.get_adunit_by_game_key(db, game_key)
    if adunit is None:
        raise HTTPException(status_code=404, detail="Ad unit not found")
    return adunit

@app.post("/api/upload_json")
async def upload_json_file(json_file: UploadFile = File(...), db: Session = Depends(get_db)):
    return await crud.create_adunit_from_json(db, json_file)

@app.post("/api/adunits")
async def create_adunit(adunit: schemas.AdUnitCreate, db: Session = Depends(get_db)):
    return crud.create_adunit(db, adunit)
    

@app.delete("/api/adunits/{game_id}/{game_version}", response_model=schemas.GameResponse)
async def delete_adunit(game_id: str, game_version: str, db: Session = Depends(get_db)):
    game_key = f"{game_id}/{game_version}"
    adunit = crud.get_adunit_by_game_key(db, game_key)
    print("ADD unit:", adunit)
    if adunit is None:
        raise HTTPException(status_code=404, detail="Adunit not found")
    return crud.delete_adunit(db, game_key)


@app.post("/api/compare_events")
async def compare_events(user_events: List[str], region: str, game_key: str):
    try:
        print(user_events, region, game_key)
        url = f"https://s3.{region}.amazonaws.com/a.futureadlabs.com/games/{game_key}/game.js";
        events_set = extract_events(url)
        print("Events:", events_set)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to extract events from {url}: {str(e)}")

    matched_events = [event for event in user_events if event in events_set]

    return {"matched_events": matched_events}