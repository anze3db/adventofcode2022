import math
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from rich.progress import track

from utils import AoC

aoc = AoC(day=int(Path(__file__).stem))
aoc.print_p1()


@dataclass
class Monkey:
    items: list[int]
    operation: Callable[[int], int]
    test: int
    if_true: int
    if_false: int
    num_inspected: int = 0


monkeys = [
    Monkey(
        items=[65, 78],
        operation=lambda old: old * 3,
        test=5,
        if_true=2,
        if_false=3,
    ),
    Monkey(
        items=[54, 78, 86, 79, 73, 64, 85, 88],
        operation=lambda old: old + 8,
        test=11,
        if_true=4,
        if_false=7,
    ),
    Monkey(
        items=[69, 97, 77, 88, 87],
        operation=lambda old: old + 2,
        test=2,
        if_true=5,
        if_false=3,
    ),
    Monkey(
        items=[99],
        operation=lambda old: old + 4,
        test=13,
        if_true=1,
        if_false=5,
    ),
    Monkey(
        items=[60, 57, 52],
        operation=lambda old: old * 19,
        test=7,
        if_true=7,
        if_false=6,
    ),
    Monkey(
        items=[91, 82, 85, 73, 84, 53],
        operation=lambda old: old + 5,
        test=3,
        if_true=4,
        if_false=1,
    ),
    Monkey(
        items=[88, 74, 68, 56],
        operation=lambda old: old * old,
        test=17,
        if_true=0,
        if_false=2,
    ),
    Monkey(
        items=[54, 82, 72, 71, 53, 99, 67],
        operation=lambda old: old + 1,
        test=19,
        if_true=6,
        if_false=0,
    ),
]


def part1(inp):
    rounds = 20
    for i in range(rounds):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.num_inspected += 1
                new_item = monkey.operation(item) // 3
                if new_item % monkey.test == 0:
                    monkeys[monkey.if_true].items.append(new_item)
                else:
                    monkeys[monkey.if_false].items.append(new_item)
            monkey.items = []
    srt = sorted([monkey.num_inspected for monkey in monkeys])
    return srt[-1] * srt[-2]


def part2(inp):
    rounds = 10000
    cap = math.prod({monkey.test for monkey in monkeys})
    for i in track(range(rounds)):
        for monkey in monkeys:
            monkey.num_inspected += len(monkey.items)
            op = monkey.operation
            test = monkey.test
            new_items = [op(item) % cap for item in monkey.items]
            first_monkey = [item for item in new_items if item % test == 0]
            second_monkey = [item for item in new_items if item % test != 0]
            monkeys[monkey.if_true].items += first_monkey
            monkeys[monkey.if_false].items += second_monkey
            monkey.items = []
    srt = sorted([monkey.num_inspected for monkey in monkeys])
    return srt[-1] * srt[-2]


aoc.submit_p1(part1(aoc.get_input()))
aoc.submit_p2(part2(aoc.get_input()))
