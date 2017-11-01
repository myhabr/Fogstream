import math


def minToTime(n):
  
  n = int(math.fabs(n))
  h = 0; m = 0
  
  if (n > 0):
    
    diff = n - n % (60*24)
    
    if (diff > 0): n = n % (60*24)
    
    m = n % 60
    diff = n - m
    
    if (diff > 0): h = int(diff / 60)

  h = str(h); m = str(m)

  if (len(h) == 1): h = "0" + h
  if (len(m) == 1): m = "0" + m

  print ("{}:{}".format(h,m))

minToTime(0)
minToTime(59)
minToTime(60)
minToTime(-500)
minToTime(1439)
minToTime(1440)
minToTime(1499)
minToTime(778643)
minToTime(345345.5464)
minToTime(-77.8643)
