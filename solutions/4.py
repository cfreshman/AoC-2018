import sys
with open(sys.argv[1]) as file:
    lines = file.read().splitlines()

import re
import datetime

records = []
sleeps = {}
for line in lines:
    timestamp, desc = re.match('\[(.*)\] (.*)', line).groups()
    year, month, day, hour, minute = map(int, re.match('(\d{4})-(\d\d)-(\d\d) (\d\d):(\d\d)', timestamp).groups())
    dt = datetime.datetime(year, month, day, hour, minute)

    if 'Guard' in desc:
        gid = int(re.search('#(\d+)', desc).group(1))
        records.append(([dt, 0, gid]))
        if gid not in sleeps:
            sleeps[gid] = [0]*60
    elif 'falls asleep' in desc:
        records.append([dt, 1])
    elif 'wakes up' in desc:
        records.append([dt, 2])

records.sort(key=lambda r: r[0])

guard = None
start = None
for record in records:
    if record[1] == 0:
        guard = record[2]
    elif record[1] == 1:
        start = record[0].minute
    else:
        for i in range(start, record[0].minute):
            sleeps[guard][i] += 1

# --- Part One ---
guard = max(sleeps.items(), key=lambda elem: sum(elem[1]))[0]
minute = max(enumerate(sleeps[guard]), key=lambda elem: elem[1])[0]
print(guard * minute)

# --- Part Two ---
guard = max(sleeps.items(), key=lambda elem: max(elem[1]))[0]
minute = max(enumerate(sleeps[guard]), key=lambda elem: elem[1])[0]
print(guard * minute)