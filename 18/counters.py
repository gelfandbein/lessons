"""
Создать модуль с названием counters который содержит
две функции count_lines и count_chars
Обе функции принимают имя файла в качестве
обязательного аргумента и возвращают число -
результат выполнения. Первая функция возвращает кол-во
строк в файле, вторая - кол-во непробельных символов
(т.е. исключая пробелы, табуляторы и символы перевода на новую строку).

Доп. задание: модуль counters переписать в виде пакета,
а каждую функции перенести в отдельный под-модуль.
"""

def count_lines(f):
  lines = 0
  for line in f:
    lines += 1
  return lines
  
def count_chars(f):
    chars=0
    for line in f:
        lines=line.split()
        chars += sum(len(word) for word in lines)
    return chars
  
def main(filename):
  with open(filename) as f:
    print(count_lines(f))
    f.seek(0)
    print(count_chars(f))
  
def end(self):
  """ clear all """
  pass


if __name__ == "__main__":
  main("./text.txt")
