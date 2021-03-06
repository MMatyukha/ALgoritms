"""
Задание 2.
Реализуйте два алгоритма.
Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.


def is_unique1 (alist : [int]) -> bool:
  for i in range(len(alist)):             # O(n)
    if alist[i] in alist[i+1:]:           # O(n)
      return False                        #  O1
  return True                             #O1
  
  O(n)*O(n)+O1=O(n^2)
  
Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.
Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.
Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.



        
def is_unique3 (alist : [int]) -> bool:
  aset = set(alist)               # O(N)
  return len(aset) == len(alist)  # O(1)

    O(N)+ O(1)=O(N)

