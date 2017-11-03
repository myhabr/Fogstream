def minToClock():
  
  h = 0; m = 0
  
  n = int(input("введите кол-во минут:"))
  
  if n:
    
    diff = n - n % (60*24)
    
    if diff: n = n % (60*24)

    m = n % 60
    diff = n - m
    
    if diff: h = int(diff/60)

  if h < 10: h = "0" + str(h)
  if m < 10: m = "0" + str(m)

  print ("на часах {}:{}".format(h,m))


minToClock()
