# C. Быстрый алгоритм Дейкстры

Вам дано описание дорожной сети страны. Ваша задача – найти длину кратчайшего пути между городами А и B.

## Формат ввода

Сеть дорог задана во входном файле следующим образом: первая строка содержит числа _N_ и _K_ _(1 ≤ N ≤ 100000, 0 ≤ K ≤
300000)_, где _K_ – количество дорог. Каждая из следующих _K_ строк содержит описание дороги с двусторонним движением –
три целых числа _a<sub>i</sub>, b<sub>i</sub>_ и _l<sub>i</sub> (1 ≤ a<sub>i</sub>, b<sub>i</sub> ≤ N, 1 ≤ l<sub>
i</sub> ≤ 10<sup>6</sup>)_. Это означает, что имеется дорога длины _l<sub>i</sub>_, которая ведет из города _a<sub>
i</sub>_ в город _b<sub>i</sub>_. В последней строке находятся два числа _А_ и _В_ – номера городов, между которыми надо
посчитать кратчайшее расстояние _(1 ≤ A, B ≤ N)_

## Формат вывода

Выведите одно число – расстояние между нужными городами. Если по дорогам от города А до города В доехать невозможно,
выведите –1.

## Пример 1

### Ввод

    6 4
    1 2 7
    2 4 8
    4 5 1
    4 3 100
    3 1

### Вывод

    115

