import os, sys
import json

from sqlalchemy.orm import Session
from . import models
from .schemas import GameResponse, AdUnitCreate
from fastapi import UploadFile

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from scripts.create_adunit import add_ad_unit

def get_adunits(db: Session):
    return db.query(models.Game).all()

def get_events(db: Session):
    return db.query(models.Event).all()

def get_adunit_by_game_key(db: Session, game_key: str):
    return db.query(models.Game).filter(models.Game.game_key == game_key).first()

def create_adunit(db: Session, adunit: AdUnitCreate):
    add_ad_unit(db, adunit)
    db.commit()
    return get_adunit_by_game_key(db, adunit.game_key)

def delete_adunit(db: Session, game_key: str):
    adunit = db.query(models.Game).filter(models.Game.game_key == game_key).first()
    redirect_urls = db.query(models.RedirectURLs).filter(models.RedirectURLs.game_key == game_key).first()
    third_party_engagement = db.query(models.ThirdPartyEngagement).filter(models.ThirdPartyEngagement.game_key == game_key).first()
    tdd_metadata_data = db.query(models.TTDMetadata).filter(models.TTDMetadata.game_key == game_key).first()

    if redirect_urls:
        db.delete(redirect_urls)

    if third_party_engagement:
        db.delete(third_party_engagement)

    if tdd_metadata_data:
        db.delete(tdd_metadata_data)
    
    if adunit:
        db.delete(adunit)
    
    db.commit()

    return adunit

async def create_adunit_from_json(db: Session, json_file: UploadFile):
    try:
        contents = await json_file.read()

        data = json.loads(contents)

        adunit = AdUnitCreate(**data)

        return create_adunit(db, adunit)
    except Exception as e:
        return {"error": str(e)}