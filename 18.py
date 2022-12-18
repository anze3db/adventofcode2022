from pathlib import Path

from utils import AoC

aoc = AoC(day=int(Path(__file__).stem))
aoc.print_p1()


def add(c1, c2):
    return c1[0] + c2[0], c1[1] + c2[1], c1[2] + c2[2]


def part1(inp):
    cubes = set()
    for i in inp:
        x, y, z = tuple(map(int, i.split(",")))
        cubes.add((x, y, z))
    sides = len(cubes) * 6
    for cube in cubes:
        for i in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
            side = add(cube, i)
            if side in cubes:
                sides -= 1

    return sides


def part2(inp):
    cubes = set()
    for i in inp:
        x, y, z = tuple(map(int, i.split(",")))
        cubes.add((x, y, z))

    visited = set()
    to_visit = [(0, 0, 0)]

    while to_visit:
        cur = to_visit.pop()
        visited.add(cur)
        for side in (
            (-1, 0, 0),
            (1, 0, 0),
            (0, -1, 0),
            (0, 1, 0),
            (0, 0, -1),
            (0, 0, 1),
        ):
            s = add(side, cur)
            if s in cubes or s in visited:
                continue
            if -1 <= s[0] < 25 and -1 <= s[1] < 25 and -1 <= s[2] < 25:
                to_visit.append(s)

    sides = 0
    for cube in cubes:
        for i in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
            side = add(cube, i)
            if side in visited:
                sides += 1

    return sides


inp = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
""".splitlines()
assert (p1_res := part1(inp)) == 64, p1_res
aoc.submit_p1(part1(aoc.get_input()))

assert (p2_res := part2(inp)) == 58, p2_res
aoc.submit_p2(part2(aoc.get_input()))
