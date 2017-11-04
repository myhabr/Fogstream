def countTables(n):
  def itemTables(x):
    if x%2: x+=1
    return x/2
  students = map(int, n.split())
  tables = int(sum(list(map(itemTables, students))))
  print ("\n> требуется столов: {}\n".format(tables))

while 1:
  string = input("введите кол-во учеников 3-х классов через пробел или -s:")
  if string.lower() == '-s':
    print("\n> --- программа остановлена ---\n")
    break
  countTables(string)
