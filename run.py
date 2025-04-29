import json
from datetime import datetime

def check_capacity(max_capacity: int, guests: list) -> bool:

    events = []
    for i in guests:
        check_in = datetime.strptime(i["check-in"], "%Y-%m-%d")
        check_out = datetime.strptime(i["check-out"], "%Y-%m-%d")
        events.append((check_in, +1))
        events.append((check_out, -1))

    events.sort(key=lambda x: (x[0], x[1]))
    counter = 0
    for i in events:
        counter += i[1]
        if counter > max_capacity:
            return False

    return True


if __name__ == "__main__":
    max_capacity = int(input())
    n = int(input())


    guests = []
    for _ in range(n):
        guest_json = input()
        guest_data = json.loads(guest_json)
        guests.append(guest_data)

    # print(guests)
    result = check_capacity(max_capacity, guests)
    print(result)