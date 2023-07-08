def read_input():
    n, d = [int(x) for x in input().split()]
    coordinates = [int(x) for x in input().split()]
    return n, d, coordinates


def students_tickets(n: int, d: int, coordinates: list, ):
    events = []
    for coordinate in coordinates:
        events.append((coordinate + d, 1))
        events.append((coordinate, -1))

    events.sort()
    curr_ticket_count = 0
    ticket_count = 0
    for coordinate, factor in events:
        curr_ticket_count += -factor
        ticket_count = max(curr_ticket_count, ticket_count)
    students = [(coordinate, student_id) for student_id, coordinate in enumerate(coordinates)]
    students.sort()
    tickets = [0] * n
    for i in range(n):
        tickets[students[i][1]] = i % ticket_count + 1

    return ticket_count, tickets


def main():
    ticket_count, tickets = students_tickets(*read_input())
    print(ticket_count)
    print(*tickets)


if __name__ == '__main__':
    main()
