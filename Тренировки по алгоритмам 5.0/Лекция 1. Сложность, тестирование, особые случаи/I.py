from collections import defaultdict


def read_input():
    n = int(input())
    year = int(input())
    holidays = set()
    for _ in range(n):
        day, month = input().split()
        holidays.add((int(day), MONTHS[month]))
    start_day_of_week = input()
    return n, year, holidays, start_day_of_week


DAYS = dict()
MONTHS = dict()
MONTH_TO_DAY_COUNT = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def best_worst_days(n, year, holidays, start_day_of_week):
    if is_leap_year(year):
        MONTH_TO_DAY_COUNT[1] = 29
    start_day_of_week = DAYS[start_day_of_week]
    holidays_count = defaultdict(int)
    days_count = defaultdict(int)
    curr_month = 0
    curr_day_of_month = 0
    for day in range(start_day_of_week, 365 + start_day_of_week + is_leap_year(year)):
        week_day = day % 7
        days_count[week_day] += 1
        if (curr_day_of_month + 1, curr_month) in holidays:
            days_count[week_day] -= 1
        curr_day_of_month += 1
        if curr_day_of_month == MONTH_TO_DAY_COUNT[curr_month]:
            curr_month += 1
            curr_day_of_month = 0
    min_count, min_day = 500, 0
    max_count, max_day = 0, 0
    for day, count in days_count.items():
        if count > max_count:
            max_day = day
            max_count = count
        if count < min_count:
            min_day = day
            min_count = count
    return DAYS[max_day], DAYS[min_day]


def main():
    for i, day in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']):
        DAYS[i] = day
        DAYS[day] = i
    for i, month in enumerate(
            ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']):
        MONTHS[i] = month
        MONTHS[month] = i
    print(*best_worst_days(*read_input()), sep=' ')


if __name__ == '__main__':
    main()
