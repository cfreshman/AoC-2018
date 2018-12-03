import sys
with open(sys.argv[1]) as file:
    lines = file.read().splitlines()


# --- Part One ---
print(sum(int(line) for line in lines))

# --- Part Two ---
seen = set()
freq = 0
while freq not in seen:
    for line in lines:
        seen.add(freq)
        freq += int(line)
        if freq in seen:
            break
print(freq)
