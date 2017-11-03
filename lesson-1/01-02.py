def countTables():
  
  def itemTables(x):
    if x%2: x+=1
    return x/2
  
  students = map(int, input("введите кол-во учеников 3-х классов через пробел:").split())
  tables = int(sum(list(map(itemTables, students))))

  print ("требуется столов: {}".format(tables))


countTables()
