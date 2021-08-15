"""
{
    "endTime" : "2020-07-14 01:39",
    "artistName" : "Jax Jones",
    "trackName" : "Harder",
    "msPlayed" : 52134
  }
"""

import datetime
from sqlalchemy import Column, String, Float, Integer, DateTime, Date, Boolean, BigInteger
from base import Base


class SpotifyStreamingHistory(Base):
    __tablename__ = 'spotify_streaming_history'

    id = Column(Integer, primary_key=True)
    endTime = Column(DateTime)
    artistName = Column(String)
    trackName = Column(String)
    msPlayed = Column(Integer)

    def __init__(self, endTime, artistName, trackName, msPlayed):
        self.endTime = datetime.datetime.strptime(endTime, '%Y-%m-%d %H:%M')
        self.artistName = artistName
        self.trackName = trackName
        self.msPlayed = msPlayed
