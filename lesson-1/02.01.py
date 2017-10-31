import math
import numpy as np

def countTables(a,b,c):
  
  students = np.array([int(a),int(b),int(c)])
  
  def itemTables(x):
    
    return math.ceil(x/2)
    
  itemTables = np.vectorize(itemTables, otypes=[np.int])

  tables = np.sum(itemTables(students))

  print ( tables )
  
countTables(2,3,15)
