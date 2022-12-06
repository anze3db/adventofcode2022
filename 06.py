from pathlib import Path

from utils import AoC

aoc = AoC(day=int(Path(__file__).stem))
aoc.print_p1()


def part1(inp):
    for i in range(len(inp)):
        if len(set(inp[i : i + 4])) == 4:
            return i + 4


def part2(inp):
    for i in range(len(inp)):
        if len(set(inp[i : i + 14])) == 14:
            return i + 14


assert part1("""mjqjpqmgbljsphdztnvjfqwrcgsmlb""") == 7
aoc.submit_p1(part1(aoc.get_input_no_split()))

assert part2("""mjqjpqmgbljsphdztnvjfqwrcgsmlb""") == 19
aoc.submit_p2(part2(aoc.get_input_no_split()))
