import sys
with open(sys.argv[1]) as file:
    lines = file.read().splitlines()

import re
import heapq


# --- Part One ---
unblocks = {}
requires = {}
waiting = set()
for line in lines:
    first, second = re.match('Step (.) must be finished before step (.) can begin', line).groups()
    unblocks[first] = unblocks.get(first, []) + [second]
    requires[second] = requires.get(second, 0) + 1
    waiting.add(second)

ready = list(set(unblocks.keys()) - waiting)
heapq.heapify(ready)

order = ''
while ready:
    step = heapq.heappop(ready)
    order += step
    if step in unblocks:
        for unblocked in unblocks[step]:
            requires[unblocked] -= 1
            if requires[unblocked] == 0:
                heapq.heappush(ready, unblocked)
print(order)

# --- Part Twp ---
unblocks = {}
requires = {}
waiting = set()
for line in lines:
    first, second = re.match('Step (.) must be finished before step (.) can begin', line).groups()
    unblocks[first] = unblocks.get(first, []) + [second]
    requires[second] = requires.get(second, 0) + 1
    waiting.add(second)

ready = list(set(unblocks.keys()) - waiting)
heapq.heapify(ready)

waiting |= set(ready)

time = 0
workers = 5
tasks = []
while waiting:
    tasks = [t for t in tasks if t[1] in waiting]
    for t in tasks:
        if t[0] == time:
            done = t[1]
            workers += 1
            waiting.remove(done)
            if done in unblocks:
                for unblocked in unblocks[done]:
                    requires[unblocked] -= 1
                    if requires[unblocked] == 0:
                        heapq.heappush(ready, unblocked)

    while ready and workers:
        workers -= 1
        step = heapq.heappop(ready)
        task = [time + (ord(step) - ord('A') + 61), step]
        tasks.append(task)

    time += 1

print(time - 1)