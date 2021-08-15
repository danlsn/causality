"""
Sample Fitbit Weight Log Entry
"logId" : 1501718399000,
  "weight" : 181.2,
  "bmi" : 26.24,
  "fat" : 23.600000381469727,
  "date" : "08/02/17",
  "time" : "23:59:59",
  "source" : "API"
"""
import datetime

from sqlalchemy import Column, String, Numeric, Integer, Date, Time
from base import Base


class FitbitWeight(Base):
    __tablename__ = "weight"

    id = Column(Integer, primary_key=True, unique=True)
    weight = Column(Numeric(5, 1))
    bmi = Column(Numeric(5, 1))
    fat = Column(Numeric(20, 1))
    date = Column(Date)  # MM/DD/YYYY
    time = Column(Time)  # HH:mm:ss
    source = Column(String)

    def __init__(self, logId: Integer, weight: Numeric, bmi: Numeric,
                 fat, date: Date, time: Time, source: String):
        self.id = logId
        self.weight = weight
        self.bmi = bmi
        self.fat = fat
        self.date = datetime.datetime.strptime(date, '%m/%d/%y')
        self.time = datetime.datetime.strptime(time, '%H:%M:%S')
        self.source = source
