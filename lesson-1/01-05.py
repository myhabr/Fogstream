def countTime():
  
  print("введите кол-во уроков:")

  n = int(input());

  if (n<1): n = 1
  if (n>10): n = 10
  
  start_h = 9
  start_m = 0
  
  les_dur = 45
  br_odd = 5
  br_ev = 15
  
  n_br = n-1
  
  n_br_ev = n_br_odd = 0
  
  if (n_br == 1): n_br_odd = 1
  
  if (n_br>1):

    if (n_br%2 == 0):
      n_br_odd = n_br_ev = n_br/2
  
    else:
      n_br_ev = (n_br-1)/2
      n_br_odd = n_br_ev+1

  com_dur = n*les_dur + n_br_ev*br_ev + n_br_odd*br_odd
  
  print("уроков: {}; перемен: {}, {}".format(n, int(n_br_odd), int(n_br_ev)))
  
  convertTime(com_dur, start_h, start_m)
  
def convertTime(n, h_st, m_st):
  
  n += h_st*60 + m_st

  m = int(n % 60)
  diff = n - m
    
  if (diff > 0): h = int(diff / 60)

  h = str(h); m = str(m)

  if (len(h) == 1): h = "0" + h
  if (len(m) == 1): m = "0" + m

  print ("уроки закончились в {}:{}".format(h,m))

countTime()
