line = None
def read_line():
    global line
    try:
        line = input()
    except:
        line = None
    return line

lines = []
while read_line() != None:
    lines.append(line)

# part 1
print(sum(int(line) for line in lines))

# part 2
seen = set()
freq = 0
while freq not in seen:
    for line in lines:
        seen.add(freq)
        freq += int(line)
        if freq in seen:
            break
print(freq)
