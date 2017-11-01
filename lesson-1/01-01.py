import math
import cmath

X = 1
Y = -1

def convertComplex(x,y):

  z = math.sqrt(x*x + y*y) # math.hypot(x, y)

  _phi = 0
  m = [0,0]

  if(z != 0):

    _phi = math.asin(math.fabs(y)/z)
    m = [0,1]

    if (x < 0):       m = [ 1, 0]
    if (y < 0):       m = [ 0,-1]
    if (x<0 and y>0): m = [ 1,-1]
    if (x<0 and y<0): m = [-1, 1]
    if (x>0 and y<0): m = [ 0,-1]

  phi = m[0]*math.pi + m[1]*_phi
  
  print("({}, {})".format(z, phi))
  
convertComplex(X,Y)

print(cmath.polar(complex(X,Y)))
