from pathlib import Path

from utils import AoC

aoc = AoC(day=int(Path(__file__).stem))
aoc.print_p1()


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def mul(a, b):
    return (a[0] * b[0], a[1] * b[1])


def absl(a):
    return abs(a[0]), abs(a[1])


def move_tail(head, tail, dr):

    diff = sub(head, tail)

    if abs(diff[0]) + abs(diff[1]) <= 1:
        return tail

    return add(mul(diff, dr), tail)


moves = {"R": (0, 1), "U": (-1, 0), "L": (0, -1), "D": (1, 0)}


def display(head, tails):
    tails = set(tails)
    size = 10
    for i in range(-size, size):
        for j in range(-size, size):
            if (i, j) in tails:
                print("#", end="")
            elif (i, j) == head:
                print("H", end="")
            else:
                print(".", end="")

        print("")


def move_knot(head, tail):
    diff = sub(head, tail)
    adiff = absl(diff)

    if adiff[0] <= 1 and adiff[1] <= 1:
        return tail

    return (
        (tail[0] - (adiff[0] - 1) if diff[0] < 0 else tail[0] + (adiff[0] - 1))
        if adiff[0] == 2
        else head[0],
        (tail[1] - (adiff[1] - 1) if diff[1] < 0 else tail[1] + (adiff[1] - 1))
        if adiff[1] == 2
        else head[1],
    )


def part1(inp):
    tail = head = prev_head = (0, 0)
    tail_visited = set()
    for i in inp:
        direction, steps = i.split(" ")
        for _ in range(int(steps)):
            tail_visited.add(tail)
            prev_head = head
            head = add(head, moves[direction])
            if abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
                tail = prev_head
    return len(tail_visited)


def part2(inp):
    head = (0, 0)
    knots = [(0, 0) for _ in range(9)]
    tail_visited = set()
    for i in inp:
        direction, steps = i.split(" ")

        for _ in range(int(steps)):
            new_knots = list()
            curr_knot = head = add(head, moves[direction])
            # tail_visited.add(head)
            for knot in knots:
                new_knot = move_knot(curr_knot, knot)
                new_knots.append(new_knot)
                curr_knot = new_knot
            tail_visited.add(knots[-1])
            tail_visited.add(new_knots[-1])

            knots = new_knots
    display(head, tail_visited)
    print(tail_visited)
    return len(tail_visited)


assert (
    part1(
        """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()
    )
    == 13
)
# aoc.submit_p1(part1(aoc.get_input()))
# print(aoc.get_input())
small = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
large = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
assert part2(large.splitlines()) == 36
# assert part2(large.splitlines()) == 36
# aoc.submit_p2(part2(aoc.get_input()))
