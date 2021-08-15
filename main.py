from dotenv import load_dotenv
from sqlalchemy.dialects.postgresql import psycopg2
import logging
import json
from models.weight import FitbitWeight
from models.heart_rate import FitbitHeartRate
from models.steps import FitbitSteps
from models.sleep import FitbitSleep
from models.altitude import FitbitAltitude
from models.spotify import SpotifyStreamingHistory
from models.resting_heart_rate import FitbitRestingHeartRate
from base import Session, Base, engine
import glob

# Load Environment Variables
load_dotenv()

logging.basicConfig(filename='logs/main.log', encoding='utf-8', level=logging.DEBUG)
logging.getLogger('sqlalchemy.dialects.postgresql').setLevel(logging.DEBUG)


def add_all_weights(path):
    Base.metadata.create_all(engine)
    s = Session()
    paths = glob.glob(path)

    files = [open(file, 'r') for file in paths]

    rec_array = [json.load(file) for file in files]
    # I promise this works. Nested List Comprehension "It's a Flatmap" - Cormac
    records = [item for sublist in rec_array for item in sublist]
    print([record.items() for record in records])
    objects = [FitbitWeight(record['logId'], record['weight'], record['bmi'], record.get('fat', None),
                            record['date'], record['time'], record.get('source', None)) for record in records]

    s.bulk_save_objects(objects)
    s.commit()
    # print(objects)
    return


def add_all_heartrates(path):
    Base.metadata.create_all(engine)
    s = Session()
    paths = glob.glob(path)
    print(f"""Paths returned: {len(paths)}""")

    for file in paths:
        f = open(file, 'r')
        records = json.load(f)
        objects = [FitbitHeartRate(record.get('dateTime'), record.get('value').get('bpm'),
                                   record.get('value').get('confidence')) for record in records]
        s.bulk_save_objects(objects)
        s.commit()


def add_all_sleep(path):
    Base.metadata.create_all(engine)
    s = Session()
    paths = glob.glob(path)
    print(f"""Paths returned: {len(paths)}""")

    for file in paths:
        f = open(file, 'r')
        records = json.load(f)
        objects = [FitbitSleep(record.get('logId'), record.get('dateOfSleep'), record.get('startTime'),
                               record.get('endTime'), record.get('duration'), record.get('minutesToFallAsleep'),
                               record.get('minutesAsleep'), record.get('minutesAwake'),
                               record.get('minutesAfterWakeup'), record.get('timeInBed'),
                               record.get('efficiency'), record.get('type'), record.get('infoCode'),
                               record.get('mainSleep')) for record in records]

        for obj in objects:
            s = Session()
            exists = s.query(FitbitSleep).filter_by(logId=obj.logId).first()
            if not exists:
                s.add(obj)
                s.commit()
            else:
                print(f"""Skipping Id {obj.logId} exists, skipping...""")


def add_all_steps(path):
    Base.metadata.create_all(engine)
    s = Session()
    paths = glob.glob(path)
    print(f"""Paths returned: {len(paths)}""")

    for file in paths:
        f = open(file, 'r')
        records = json.load(f)
        objects = [FitbitSteps(record.get('dateTime'), record.get('value')) for record in records]
        s.bulk_save_objects(objects)
        s.commit()


def add_all_resting_heartrates(path):
    Base.metadata.create_all(engine)
    s = Session()
    paths = glob.glob(path)
    print(f"""Paths returned: {len(paths)}""")

    for file in paths:
        f = open(file, 'r')
        records = json.load(f)
        objects = [FitbitRestingHeartRate(record.get('dateTime'), record.get('value').get('value'),
                                          record.get('value').get('error')) for record in records]

        for obj in objects:
            if FitbitRestingHeartRate.valueBpm != 0.0:
                s.add(obj)
                s.commit()
            else:
                print(f"""Skipping Id {obj.dateTime} exists, skipping...""")


def add_all_altitudes(path):
    Base.metadata.create_all(engine)
    s = Session()
    paths = glob.glob(path)
    print(f"""Paths returned: {len(paths)}""")

    for file in paths:
        f = open(file, 'r')
        records = json.load(f)
        objects = [FitbitAltitude(record.get('dateTime'), record.get('value')) for record in records]
        s.bulk_save_objects(objects)
        s.commit()


def add_streaming_history(path):
    Base.metadata.create_all(engine)
    s = Session()
    paths = glob.glob(path)
    print(f"""Paths returned: {len(paths)}""")

    for file in paths:
        f = open(file, 'r')
        records = json.load(f)
        objects = [SpotifyStreamingHistory(record.get('endTime'), record.get('artistName'),
                                           record.get('trackName'), record.get('msPlayed')) for record in records]
        s.bulk_save_objects(objects)
        s.commit()


if __name__ == '__main__':
    # add_all_weights('data/user-site-export/weight*')
    # add_all_sleep('data/user-site-export/sleep-2016*')
    # add_all_steps('data/user-site-export/steps*')
    # add_all_resting_heartrates('data/user-site-export/resting_heart_rate*')
    # add_all_altitudes('data/user-site-export/altitude*')
    add_streaming_history('data/StreamingHistory00.json')
