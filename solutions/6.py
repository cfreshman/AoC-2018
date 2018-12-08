import sys
with open(sys.argv[1]) as file:
    lines = file.read().splitlines()


points = []
for (i, line) in enumerate(lines):
    x, y = map(int, line.split(', '))
    points.append([i, x, y])

def man_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# --- Part One ---
areas = {}
infinite = set()
mins = [min(p[i] for p in points) for i in [1, 2]]
maxs = [max(p[i] for p in points) for i in [1, 2]]
for x in range(mins[0], maxs[0]+1):
    for y in range(mins[1], maxs[1]+1):
        closest = sorted(points, key=lambda p: man_dist(x, y, p[1], p[2]))
        if man_dist(x, y, closest[0][1], closest[0][2]) != man_dist(x, y, closest[1][1], closest[1][2]):
            i = closest[0][0]
            areas[i] = areas.get(i, 0) + 1
            if x in [mins[0], maxs[0]] or y in [mins[1], maxs[1]]:
                infinite.add(i)

largest = max(area for (i, area) in areas.items() if not i in infinite)
print(largest)

# --- Part Two ---
region_size = 0
for x in range(mins[0], maxs[0]+1):
    for y in range(mins[1], maxs[1]+1):
        total_dist = sum(man_dist(x, y, p[1], p[2]) for p in points)
        if total_dist < 10000:
            region_size += 1
print(region_size)
