import math


class MyTime:
    def __init__(self, data: str):
        h, m, s = [int(x) for x in data.split(sep=':')]
        self.secs = h * 3600 + m * 60 + s

    def __sub__(self, other):
        result = MyTime('00:00:00')
        if self == other:
            result.secs = 0
        elif self > other:
            result.secs = self.secs - other.secs
        else:
            result.secs = 86400 - other.secs + self.secs
        return result

    def __add__(self, other):
        result = MyTime('00:00:00')
        result.secs = (other.secs + self.secs) % 86400
        return result

    def __truediv__(self, other):
        result = MyTime('00:00:00')
        result.secs = self.secs / other
        if result.secs - int(result.secs) < 0.5:
            result.secs = math.floor(result.secs)
        else:
            result.secs = math.ceil(result.secs)
        return result

    def __lt__(self, other):
        return self.secs < other.secs

    def __gt__(self, other):
        return self.secs > other.secs

    def __eq__(self, other):
        return self.secs == other.secs

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        h = self.secs // 3600
        m = self.secs % 3600 // 60
        s = self.secs % 3600 % 60
        return f'{h:02}:{m:02}:{s:02}'


def read_input():
    a, b, c = MyTime(input()), MyTime(input()), MyTime(input())
    return a, b, c


def synchronize(a: MyTime, b: MyTime, c: MyTime) -> MyTime:
    delta = c - a
    delta = delta / 2
    result = b + delta
    return result


assert str(MyTime('05:01:03')) == '05:01:03'
assert str(MyTime('18:09:45')) == '18:09:45'
assert MyTime('05:01:03') == MyTime('05:01:03')
assert MyTime('05:01:03') != MyTime('05:02:03')
assert MyTime('05:02:03') - MyTime('05:01:03') == MyTime('00:01:00')
assert MyTime('00:00:01') - MyTime('23:59:59') == MyTime('00:00:02')
assert MyTime('15:00:00') - MyTime('16:00:00') == MyTime('23:00:00')
assert MyTime('01:02:03') + MyTime('02:03:04') == MyTime('03:05:07')
assert MyTime('23:59:59') + MyTime('00:00:01') == MyTime('00:00:00')
assert MyTime('23:59:59') + MyTime('00:00:02') == MyTime('00:00:01')
assert MyTime('00:00:3') / 2 == MyTime('00:00:02')
assert MyTime('00:00:4') / 3 == MyTime('00:00:01')

assert synchronize(MyTime('15:01:00'), MyTime('18:09:45'), MyTime('15:01:40')) == MyTime('18:10:05')


def main():
    print(synchronize(*read_input()))


if __name__ == '__main__':
    main()
