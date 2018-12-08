import sys
with open(sys.argv[1]) as file:
    lines = file.read().splitlines()

from collections import namedtuple
Node = namedtuple('Node', 'n_c n_m children metadata')


data = [int(x) for x in lines[0].split()]

metadata_sum = 0
# returns [node, next index]
def read_node(index):
    n_c, n_m, children, metadata = data[index], data[index+1], [], []
    node = Node(n_c, n_m, children, metadata)

    index += 2
    for c in range(n_c):
        [child, index] = read_node(index)
        node.children.append(child)

    node.metadata.extend(data[index:index+n_m])
    index += n_m

    global metadata_sum
    metadata_sum += sum(node.metadata)

    return node, index

# --- Part 1 ---
[root, _] = read_node(0)
print(metadata_sum)

# --- Part 2 ---
def get_value(node):
    if not node.children:
        return sum(node.metadata)

    return sum(get_value(node.children[i-1]) for i in node.metadata if i > 0 and i <= node.n_c)

print(get_value(root))
