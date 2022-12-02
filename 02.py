from utils import console, get_input, submit


def part1(inp):
    res = 0
    score = {"X": 1, "Y": 2, "Z": 3}
    for i in inp:
        opponent, me = i.split(" ")
        res += score[me]
        match (opponent, me):
            case ("A", "Y") | ("B", "Z") | ("C", "X"):
                # Wins
                res += 6
            case ("A", "X") | ("B", "Y") | ("C", "Z"):
                # Ties
                res += 3
    return res


def part2(inp):
    res = 0
    score = {"X": 0, "Y": 3, "Z": 6}
    scoreP = {"A": 1, "B": 2, "C": 3}
    wins = {"A": "B", "B": "C", "C": "A"}
    looses = {"A": "C", "B": "A", "C": "B"}
    for i in inp:
        opponent, me = i.split(" ")
        res += score[me]
        match me:
            case "Y":
                res += scoreP[opponent]
            case "X":
                res += scoreP[looses[opponent]]
            case "Z":
                res += scoreP[wins[opponent]]
    return res


assert (
    part1(
        """A Y
B X
C Z""".splitlines()
    )
    == 15
)
console.log(part1(get_input(2)))
# submit(day=2, level=1, answer=part1(get_input(2)))

assert (
    part2(
        """A Y
B X
C Z""".splitlines()
    )
    == 12
)
console.log(part2(get_input(2)))
# submit(day=2, level=2, answer=part2(get_input(2)))
