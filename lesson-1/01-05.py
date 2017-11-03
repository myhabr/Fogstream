def calcTime():

  n = int(input("введите кол-во уроков:"));

  if (n<1): n = 1
  if (n>10): n = 10
  
  bgn = [9,00]
  lesDur = 45
  brOdd = 5
  brEv = 15
  
  nBr = n-1
  nBrEv = 0

  if (nBr>1): nBrEv = nBr//2

  nBrOdd = nBr - nBrEv
  fullDur = n*lesDur + nBrEv*brEv + nBrOdd*brOdd
  
  # print("уроков: {}; перемен: {}(5), {}(15)".format(n, int(nBrOdd), int(nBrEv)))
  print("уроки заканчиваются в {}".format(convertTime(fullDur, bgn)))
  
def convertTime(n, start):

  n += start[0]*60 + start[1]
  m = int(n % 60)
  diff = n - m

  if (diff): h = int(diff / 60)
  if (h<10): h = "0" + str(h)
  if (m<10): m = "0" + str(m)

  return ("{}:{}".format(h,m))

calcTime()
