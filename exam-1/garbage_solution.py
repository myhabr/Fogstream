from datetime import datetime

class Singleton(type):
  _instances = {}
  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
    return cls._instances[cls]

catalog = [
{"id":1, "author":"Lev Tolstoy", "title":"War and Peace", "year":"1869"},
{"id":2, "author":"Harper Lee", "title":"To Kill a Mockingbird", "year":"1960"},
{"id":3, "author":"Jacque Fresco", "title":"The Best That Money Can't Buy", "year":"2002"}
]

def sanValue(val):
  val = val.lower().replace(" ","")
  if not val:
    print("\nОшибка ввода")
  return val

class Library(metaclass=Singleton):

  def __init__(self, data):
    self._catalog = data
    self._lastId = self._catalog[-1]['id']
    
  def printItem(self, i):
    print()
    for k, v in self._catalog[i].items():
      print("{}:\t{}".format(k, v))

  def printCatalog(self):
    print("\n" + "-"*16 + " Каталог: " + "-"*16)
    catalogSize = len(self._catalog)
    if (catalogSize):
      for i in range(catalogSize):
        self.printItem(i)
    else:
      print("\nВ каталоге нет записей")
    print("\n"+"-"*42)
  
  def findRec(self, idRec):
    for item in self._catalog:
      if item['id'] == idRec:
        return self._catalog.index(item)
    return -1

  def searchByField(self, field, words):
    result = []
    for item in self._catalog:
      for word in words:
        fieldWords = str(item[field]).lower().split()
        for fieldWord in fieldWords:
          if word == fieldWord:
            result.append(self._catalog.index(item))
    return result

  def searchRec(self):
    while 1:
      searchField = None
      searchOpt = input("\nВведите команду поиска или -help:")
      searchOpt = sanValue(searchOpt)
      if not searchOpt: continue
      if searchOpt == "-help": print("\n -i - поиск по полю 'id'\n -a - поиск по полю 'author'\n -t - поиск по полю 'title'\n -y - поиск по полю 'year'\n -c - выход")
      elif searchOpt == "-c": break
      elif searchOpt == "-i": searchField = "id"
      elif searchOpt == "-a": searchField = "author"
      elif searchOpt == "-t": searchField = "title"
      elif searchOpt == "-y": searchField = "year"
      else: print("\nНеизвестная команда '{}'".format(searchOpt))
      if searchField:
        while 1:
          keyWords = input("\nПоиск по полю '{}'. Введите ключевые слова через пробел или -c:".format(searchField)).lower()
          if not keyWords:
            print("\nОшибка ввода")
            continue
          if keyWords == "-c": break
          keyWords = keyWords.split()
          indexes = self.searchByField(searchField, keyWords)
          if (indexes):
            print("\nРезультаты поиска:")
            list(map(self.printItem, indexes))
          else:
            print("\nНичего не найдено")

  def createRec(self):
    while 1:
      try:
        author = str(input("\nВведите автора книги:"))
        title = str(input("\nВведите название книги:"))
        year = input("\nВведите год издания книги:")
        year = int(sanValue(year))
      except ValueError:
        print("\nОшибка ввода")
        continue
      else:
        if (year > datetime.now().year):
          print("\nКнига еще не написана")
          continue
        newId = self._lastId+1
        newBook = dict(id=newId,author=author,title=title,year=year)
        try:
          self._catalog.append(newBook)
        except Exception:
          print("\nОшибка записи в каталог\n")
        else:
          self._lastId = newId
          newIndex = self.findRec("id")
          print("\nВ каталог добавлена запись:")
          self.printItem(newIndex)
          break

  def deleteRec(self):
    try:
      deletedid = input("\nВведите id книги для удаления:")
      deletedid = int(sanValue(deletedid))
    except ValueError:
      print("\nОшибка ввода")
      return None
    detetedIndex = self.findRec(deletedid)
    if detetedIndex != -1:
      print("\nБудет удалена книга:")
      self.printItem(detetedIndex)
      resp = input("\nПодтвердите удаление? (y/n):")
      resp = sanValue(resp)
      if resp == "y":
        try:
          del self._catalog[detetedIndex]
          print("\nКнига была удалена из каталога")
        except:
          print("\nОшибка выполнения операции")
    else:
      print("\nКнига c id = {} не найдена".format(deletedid))

  def updateRec(self):
    while 1:
      editedId = input("\nВведите id книги для редактирования или -c:")
      editedId = sanValue(editedId)
      if isinstance(editedId, str):
        if editedId.lower() == "-c":
          break
      try:
        editedId = int(editedId)
      except ValueError:
        print("\nОшибка ввода")
        continue
      else:
        editedIndex = self.findRec(editedId)
        if editedIndex != -1:
          print("\nНайдена запись для редактирования:")
          self.printItem(editedIndex)
          item = self._catalog[editedIndex]
          while 1:
            editedField = None
            editedKey = input("\nРедактирование полей книги\n\n -a - author\n -t - title\n -y - year\n -c - выход\n\nВведите поле для редактирования или -c:")
            editedKey = sanValue(editedKey)
            if not editedKey: continue
            if editedKey == "-c": break
            elif editedKey == "-a": editedField = 'author'
            elif editedKey == "-t": editedField = 'title'
            elif editedKey == "-y": editedField = 'year'
            if editedField:
              print("\nТекущее значение поля '{}': {}".format(editedField, item[editedField]))
              newValue = str(input("\nВведите новое значение для поля '{}' или -c:".format(editedField)))
              if newValue.lower() == "-c": continue
              item[editedField] = newValue
              print("\nЗначение поля было изменено")
            else:
              print("\nНеизвестная команда '{}'".format(editedKey))
        else:
          print("\nКнига c id = {} не найдена".format(editedId))

a = Library(catalog)

while 1:
  action = input("\nВведите команду или -help:")
  action = sanValue(action)
  if not action: continue
  if action == "-help": print("\n -l - показать все книги в каталоге\n -f - поиск по каталогу\n -n - добавить книгу в каталог\n -u - редактировать данные книги\n -d - удалить книгу из каталога\n -s - выход из программы")
  elif action == "-l": a.printCatalog()
  elif action == "-f": a.searchRec()
  elif action == "-n": a.createRec()
  elif action == "-u": a.updateRec() 
  elif action == "-d": a.deleteRec()
  elif action == "-s":
    print("\nПрограмма остановлена\n")
    break
  else: print("\nНеизвестная команда '{}'".format(action))
