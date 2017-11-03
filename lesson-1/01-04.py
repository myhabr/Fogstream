def getPoint():
  
  roadLength = 109
  reverse = 0
  
  v,t = map(float, input("введите скорость (км/ч) и время движения (ч) через пробел:").split())
  
  if v<0:
    reverse = 1
    v = -v

  fullPath = v*t
  path = fullPath % roadLength
  diff = fullPath - path

  if diff: fullPath = path
  if reverse: fullPath = roadLength - fullPath

  fullPath = round(fullPath)
  
  print("остановка на отметке {}км".format(fullPath))

getPoint()
