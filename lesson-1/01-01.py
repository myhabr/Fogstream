import math
import cmath


def convertComplex(n):
  x, y = map(float, n.split())
  z = (x*x + y*y)**.5 # math.hypot(x, y)
  _phi = 0
  m = [0,0]
  if z:
    _phi = math.asin(math.fabs(y)/z)
    m = [0,1]
    if x < 0:       m = [ 1, 0]
    if y < 0:       m = [ 0,-1]
    if x<0 and y>0: m = [ 1,-1]
    if x<0 and y<0: m = [-1, 1]
    if x>0 and y<0: m = [ 0,-1]
  phi = m[0]*math.pi + m[1]*_phi
  print("\n({}, {})".format(z, phi))
  print(cmath.polar(complex(x,y)))

while 1:
  string = input("\nвведите X Y через пробел или -s:")
  if string.lower() == '-s':
    print("\n> --- программа остановлена ---\n")
    break
  convertComplex(string)
