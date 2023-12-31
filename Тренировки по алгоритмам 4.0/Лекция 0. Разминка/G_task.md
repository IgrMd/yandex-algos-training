# G. Кролик учит геометрию

Кролики очень любопытны. Они любят изучать геометрию, бегая по грядкам. Наш кролик как раз такой. Сегодня он решил
изучить новую фигуру — квадрат.

Кролик бегает по грядке — клеточному полю _N × M_ клеток. В некоторых из них посеяны морковки, в некоторых нет.

Помогите кролику найти сторону квадрата наибольшей площади, заполненного морковками полностью.

## Формат ввода

В первой строке даны два натуральных числа _N_ и _M_ _(1 ≤ N, M ≤ 1000)_. Далее в _N_ строках расположено по _M_ чисел,
разделенных пробелами (число равно _0_, если в клетке нет морковки или _1_, если есть).

## Формат вывода

Выведите одно число — сторону наибольшего квадрата, заполненного морковками.

## Пример 1

### Ввод

    4 5
    0 0 0 1 0
    0 1 1 1 0
    0 0 1 1 0
    1 0 1 0 0

### Вывод

    2

## Пример 2

### Ввод

    10 10
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1

### Вывод

    10

## Пример 3

### Ввод

    10 10
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0

### Вывод

    0
