"""
# Sample Fitbit Heart rate data record
{
  "dateTime" : "04/02/17 23:32:24",
  "value" : {
    "bpm" : 70,
    "confidence" : 0
  }
"""

import datetime

from sqlalchemy import Column, String, Numeric, Integer, DateTime, Time
from base import Base


class FitbitHeartRate(Base):
    __tablename__ = "heartrates"

    date = Column(DateTime, primary_key=True, unique=True)
    bpm = Column(Integer)
    confidence = Column(Integer)

    def __init__(self, dateTime, valueBpm, valueConfidence):
        self.date = datetime.datetime.strptime(dateTime, '%m/%d/%y %H:%M:%S')
        self.bpm = valueBpm
        self.confidence = valueConfidence
