def minToClock(n):
  n = int(n)
  h = 0; m = 0
  if n:
    diff = n - n % (60*24)
    if diff: n = n % (60*24)
    m = n % 60
    diff = n - m
    if diff: h = int(diff/60)
  if h < 10: h = "0"+str(h) # h = "{0:0>2}".format(h)
  if m < 10: m = "0"+str(m) # m = "{0:0>2}".format(m)
  print ("\n> {}:{}\n".format(h,m))

while 1:
  string = input("введите кол-во минут или -s: ")
  if string.lower() == '-s':
    print("\n> --- программа остановлена ---\n")
    break
  minToClock(string)
