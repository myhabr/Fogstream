import math

def getPoint(v,t):

  reverse = False

  if (v<0): reverse = True

  roadLength = 109

  v = math.fabs(v)

  fullPath = v*t

  path = fullPath % roadLength

  diff = fullPath - path

  if (diff > 0):

    fullPath = path
    
  if (reverse):
    
    fullPath = roadLength - fullPath
    
  fullPath = round(fullPath)
  
  print(fullPath)

getPoint(-62,4.3)
