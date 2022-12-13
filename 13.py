import functools
from pathlib import Path

from utils import AoC

aoc = AoC(day=int(Path(__file__).stem))
aoc.print_p1()


def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l == r:
            return None
        return l < r
    if isinstance(l, list) and isinstance(r, int):
        return compare(l, [r])
    if isinstance(l, int) and isinstance(r, list):
        return compare([l], r)
    if isinstance(l, list) and isinstance(r, list):
        for i, v1 in enumerate(l):
            try:
                v2 = r[i]
            except:
                return False
            rs = compare(v1, v2)
            if rs is None:
                continue
            return rs
        if len(l) < len(r):
            return True

    return None


def compare2(l, r):
    comp = compare(l, r)
    if comp in (True, None):
        return 1
    else:
        return -1


def part1(inp):

    compares = []
    for ind, i in enumerate(inp.split("\n\n")):
        v1, v2 = i.split()
        loc = {}
        exec("l1 = " + v1, globals(), loc)
        exec("l2 = " + v2, globals(), loc)
        if compare(loc["l1"], loc["l2"]) in (True, None):
            compares.append(ind + 1)
    return sum(compares)


def part2(inp):
    compares = []
    for ind, i in enumerate(inp.split("\n\n")):
        v1, v2 = i.split()
        loc = {}
        exec("l1 = " + v1, globals(), loc)
        exec("l2 = " + v2, globals(), loc)
        compares.append(loc["l1"])
        compares.append(loc["l2"])
    first = [[2]]
    second = [[6]]
    compares.append(first)
    compares.append(second)
    mul = 1
    for i, v in enumerate(
        sorted(compares, key=functools.cmp_to_key(compare2), reverse=True)
    ):
        if v is first or v is second:
            mul *= i + 1
    return mul


assert (
    part1(
        """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
    )
    == 13
)
aoc.submit_p1(part1(aoc.get_input_no_split()))

assert (
    part2(
        """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
    )
    == 140
)
aoc.submit_p2(part2(aoc.get_input_no_split()))
