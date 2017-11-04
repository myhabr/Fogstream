def getPoint(n):
  roadLength = 109
  reverse = 0
  v,t = map(float, n.split())
  if v<0:
    reverse = 1
    v = -v
  fullPath = v*t
  path = fullPath % roadLength
  diff = fullPath - path
  if diff: fullPath = path
  if reverse: fullPath = roadLength - fullPath
  fullPath = round(fullPath)
  print("\n> остановка на отметке {}км\n".format(fullPath))
  
while 1:
  string = input("введите скорость (км/ч)\n и время движения (ч) через пробел или -s:")
  if string.lower() == '-s':
    print("\n> --- программа остановлена ---\n")
    break
  getPoint(string)
