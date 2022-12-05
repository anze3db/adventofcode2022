from collections import defaultdict
from pathlib import Path

from utils import AoC

aoc = AoC(day=int(Path(__file__).stem))
aoc.print_p1()


def part1(inp):
    state, instructions = inp.split("\n\n")
    stacks = defaultdict(list)
    for s in reversed(state.replace("    ", " ").splitlines()[:-1]):
        crates = s.replace("[", "").replace("]", "").split(" ")
        for i, crate in enumerate((crates)):
            if crate:
                stacks[i + 1].append(crate)

    for ins in instructions.splitlines():
        move, frm, to = map(
            int,
            ins.replace("move ", "").replace(" from", "").replace(" to", "").split(" "),
        )
        for _ in range(0, move):
            crate = stacks[frm].pop(-1)
            stacks[to].append(crate)
    res = ""
    for stack in stacks.values():
        res += stack[-1]
    return res


def part2(inp):
    state, instructions = inp.split("\n\n")
    stacks = defaultdict(list)
    for s in reversed(state.replace("    ", " ").splitlines()[:-1]):
        crates = s.replace("[", "").replace("]", "").split(" ")
        for i, crate in enumerate((crates)):
            if crate:
                stacks[i + 1].append(crate)

    for ins in instructions.splitlines():
        move, frm, to = map(
            int,
            ins.replace("move ", "").replace(" from", "").replace(" to", "").split(" "),
        )
        crates = []
        for _ in range(0, move):
            crate = stacks[frm].pop(-1)
            crates.append(crate)
        for _ in range(0, move):
            stacks[to].append(crates.pop(-1))

    res = ""
    for stack in stacks.values():
        res += stack[-1]
    return res


assert (
    part1(
        """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    )
    == "CMZ"
)
aoc.submit_p1(part1(aoc.get_input_no_split()))

assert (
    part2(
        """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    )
    == "MCD"
)
aoc.submit_p2(part2(aoc.get_input_no_split()))
