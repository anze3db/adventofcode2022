import os
from datetime import datetime
from typing import Any

import percache
import requests
from bs4 import BeautifulSoup
from rich.console import Console

cache = percache.Cache(".cache", livesync=True)
console = Console()

AOC_URL = "https://adventofcode.com"
AOC_SESSION = os.getenv("AOC_SESSION")
assert (
    AOC_SESSION
), "Set AOC_SESSION env variable to your session cookie on adventofcode.com (export AOC_SESSION='your session cookie')"


class AoC:
    def __init__(self, day: int, year: int = datetime.now().year):
        console.log(f"Solving {day=} {year=}")
        self.day = day
        self.year = year

    def print_p1(self):
        console.log(get_puzzle(self.day, self.year, part=1))

    def print_p2(self):
        console.log(get_puzzle(self.day, self.year, part=2))

    def get_input(self):
        return get_input(year=self.year, day=self.day)

    def get_input_no_split(self):
        return get_input(year=self.year, day=self.day, no_split=True)

    def submit_p1(self, answer: Any):
        submit(year=self.year, day=self.day, level=1, answer=answer)
        self.print_p2()

    def submit_p2(self, answer: Any):
        submit(year=self.year, day=self.day, level=2, answer=answer)


@cache
def submit(year: int, day: int, level: int, answer: Any):
    console.log(f"Posting [bold]{answer}[/bold] for {day=} {level=}")
    result = requests.post(
        f"{AOC_URL}/{year}/day/{day}/answer",
        dict(level=level, answer=answer),
        cookies={"session": AOC_SESSION},
        timeout=10,
    )
    assert result.status_code == 200, result.text
    soup = BeautifulSoup(result.text, features="html.parser")
    console.log(soup.body.main.article.get_text())


@cache
def get_puzzle(day: int, year: int, part: int):
    result = requests.get(
        f"{AOC_URL}/{year}/day/{day}",
        cookies={"session": AOC_SESSION},
        timeout=10,
    )
    assert result.status_code == 200, result.text

    soup = BeautifulSoup(result.text, features="html.parser")

    return soup.body.main.findAll("article")[part - 1].get_text()


@cache
def get_input(year: int, day: int, no_split=False):
    console.log("Fetching from server")
    result = requests.get(
        f"{AOC_URL}/{year}/day/{day}/input",
        cookies={"session": AOC_SESSION},
        timeout=10,
    )
    assert result.status_code == 200, (f"{AOC_URL}/{year}/day/{day}/input", result.text)
    if no_split:
        return result.text
    return result.text.splitlines()
