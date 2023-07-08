AD_LENGTH = 5


def read_input():
    n = int(input())
    customers = []
    for _ in range(n):
        start, end = list(map(int, input().split()))
        if end - start < AD_LENGTH:
            continue
        customers.append((start, end - AD_LENGTH))
    return n, customers


def ad_schedule(n: int, customers: list, ):
    if len(customers) == 0:
        return 0, 1, 6
    if len(customers) == 1:
        return 1, customers[0][0], customers[0][0] + 5
    events = []
    for customer_id, (start, end) in enumerate(customers):
        events.append((start, 0, customer_id))
        events.append((end, 1, customer_id))
    events.sort()

    ad_start1 = 0
    ad_start2 = 0
    max_customers_listen = 0
    first_ad = set()
    for i in range(len(events)):
        event1 = events[i]
        if event1[1] == 0:
            first_ad.add(event1[2])
            if len(first_ad) > max_customers_listen:
                max_customers_listen = len(first_ad)
                ad_start1 = event1[0]
                ad_start2 = ad_start1 + AD_LENGTH
            second_ad = 0
            for j in range(i + 1, len(events)):
                event2 = events[j]
                if event2[2] in first_ad:
                    continue
                if event2[1] == 0:
                    second_ad += 1
                if event2[0] - event1[0] >= AD_LENGTH and second_ad + len(first_ad) > max_customers_listen:
                    max_customers_listen = second_ad + len(first_ad)
                    ad_start1 = event1[0]
                    ad_start2 = event2[0]
                if event2[1] == 1:
                    second_ad -= 1
        if event1[1] == 1:
            first_ad.remove(event1[2])
    return max_customers_listen, min(ad_start1, ad_start2), max(ad_start1, ad_start2)


def main():
    print(*ad_schedule(*read_input()))


if __name__ == '__main__':
    main()
