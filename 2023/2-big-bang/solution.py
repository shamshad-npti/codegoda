"""
Approach: Greedy, Stack
Time Complexity: O(N)
Space Complexity: O(N)
"""


class Body(object):
    def __init__(self, mass, momentum):
        self.mass = mass
        self.momentum = momentum

    def __add__(self, other):
        return Body(self.mass + other.mass, self.momentum + other.momentum)

    def __lt__(self, other):
        return self.momentum * other.mass < other.momentum * self.mass


def main():
    _ = int(input())
    masses = list(map(int, input().split()))
    velocities = list(map(int, input().split()))
    bodies = [Body(m, m*v) for m, v in zip(masses, velocities)]
    stack = []
    for body in bodies:
        while stack and body < stack[-1]:
            body += stack.pop()
        stack += [body]

    print(len(stack))
    stack.sort(key=lambda body: (body.mass, body.momentum))
    print("\n".join(map(lambda body: f"{body.mass} {body.momentum}", stack)))


if __name__ == "__main__":
    main()
