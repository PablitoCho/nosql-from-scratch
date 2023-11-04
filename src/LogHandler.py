import os
ACTIVE_LOG = 'datafile.log'

def singleton(class_): # singleton 출처 : https://jh-bk.tistory.com/43
  instances = {}
  def get_instance(*args, **kwargs):
    if class_ not in instances:
      instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return get_instance

@singleton
class LogAppender:
  def __init__(self, datafilesDir):
    self.datafilesDir = datafilesDir
    self.activeLog = ACTIVE_LOG
    self.stream = open(os.path.join(self.datafilesDir, self.activeLog), 'a')
  
  def write(self, log):
    try:
      self.stream.write(log + '\n')
      self.stream.flush()
    except IOError:
      print("File stream not opened")

class LogReader:
  def __init__(self, datafilesDir):
    self.datafilesDir = datafilesDir
    self.activeLog = ACTIVE_LOG

  def read(self, key, index=None):
    with open(os.path.join(self.datafilesDir, self.activeLog), 'r') as f:
      kvs = [line.strip() for line in f]
      if index:
        print('by index')
        _, value = splitKv(kvs[index])
        return value
      print('fullscan')
      for kv in reversed(kvs):
        k, v = splitKv(kv)
        if k == key:
          return v
      return None

def splitKv(log):
  key = log.split(',')[0]
  value = ''.join(log.split(',')[1:])
  return key, value