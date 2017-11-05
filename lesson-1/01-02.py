def countTables(n):
  students = map(int, n.split())
  tables = int(sum(list(map(lambda x : x//2+x%2, students))))
  print ("\n> требуется столов: {}\n".format(tables))

while 1:
  string = input("введите кол-во учеников 3-х классов через пробел или -s:")
  if string.lower() == '-s':
    print("\n> --- программа остановлена ---\n")
    break
  countTables(string)
