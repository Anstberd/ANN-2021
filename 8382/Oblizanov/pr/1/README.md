# Практика №1, вариант 6
## Задание:
Написать функцию, которая принимает список чисел и возвращает кортеж из двух элементов. Первый элемент кортежа – мат. ожидание, второй элемент – СКО. Запрещается использовать функции для расчета соответствующих характеристик.

## Реализация:
Функция `m_and_sd` принимает на вход список чисел. Далее по стандартным формулам рассчитывается мат. ожидание и СКО.
Функция возвращает кортеж, что проверяется при выводе результата.

Числа вводятся через пробел в любом количестве. Есть проверка на некорретный ввод через try-except.

### Пример
Ввод: 
```
2.1 8 -5 6 3 -9.5 4 1
```

Вывод:
```
(expected value, standard deviation)
(1.2, 5.409944546850735)
<class 'tuple'>
```

### Проверка

https://math.semestr.ru/math/expectation-discrete.php

Вывод:
```
Математическое ожидание: 1.2
Среднее квадратическое отклонение: 5.41
```

https://allcalc.ru/node/1011

Вывод:
```
Среднее квадратическое отклонение: 5.41
```

