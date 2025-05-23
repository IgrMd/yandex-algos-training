# A. Угадай число - 2

Август загадал натуральное число от 1 до n. Беатриса пытается угадать это число, для этого она называет некоторые
множества натуральных чисел. Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO в
противном случае. После нескольких заданных вопросов Беатриса запуталась в том, какие вопросы она задавала и какие
ответы получила и просит вас помочь ей определить, какие числа мог задумать Август.

Август и Беатриса продолжают играть в игру, но Август начал жульничать. На каждый из вопросов Беатрисы он выбирает такой
вариант ответа YES или NO, чтобы множество возможных задуманных чисел оставалось как можно больше. Например, если Август
задумал число от 1 до 5, а Беатриса спросила про числа 1 и 2, то Август ответит NO, а если Беатриса спросит про 1, 2, 3,
то Август ответит YES. Если же Бетриса в своем вопросе перечисляет ровно половину из задуманных чисел, то Август из
вредности всегда отвечает NO. Наконец, Август при ответе учитывает все предыдущие вопросы Беатрисы и свои ответы на них,
то есть множество возможных задуманных чисел уменьшается.

## Формат ввода

Вам дана последовательность вопросов Беатрисы. Приведите ответы Августа на них. Первая строка входных данных содержит
число n — наибольшее число, которое мог загадать Август. Далее идут строки, содержащие вопросы Беатрисы. Каждая строка
представляет собой набор чисел, разделенных пробелами. Последняя строка входных данных содержит одно слово HELP.

## Формат вывода

Для каждого вопроса Беатрисы выведите ответ Августа на этот вопрос. После этого выведите (через пробел, в порядке
возрастания) все числа, которые мог загадать Август после ответа на все вопросы Беатрисы.

## Пример 1

### Ввод

    10
    1 2 3 4 5
    2 4 6 8 10
    HELP

### Вывод

    NO
    YES
    6 8 10

## Пример 2

### Ввод

    10
    1
    2
    3
    4
    5
    6
    7
    8
    9
    HELP

### Вывод

    NO
    NO
    NO
    NO
    NO
    NO
    NO
    NO
    NO
    10

## Пример 3

### Ввод

    16
    1 2 3 4 5 6 7 8
    9 10 11 12
    13 14
    16
    HELP

### Вывод

    NO
    NO
    NO
    NO
    15