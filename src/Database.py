import os
from pathlib import Path
from .LogHandler import LogAppender, LogReader, splitKv, ACTIVE_LOG

class Database:
  def __init__(self, datafilesDir):
    self.datafilesDir = datafilesDir
    self.activeLog = ACTIVE_LOG
    if not Path(datafilesDir).exists():
      Path(datafilesDir).mkdir()
    self.logWriter = LogAppender(datafilesDir)
    self.logReader = LogReader(datafilesDir)
    self.cursor = 0 # current location
    self.index = {} # hash index
    self.initIndex()
    print(f'index {self.index}')

  def set(self, key, value):
    log = f"{key},{value}" # key,value
    self.logWriter.write(log)
    self.index[key] = self.cursor
    self.cursor += 1
    print(f'index {self.index}')

  def get(self, key):
    try:
      idx = self.index[key]
      return self.logReader.read(key, idx)
    except KeyError:
      return self.logReader.read(key)

  def initIndex(self):
    with open(os.path.join(self.datafilesDir, self.activeLog), 'r') as f:
      kvs = [line.strip() for line in f]
      for i, kv in enumerate(kvs):
        k, _ = splitKv(kv)
        self.index[k] = i
      self.cursor = len(kvs)