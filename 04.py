from utils import AoC

aoc = AoC(day=4)
aoc.print_p1()


def part1(inp):
    res = 0
    for i in inp:
        elf1, elf2 = [list(map(int, e.split("-"))) for e in i.split(",")]
        if (
            elf1[0] <= elf2[0]
            and elf1[1] >= elf2[1]
            or elf2[0] <= elf1[0]
            and elf2[1] >= elf1[1]
        ):
            res += 1
    return res


def part2(inp):
    res = 0
    for i in inp:
        elf1, elf2 = [list(map(int, e.split("-"))) for e in i.split(",")]
        elf1 = set(range(elf1[0], elf1[1] + 1))
        elf2 = set(range(elf2[0], elf2[1] + 1))
        if elf1.intersection(elf2):
            res += 1
    return res


assert (
    part1(
        """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()
    )
    == 2
)
aoc.submit_p1(part1(aoc.get_input()))

assert (
    part2(
        """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()
    )
    == 4
)
aoc.submit_p2(part2(aoc.get_input()))
