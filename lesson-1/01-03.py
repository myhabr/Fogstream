def minToClock(n):
  n = n % (60*24)
  h = "{0:0>2}".format(n//60)
  m = "{0:0>2}".format(n%60)
  print ("\n> {}:{}\n".format(h,m))

while 1:
  string = input("введите число минут или -s: ")
  if string.lower() == '-s':
    print("\n> --- программа остановлена ---\n")
    break
  minToClock(int(string))
