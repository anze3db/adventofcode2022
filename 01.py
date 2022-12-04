from utils import console, get_input, submit

inp = get_input(2022, 1)
console.log(inp)

s = 0
elves = []
for i in inp:
    if i == "":
        elves.append(s)
        s = 0
        continue
    s += int(i)
res = max(elves)
submit(year=2022, day=1, level=1, answer=res)

res = sum(sorted(elves)[-3:])
submit(year=2022, day=1, level=2, answer=res)
