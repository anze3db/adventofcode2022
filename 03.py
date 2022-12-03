from collections import Counter

from utils import console, get_input, submit

cnt = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part1(inp):
    res = 0
    for i in inp:
        ln = len(i) // 2
        c = set(i[:ln]).intersection(set(i[ln:])).pop()
        res += cnt.index(c)
    return res


def part2(inp):
    res = 0
    for i in range(0, len(inp), 3):
        c = (
            set(inp[i])
            .intersection(set(inp[i + 1]))
            .intersection(set(inp[i + 2]))
            .pop()
        )
        res += cnt.index(c)
    return res


assert (
    part1(
        """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()
    )
    == 157
)
console.log(part1(get_input(3)))
submit(day=3, level=1, answer=part1(get_input(3)))

assert (
    part2(
        """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()
    )
    == 70
)
console.log(part2(get_input(3)))
submit(day=3, level=2, answer=part2(get_input(3)))
