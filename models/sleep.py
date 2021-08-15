"""
[{
  "logId" : 1028309330,
  "dateOfSleep" : "2015-06-16",
  "startTime" : "2015-06-15T23:46:00.000",
  "endTime" : "2015-06-16T10:19:10.000",
  "duration" : 37980000,
  "minutesToFallAsleep" : 7,
  "minutesAsleep" : 608,
  "minutesAwake" : 18,
  "minutesAfterWakeup" : 0,
  "timeInBed" : 633,
  "efficiency" : 97,
  "type" : "classic",
  "infoCode" : 0,
  "levels" : {
    "summary" : {
      "restless" : {
        "count" : 14,
        "minutes" : 24
      },
      "awake" : {
        "count" : 1,
        "minutes" : 1
      },
      "asleep" : {
        "count" : 0,
        "minutes" : 608
      }
    },
    "data" : [{
      "dateTime" : "2015-06-15T23:46:00.000",
      "level" : "restless",
      "seconds" : 360
    },{
      "dateTime" : "2015-06-15T23:52:00.000",
      "level" : "awake",
      "seconds" : 60
    },{
      "dateTime" : "2015-06-15T23:53:00.000",
      "level" : "asleep",
      "seconds" : 4620
    },{
      "dateTime" : "2015-06-16T01:10:00.000",
      "level" : "restless",
      "seconds" : 60
    },{
      "dateTime" : "2015-06-16T01:11:00.000",
      "level" : "asleep",
      "seconds" : 3300
    },{
      "dateTime" : "2015-06-16T02:06:00.000",
      "level" : "restless",
      "seconds" : 60
    },{
      "dateTime" : "2015-06-16T02:07:00.000",
      "level" : "asleep",
      "seconds" : 120
    },{
      "dateTime" : "2015-06-16T02:09:00.000",
      "level" : "restless",
      "seconds" : 120
    },{
      "dateTime" : "2015-06-16T02:11:00.000",
      "level" : "asleep",
      "seconds" : 1020
    },{
      "dateTime" : "2015-06-16T02:28:00.000",
      "level" : "restless",
      "seconds" : 60
    },{
      "dateTime" : "2015-06-16T02:29:00.000",
      "level" : "asleep",
      "seconds" : 7200
    },{
      "dateTime" : "2015-06-16T04:29:00.000",
      "level" : "restless",
      "seconds" : 60
    },{
      "dateTime" : "2015-06-16T04:30:00.000",
      "level" : "asleep",
      "seconds" : 4140
    },{
      "dateTime" : "2015-06-16T05:39:00.000",
      "level" : "restless",
      "seconds" : 60
    },{
      "dateTime" : "2015-06-16T05:40:00.000",
      "level" : "asleep",
      "seconds" : 180
    },{
      "dateTime" : "2015-06-16T05:43:00.000",
      "level" : "restless",
      "seconds" : 60
    },{
      "dateTime" : "2015-06-16T05:44:00.000",
      "level" : "asleep",
      "seconds" : 540
    },{
      "dateTime" : "2015-06-16T05:53:00.000",
      "level" : "restless",
      "seconds" : 120
    },{
      "dateTime" : "2015-06-16T05:55:00.000",
      "level" : "asleep",
      "seconds" : 540
    },{
      "dateTime" : "2015-06-16T06:04:00.000",
      "level" : "restless",
      "seconds" : 60
    },{
      "dateTime" : "2015-06-16T06:05:00.000",
      "level" : "asleep",
      "seconds" : 3420
    },{
      "dateTime" : "2015-06-16T07:02:00.000",
      "level" : "restless",
      "seconds" : 60
    },{
      "dateTime" : "2015-06-16T07:03:00.000",
      "level" : "asleep",
      "seconds" : 1440
    },{
      "dateTime" : "2015-06-16T07:27:00.000",
      "level" : "restless",
      "seconds" : 60
    },{
      "dateTime" : "2015-06-16T07:28:00.000",
      "level" : "asleep",
      "seconds" : 360
    },{
      "dateTime" : "2015-06-16T07:34:00.000",
      "level" : "restless",
      "seconds" : 60
    },{
      "dateTime" : "2015-06-16T07:35:00.000",
      "level" : "asleep",
      "seconds" : 1500
    },{
      "dateTime" : "2015-06-16T08:00:00.000",
      "level" : "restless",
      "seconds" : 240
    },{
      "dateTime" : "2015-06-16T08:04:00.000",
      "level" : "asleep",
      "seconds" : 8100
    }]
  },
  "mainSleep" : true
}]
"""

import datetime

from sqlalchemy import Column, String, Numeric, Integer, DateTime, Date, Boolean, BigInteger
from base import Base


class FitbitSleep(Base):
    __tablename__ = "sleep"

    logId = Column(BigInteger, primary_key=True, unique=True)
    dateOfSleep = Column(Date)
    startTime = Column(DateTime)
    endTime = Column(DateTime)
    duration = Column(Integer)
    minutesToFallAsleep = Column(Integer)
    minutesAsleep = Column(Integer)
    minutesAwake = Column(Integer)
    minutesAfterWakeup = Column(Integer)
    timeInBed = Column(Integer)
    efficiency = Column(Integer)
    type = Column(String)
    infoCode = Column(Integer)
    mainSleep = Column(Boolean)

    def __init__(self, logId, dateOfSleep, startTime, endTime, duration, minutesToFallAsleep,
                 minutesAsleep, minutesAwake, minutesAfterWakeup, timeInBed, efficiency,
                 sleepType, infoCode, mainSleep):

        self.logId = logId
        self.dateOfSleep = dateOfSleep
        self.startTime = startTime
        self.endTime = endTime
        self.duration = duration
        self.minutesToFallAsleep = minutesToFallAsleep
        self.minutesAsleep = minutesAsleep
        self.minutesAwake = minutesAwake
        self.minutesAfterWakeup = minutesAfterWakeup
        self.timeInBed = timeInBed
        self.efficiency = efficiency
        self.type = sleepType
        self.infoCode = infoCode
        self.mainSleep = mainSleep

