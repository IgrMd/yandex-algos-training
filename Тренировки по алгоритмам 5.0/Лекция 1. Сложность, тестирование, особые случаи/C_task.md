# C. Форматирование файла

Петя - начинающий программист. Сегодня он написал код из _n_ строк.  
К сожалению оказалось, что этот код трудно читать. Петя решил исправить это, добавив в различные места пробелы. А
точнее, для _i_-й строки ему нужно добавить **_ровно_** _a<sub>i</sub>_ пробелов.  
Для добавления пробелов Петя выделяет строку и нажимает на одну из трёх клавиш: Space, Tab, и Backspace. При нажатии на
Space в строку добавляется один пробел. При нажатии на Tab в строку добавляются четыре пробела. При нажатии на Backspace
в строке удаляется один пробел.  
Ему хочется узнать, какое наименьшее количество клавиш придётся нажать, чтобы добавить необходимое количество пробелов в
каждую строку. Помогите ему!

## Формат ввода

Первая строка входных данных содержит одно целое положительное число
_n (1 ≤ n ≤ 10<sup>5</sup>)_ – количество строк в файле.
Каждая из следующих n строк содержит одно целое неотрицательное число
_a<sub>i</sub> (0 ≤ a<sub>i</sub> ≤ 10<sup>9</sup>)_ – количество пробелов, которые нужно добавить в _i_-ю строку файла.

## Формат вывода

Выведите одно число – минимальное количество нажатий, чтобы добавить в каждой строке необходимое количество пробелов.

## Пример 1

### Ввод

    5
    1
    4
    12
    9
    0

### Вывод

    8

