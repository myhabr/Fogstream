def convertTime(n, bgn):
  n += bgn[0]*60 + bgn[1]
  m = int(n % 60)
  h = int(n // 60)
  if h<10: h = "0" + str(h)
  if m<10: m = "0" + str(m)
  return ("{}:{}".format(h,m))

def calcTime(n):
  bgn = [9,00]
  lesDur, brOdd, brEv = 45, 5, 15
  n = int(n)
  if n<1: n = 1
  if n>10: n = 10
  nBr = n-1
  nBrEv = 0
  if nBr>1: nBrEv = nBr//2
  nBrOdd = nBr - nBrEv
  fullDur = n*lesDur + nBrEv*brEv + nBrOdd*brOdd
  print("\n> уроков: {}; перемен: {}({}), {}({})\n> заканчиваются в {}\n".format(n, int(nBrOdd), brOdd, int(nBrEv), brEv, convertTime(fullDur, bgn)))

while 1:
  string = input("введите кол-во уроков или -s:")
  if string.lower() == '-s':
    print("\n> --- программа остановлена ---\n")
    break
  calcTime(string)
