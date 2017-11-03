def calcTime():
  
  bgn = [9,00]
  lesDur = 45
  brOdd = 5
  brEv = 15

  n = int(input("введите кол-во уроков:"))

  if n<1: n = 1
  if n>10: n = 10
  
  nBr = n-1
  nBrEv = 0

  if nBr>1: nBrEv = nBr//2

  nBrOdd = nBr - nBrEv
  fullDur = n*lesDur + nBrEv*brEv + nBrOdd*brOdd
  
  # print("уроков: {}; перемен: {}({}), {}({})".format(n, int(nBrOdd), brOdd, int(nBrEv), brEv))
  print("уроки заканчиваются в {}".format(convertTime(fullDur, bgn)))
  
def convertTime(n, bgn):

  n += bgn[0]*60 + bgn[1]
  m = int(n % 60)
  diff = n - m

  if diff: h = int(diff / 60)
  if h<10: h = "0" + str(h)
  if m<10: m = "0" + str(m)

  return ("{}:{}".format(h,m))

calcTime()
