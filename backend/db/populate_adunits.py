import os, sys
import json
from sqlalchemy.orm import sessionmaker

from tables import Game, RedirectURLs, ThirdPartyEngagement, TTDMetadata, Base

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from scripts.add_adunit import add_ad_unit
from postgres_connect import create_database_engine

def populate_ad_units(session, ad_units_data):
    for ad_unit in ad_units_data:
        add_ad_unit(session, ad_unit)
        
    session.commit()

if __name__ == "__main__":
    engine = create_database_engine()
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    with open('json/ad_units.json') as ad_units_file:
        ad_units_data = json.load(ad_units_file)
        populate_ad_units(session, ad_units_data)

    print('Ad units data successfully populated in the database.')
