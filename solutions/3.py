import sys
with open(sys.argv[1]) as file:
    lines = file.read().splitlines()

import re
import itertools

fabric = {}
overlaps = 0
intact = set()
for line in lines:
    id, x, y, w, h = map(int, re.match('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line).groups())

    intact.add(id)
    for coords in itertools.product(range(x, x+w), range(y, y+h)):
        if not coords in fabric:
            fabric[coords] = id
        else:
            overlaps += 1
            intact -= {id, fabric[coords]}

# --- Part One ---
print(overlaps)

# --- Part Two ---
print(intact.pop())
