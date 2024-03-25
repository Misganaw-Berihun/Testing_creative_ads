from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware

from scripts.event_extractor import extract_events

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

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
    unmatched_events = [event for event in user_events if event not in events_set]

    return {"matched_events": matched_events, "unmatched_events": unmatched_events}