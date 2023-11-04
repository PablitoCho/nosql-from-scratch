import os, sys
from pathlib import Path
from .LogHandler import LogAppender, LogReader

class Database:
  def __init__(self, datafilesDir):
    self.datafilesDir = datafilesDir
    if not Path(datafilesDir).exists():
      Path(datafilesDir).mkdir()
    self.logWriter = LogAppender(datafilesDir)
    self.logReader = LogReader(datafilesDir)

  def set(self, key, value):
    log = f"{key},{value}" # key,value
    self.logWriter.write(log)

  def get(self, key):
    return self.logReader.read(key)