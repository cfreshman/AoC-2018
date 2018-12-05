import sys
with open(sys.argv[1]) as file:
    lines = file.read().splitlines()


diff = abs(ord('a') - ord('A'))

# --- Part One ---
line = lines[0]
prev_len = None
while len(line) != prev_len:
    prev_len = len(line)
    for i in range(len(line)-2, -1, -1):
        if i < len(line)-1 and abs(ord(line[i]) - ord(line[i+1])) == diff:
            line = line[:i] + line[i+2:]
print(len(line))

# --- Part Two ---
line = lines[0]
min_len = len(line)
for type in set(line.lower()):
    removed = line.replace(type, '').replace(type.upper(), '')
    prev_len = None
    while len(removed) != prev_len:
        prev_len = len(removed)
        for i in range(len(removed)-2, -1, -1):
            if i < len(removed)-1 and abs(ord(removed[i]) - ord(removed[i+1])) == diff:
                removed = removed[:i] + removed[i+2:]
    min_len = min(min_len, len(removed))
print(min_len)
