import math


def countTables(a,b,c):

  def prepareData(x):
    return int(math.fabs(x))
    
  def itemTables(x):
    return math.ceil(x/2)
    
  students = list(map(prepareData, [a,b,c]))
    
  tables = sum(list(map(itemTables, students)))

  print (tables)

countTables(2.3,3,-4)
