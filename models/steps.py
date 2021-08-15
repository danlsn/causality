"""
{
  "dateTime" : "11/02/17 00:21:00",
  "value" : "0"
}
"""

import datetime
from sqlalchemy import Column, String, Numeric, Integer, DateTime, Date, Boolean, BigInteger
from base import Base


class FitbitSteps(Base):
    __tablename__ = "steps"

    dateTime = Column(DateTime, primary_key=True, unique=True)
    value = Column(Integer)

    def __init__(self, dateTime, value):
        self.dateTime = datetime.datetime.strptime(dateTime, '%m/%d/%y %H:%M:%S')
        self.value = value

