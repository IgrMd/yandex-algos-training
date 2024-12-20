# H. Стек с суммой*

Стек с суммой должен поддерживать три операции:

1. Добавить число _x_ в стек
2. Подсчитать и вывести сумму _k_ чисел находящихся на вершине стека
3. Удалить число из стека

Реализуйте структуру данных, которая поддерживает эти операции.

## Формат ввода

В первой строке задается количество операций со стеком _n (1 ≤ n ≤ 100000)_.

В следующих n строках задаются операции со стеком. Каждая операция имеет один из трех типов:

_+x_ — добавить в стек число _x (1 ≤ x ≤ 10<sup>9</sup>)_

_—_ — удалить элемент с вершины стека (гарантируется, что в этот момент стек не пуст)

_?k_ — подсчитать и вывести сумму k элементов на вершине стека (гарантируется, что в стеке не менее k элементов)

Изначально стек пуст.

## Формат вывода

Для каждого запроса "_—_" необходимо вывести значение удаляемого из стека элементов, а для каждого запроса "_?k_" —
сумму _k_ элементов на вершине стека.

## Пример 1

### Ввод

    7
    +1
    +2
    +3
    ?2
    -
    -
    ?1

### Вывод

    5
    3
    2
    1

