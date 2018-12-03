import sys
with open(sys.argv[1]) as file:
    lines = file.read().splitlines()

from collections import Counter


# --- Part One ---
two_count, three_count = 0, 0
for line in lines:
    counts = Counter(list(line)).items()
    if any(letter for (letter, count) in counts if count == 2):
        two_count += 1
    if any(letter for (letter, count) in counts if count == 3):
        three_count += 1
print(two_count * three_count)

# --- Part Two ---
seen = set()
for line in lines:
    new = set()
    for i in range(len(line)):
        variant = line[:i] + line[i+1:]
        if variant in seen:
            print(variant)
            exit(0)
        new.add(variant)
    seen |= new
