from dataclasses import dataclass
from pathlib import Path
from typing import Self

from utils import AoC

aoc = AoC(day=int(Path(__file__).stem))
aoc.print_p1()


@dataclass
class File:
    name: str
    size: int


class Dir:
    def __init__(self, name: str, parent: Self | None):
        self.name = name
        self.parent = parent
        self.files: list[File] = []
        self.dirs: list[Dir] = []
        self.sum_files = None

    def get_size(self):
        if self.sum_files is not None:
            return self.sum_files

        files = sum(f.size for f in self.files)
        dirs = sum(d.get_size() for d in self.dirs)
        self.sum_files = files + dirs
        return self.sum_files

    def __str__(self):
        return f"Dir({self.name=}, {self.sum_files=})"

    def __repr__(self) -> str:
        return self.__str__()


def run_commands(inp):
    root = current_path = Dir("/", None)
    root.parent = root
    dirs = [root]

    for i, cmd in enumerate(inp):
        if cmd[0] != "$":
            continue
        cmd, *arg = cmd.replace("$ ", "").split(" ")
        match cmd, arg:
            case ("cd", [".."]):
                current_path = current_path.parent
            case ("cd", ["/"]):
                current_path = root
            case ("cd", [dr]):
                current_path = next(d for d in current_path.dirs if d.name == dr)
                dirs.append(current_path)
            case ("ls", _):
                for j in range(len(inp) - i - 1):
                    curr_file = inp[i + j + 1].split(" ")
                    if curr_file[0] == "$":
                        break
                    size_or_dir, name = curr_file
                    if size_or_dir == "dir":
                        current_path.dirs.append(Dir(name, current_path))
                        continue
                    current_path.files.append(File(name, int(size_or_dir)))

    res = 0
    for d in dirs:
        s = d.get_size()
        if s <= 100000:
            res += s
    target = 30000000 - (70000000 - root.get_size())

    return res, min([d.get_size() for d in dirs if d.get_size() >= target])


def part1(inp):
    return run_commands(inp)[0]


def part2(inp):
    return run_commands(inp)[1]


assert (
    part1(
        """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()
    )
    == 95437
)
aoc.submit_p1(part1(aoc.get_input()))

assert (
    part2(
        """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()
    )
    == 24933642
)
aoc.submit_p2(part2(aoc.get_input()))
