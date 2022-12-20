from collections import deque
from pathlib import Path

from utils import AoC

aoc = AoC(day=int(Path(__file__).stem))
aoc.print_p1()


def part1(inp):
    l = [(int(v), i) for i, v in enumerate(inp)]
    q = deque(l)
    for v, i in l:
        c = q.index((v, i))
        q.remove((v, i))
        q.rotate(-v)
        q.insert(c, (v, i))

    final = [r for r, _ in q]
    zero = final.index(0)
    res = sum(
        [
            final[(zero + 1000) % len(inp)],
            final[(zero + 2000) % len(inp)],
            final[(zero + 3000) % len(inp)],
        ]
    )
    return res


def part2(inp):
    l = [(int(v) * 811589153, i) for i, v in enumerate(inp)]
    q = deque(l)
    for _ in range(10):
        for v, i in l:
            c = q.index((v, i))
            q.remove((v, i))
            q.rotate(-v)
            q.insert(c, (v, i))

    final = [r for r, _ in q]
    zero = final.index(0)
    res = sum(
        [
            final[(zero + 1000) % len(inp)],
            final[(zero + 2000) % len(inp)],
            final[(zero + 3000) % len(inp)],
        ]
    )
    return res


inp = """1
2
-3
3
-2
0
4""".splitlines()
assert (p1_res := part1(inp)) == 3, p1_res
aoc.submit_p1(part1(aoc.get_input()))

assert (p2_res := part2(inp)) == 1623178306, p2_res
aoc.submit_p2(part2(aoc.get_input()))
