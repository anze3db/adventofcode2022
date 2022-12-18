from pathlib import Path

from rich import progress

from utils import AoC

aoc = AoC(day=int(Path(__file__).stem))
aoc.print_p1()


def dist(x, y):
    ax, bx = x
    ay, by = y
    return abs(ax - ay) + abs(bx - by)


# def lower_dist(dist, point):
#     """Returns all points that are closer than the distance"""
#     for i in range(dist):


def parse_inp(inp):
    for i in inp:
        sensor, beacon = (
            i.replace("Sensor at x=", "")
            .replace("closest beacon is at x=", "")
            .replace("y=", "")
            .split(":")
        )
        sensor = tuple(map(int, sensor.split(",")))
        beacon = tuple(map(int, beacon.split(",")))
        yield sensor, beacon, dist(sensor, beacon)


def part1(inp, y):
    sensors = set()
    beacons = set()
    sensor_beacon_dist = {}

    for s, b, d in parse_inp(inp):
        sensors.add(s)
        beacons.add(b)
        sensor_beacon_dist[s] = d
    mx = max([s[0] for s in sensors]) + 100
    nx = min([s[0] for s in sensors]) + 100
    my = max([s[1] for s in sensors])
    ny = min([s[1] for s in sensors])
    print(mx, nx)
    res = 0
    print(sensors)
    print(beacons)

    for j in [y]:
        for i in progress.track(range(-mx, mx * 1.5)):
            p = i, j
            if p in sensors:
                # print("S", end="")
                res += 1
            elif p in beacons:
                ...
                # print("B", end="")
                # res += 1
            else:
                s_set = False
                for s in sensors:
                    dist_to_sensor = dist(s, p)
                    # print(dist_to_sensor, sensor_beacon_dist[s])
                    if dist_to_sensor <= sensor_beacon_dist[s]:
                        s_set = True
                if s_set:
                    # print("#", end="")
                    res += 1
                # else:
                # print(".", end="")
        # print("")
    return res


######################


def part2(inp, mx):
    sensors = set()
    beacons = set()
    sensor_beacon_dist = {}

    for s, b, d in parse_inp(inp):
        sensors.add(s)
        beacons.add(b)
        sensor_beacon_dist[s] = d
    for i in progress.track(range(mx)):
        j = 0
        while j <= mx:
            if (i, j) in sensors or (i, j) in beacons:
                j += 1
                continue
            distances = [1]
            for sensor in sensors:
                dist_to_sensor = dist(sensor, (i, j))
                if dist_to_sensor <= sensor_beacon_dist[sensor]:
                    distances.append(sensor_beacon_dist[sensor] - dist_to_sensor)
            if len(distances) == 1:
                return i * 4000000 + j
            else:
                j += max(distances)


inp = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()
# assert (p1_res := part1(inp, y=10)) == 26, p1_res
# aoc.submit_p1(part1(aoc.get_input(), y=2000000))

assert (p2_res := part2(inp, 20)) == 56000011, p2_res
aoc.submit_p2(part2(aoc.get_input(), 4000000))
