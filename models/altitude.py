"""
{
  "dateTime" : "02/29/16 19:33:00",
  "value" : "20"
}
"""

import datetime
from sqlalchemy import Column, String, Float, Integer, DateTime, Date, Boolean, BigInteger
from base import Base


class FitbitAltitude(Base):
    __tablename__ = "altitudes"

    dateTime = Column(DateTime, primary_key=True, unique=True)
    value = Column(Integer)

    def __init__(self, dateTime, value):
        self.dateTime = datetime.datetime.strptime(dateTime, '%m/%d/%y %H:%M:%S')
        self.value = value
