from pathlib import Path

from utils import AoC

aoc = AoC(day=int(Path(__file__).stem))
aoc.print_p1()

test_inp = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


def part1(inp):
    cycle = 1
    x = 1
    res = 0
    for i in inp:
        instr, *val = i.split(" ")
        if instr == "noop":
            cycle += 1
            if cycle in (20, 60, 100, 140, 180, 220):
                res += x * cycle
            continue
        v = int(val[0])
        cycle += 1
        if cycle in (20, 60, 100, 140, 180, 220):
            res += x * cycle
        cycle += 1
        x += v
        if cycle in (20, 60, 100, 140, 180, 220):
            res += x * cycle
    return res


def part2(inp):
    cycle = 1
    x = 1
    res = 0
    row = ["."] * 40
    for i in inp:
        instr, *val = i.split(" ")
        if instr == "noop":
            if (cycle % 40) in (x, x + 1, x + 2):
                row[(cycle - 1) % 40] = "#"
            cycle += 1
            if cycle in (40, 80, 120, 160, 200, 240):
                print("".join(row))
                row = ["."] * 40
            continue
        v = int(val[0])
        if (cycle % 40) in (x, x + 1, x + 2):
            row[(cycle - 1) % 40] = "#"
        cycle += 1
        if cycle in (40, 80, 120, 160, 200, 240):
            print("".join(row))
            row = ["."] * 40
        if (cycle % 40) in (x, x + 1, x + 2):
            row[(cycle - 1) % 40] = "#"
        cycle += 1
        x += v
        if cycle in (40, 80, 120, 160, 200, 240):
            print("".join(row))
            row = ["."] * 40

    return res


assert part1(test_inp.splitlines()) == 13140
aoc.submit_p1(part1(aoc.get_input()))

part2(part2(aoc.get_input()))
aoc.submit_p2(part2(aoc.get_input()))
