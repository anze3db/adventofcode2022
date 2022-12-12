import heapq
import math
from collections import defaultdict
from pathlib import Path
from string import ascii_lowercase

from utils import AoC

aoc = AoC(day=int(Path(__file__).stem))
aoc.print_p1()


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def dijkstra(start, end, grid):
    dist = defaultdict(lambda: math.inf)
    dist[start] = 0
    visited = set()
    queue = [(0, start)]
    while end not in visited:
        try:
            _, nex = heapq.heappop(queue)
        except IndexError:
            return math.inf
        visited.add(nex)
        for n in [
            add(nex, (1, 0)),
            add(nex, (-1, 0)),
            add(nex, (0, 1)),
            add(nex, (0, -1)),
        ]:
            if n in visited:
                continue
            if n not in grid:
                continue
            if grid[n] > (grid[nex] + 1):
                # Too high
                continue

            if dist[n] > dist[nex] + 1:
                dist[n] = dist[nex] + 1
                heapq.heappush(queue, (dist[nex] + 1, n))
    return dist[end]


def part1(inp):
    start = None
    end = None
    grid = {}

    for y, i in enumerate(inp):
        for x, j in enumerate(i):
            if j == "S":
                start = (x, y)
                grid[(x, y)] = ascii_lowercase.index("a")
            elif j == "E":
                end = (x, y)
                grid[(x, y)] = ascii_lowercase.index("z")
            else:
                grid[(x, y)] = ascii_lowercase.index(j)
    return dijkstra(start, end, grid)


def part2(inp):
    end = None
    grid = {}
    starts = []
    for y, i in enumerate(inp):
        for x, j in enumerate(i):
            if j == "S" or j == "a":
                starts.append((x, y))
                grid[(x, y)] = ascii_lowercase.index("a")
            elif j == "E":
                end = (x, y)
                grid[(x, y)] = ascii_lowercase.index("z")
            else:
                grid[(x, y)] = ascii_lowercase.index(j)
    return min(dijkstra(start, end, grid) for start in starts)


assert (
    part1(
        """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()
    )
    == 31
)
aoc.submit_p1(part1(aoc.get_input()))

assert (
    part2(
        """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()
    )
    == 29
)
aoc.submit_p2(part2(aoc.get_input()))
