"""
{
  "dateTime" : "05/16/16 00:00:00",
  "value" : {
    "date" : "05/16/16",
    "value" : 61.87071418762207,
    "error" : 9.121512413024902
  }
"""

import datetime
from sqlalchemy import Column, String, Float, Integer, DateTime, Date, Boolean, BigInteger
from base import Base


class FitbitRestingHeartRate(Base):
    __tablename__ = "resting_heartrates"

    dateTime = Column(DateTime, primary_key=True, unique=True)
    valueBpm = Column(Float)
    error = Column(Float)

    def __init__(self, dateTime, valueBpm, error):
        self.dateTime = datetime.datetime.strptime(dateTime, '%m/%d/%y %H:%M:%S')
        self.valueBpm = valueBpm
        self.error = error
