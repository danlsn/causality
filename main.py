# Load Environment Variables
from dotenv import load_dotenv
from sqlalchemy.dialects.postgresql import psycopg2

load_dotenv()

import logging

logging.basicConfig(filename='logs/main.log', encoding='utf-8', level=logging.DEBUG)
logging.getLogger('sqlalchemy.dialects.postgresql').setLevel(logging.DEBUG)

import json
from models.weight import FitbitWeight
from models.heart_rate import FitbitHeartRate
from models.sleep import FitbitSleep
from base import Session, Base, engine
import glob


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


if __name__ == '__main__':
    # add_all_weights('data/user-site-export/weight*')
    add_all_sleep('data/user-site-export/sleep-2016*')
