import os
from pathlib import Path
from .LogHandler import LogAppender, LogReader, splitKv, ACTIVE_LOG

class Database:
  def __init__(self, segmentsDir):
    self.segmentsDir = segmentsDir
    self.activeLog = ACTIVE_LOG
    if not Path(segmentsDir).exists():
      Path(segmentsDir).mkdir()
    self.logWriter = LogAppender(segmentsDir)
    self.logReader = LogReader(segmentsDir)
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
    with open(os.path.join(self.segmentsDir, self.activeLog), 'r') as f:
      kvs = [line.strip() for line in f]
      for i, kv in enumerate(kvs):
        k, _ = splitKv(kv)
        self.index[k] = i
      self.cursor = len(kvs)