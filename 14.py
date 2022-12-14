from pathlib import Path

from utils import AoC

aoc = AoC(day=int(Path(__file__).stem))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def normalize(a):
    return tuple(
        map(
            int,
            (
                a[0] / (abs(a[0]) if a[0] != 0 else 1),
                a[1] / abs(a[1] if a[1] != 0 else 1),
            ),
        )
    )


def draw(grid, current):
    for i in range(10):
        for j in range(490, 510):
            if (j, i) == current:
                print("+", end="")
            else:
                print(grid.get((j, i), "."), end="")
        print("")
    print("----------------------------")


def simulate_sand(grid, start):
    moves = [(0, -1), (1, -1), (-1, -1)]
    cnt = 0
    while True:
        cnt += 1
        current = start
        # draw(grid, current)
        while True:
            if current[1] > 5000:
                draw(grid, current)
                return cnt - 1
            for m in moves:
                n = sub(current, m)
                if not grid.get(n):
                    current = n
                    break
            else:
                grid[current] = "o"
                if current == (500, 0):
                    return cnt
                break


def part1(inp):
    grid = {}
    for i in inp:
        points = i.split(" -> ")
        instrs = [tuple(map(int, p.split(","))) for p in points]
        for ind, instr in enumerate(instrs[:-1]):
            # draw(grid, (0, 0))
            start, stop = instr, instrs[ind + 1]
            diff = sub(start, stop)
            step = normalize(diff)
            grid[start] = "#"
            current = start
            while current != stop:
                current = sub(current, step)
                grid[current] = "#"
    return simulate_sand(grid, (500, 0))


def part2(inp):
    grid = {}
    for i in inp:
        points = i.split(" -> ")
        instrs = [tuple(map(int, p.split(","))) for p in points]
        for ind, instr in enumerate(instrs[:-1]):
            # draw(grid, (0, 0))
            start, stop = instr, instrs[ind + 1]
            diff = sub(start, stop)
            step = normalize(diff)
            grid[start] = "#"
            current = start
            while current != stop:
                current = sub(current, step)
                grid[current] = "#"
    max_j = max([j for i, j in grid])
    print(max_j)
    for i in range(-1000, 1000):
        grid[(i, max_j + 2)] = "#"

    return simulate_sand(grid, (500, 0))


inp = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()
# assert (p1_res := part1(inp)) == 24, p1_res
# # print(part1(aoc.get_input()))
# # assert False
# aoc.submit_p1(part1(aoc.get_input()))

assert (p2_res := part2(inp)) == 93, p2_res
aoc.submit_p2(part2(aoc.get_input()))
