"""
Time Complexity: O(N*sqrt(N))
Space Complexity: O(N)
"""

BOOK = "B"
CANCEL = "C"
PRINT = "P"


def main():
    N = int(input())
    user_bookings = {}
    bookings = {}
    result = []
    for _ in range(N):
        command, args = input().split()
        args = int(args)
        if command == BOOK or command == CANCEL:
            # O(1)
            change = 1 if command == BOOK else -1
            current = user_bookings.get(args, 0)
            updated = max(current + change, 0)
            if current:
                bookings[current] -= 1
                if not bookings[current]:
                    del bookings[current]
            if updated >= 1:
                bookings[updated] = bookings.get(updated, 0) + 1
            user_bookings[args] = updated
        else:
            # O(sqrt(N))
            count, total = 0, 0
            for k, v in bookings.items():
                if k >= args:
                    count += v
                    total += k*v
            result += [(count, total)]

    print("\n".join([f"{cnt} {tot}" for cnt, tot in result]))


if __name__ == "__main__":
    main()
