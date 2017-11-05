def getPoint(n):
  roadLength = 109
  reverse = 0
  v,t = map(float, n.split())
  if v<0:
    reverse = 1
    v = -v
  fullPath = v*t
  point = fullPath % roadLength
  if reverse and point: point = roadLength - point
  point = round(point)
  print("\n> остановка на отметке {}км\n".format(point))

while 1:
  string = input("введите скорость (км/ч)\n и время движения (ч) через пробел или -s:")
  if string.lower() == '-s':
    print("\n> --- программа остановлена ---\n")
    break
  getPoint(string)
