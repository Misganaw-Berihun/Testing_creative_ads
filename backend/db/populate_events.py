import os
import json
from postgres_connect import create_database_engine
from sqlalchemy.orm import sessionmaker
from  tables import Event, Base

def populate_events(session, events_data):
    for event in events_data:
        new_event = Event(action_type=event['action_type'], event_type=event['event_type'])
        session.add(new_event)
    session.commit()

if __name__ == "__main__":
    engine = create_database_engine()
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    with open('json/events.json') as events_file:
        events_data = json.load(events_file)
        populate_events(session, events_data)

    print('Events data successfully populated in the database.')
