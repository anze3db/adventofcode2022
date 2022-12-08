from pathlib import Path

from utils import AoC

aoc = AoC(day=int(Path(__file__).stem))
aoc.print_p1()


def part1(inp):
    grid = {}
    for i, line in enumerate(inp):
        for j, l in enumerate(line):
            grid[(i, j)] = int(l)
    res = 0
    for tree in grid:
        for d in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            offset = 1
            brk = False
            while True:
                current_off = (d[0] * offset + tree[0], d[1] * offset + tree[1])
                offset += 1
                if (curr := grid.get(current_off)) is None:
                    res += 1
                    brk = True
                    break
                if curr >= grid[tree]:
                    break
            if brk:
                break

    return res


def part2(inp):
    grid = {}
    for i, line in enumerate(inp):
        for j, l in enumerate(line):
            grid[(i, j)] = int(l)
    res = 0
    scores = []
    for tree in grid:
        score = 1
        for d in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            tmp_score = 0
            offset = 1
            brk = False
            while True:
                current_off = (d[0] * offset + tree[0], d[1] * offset + tree[1])
                offset += 1
                if (curr := grid.get(current_off)) is None:
                    res += 1
                    brk = True
                    break
                tmp_score += 1
                if curr >= grid[tree]:
                    break
            score *= tmp_score
            # if brk:
            #     break

        scores.append(score)
    return max(scores)


assert (
    part1(
        """30373
25512
65332
33549
35390""".splitlines()
    )
    == 21
)
aoc.submit_p1(part1(aoc.get_input()))

assert (
    part2(
        """30373
25512
65332
33549
35390""".splitlines()
    )
    == 8
)
aoc.submit_p2(part2(aoc.get_input()))
