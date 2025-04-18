# E. Наибольшее произведение двух чисел (составление тестов)

На соревновании участникам была предложена следующая задача:

——

Дан список, заполненный произвольными целыми числами. Найдите в этом списке два числа, произведение которых максимально.
Выведите эти числа в порядке неубывания.

Список содержит не менее двух элементов. Числа подобраны так, что ответ однозначен.

Решение должно иметь сложность _O(n)_, где _n_ - размер списка.

——

Вам предстоит разработать набор тестов (только входных данных) для этой задачи, тщательно проверяющий решения
участников.

## Формат вывода

Сдавать следует не программу, а текстовый файл.

В первой строке файла запишите число _(1 ≤ N ≤ 20)_ — количество тестов, которые вы разработали.

В следующих _N_ строках запишите по одному тесту. Каждый тест должен состоять из одной строки, в которой записано число
_K_ _(2 ≤ K ≤ 10)_ — количества чисел в последовательности, а затем _K_ чисел _a<sub>i</sub> (-100 ≤ a<sub>i</sub>
≤100)_.

## Примечания

Пример формата файла для сдачи:

2

3 1 2 3

5 -1 1 0 -2 3
