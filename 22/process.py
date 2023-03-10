from collections import deque
from csv import reader

def fill_tree(maindeq, maintree):
    while len(maindeq) > 0:
        dep_times = []
        pid, time, deps = maindeq.popleft()
        if len(deps) == 1 and deps[0] == 0:
            maintree[pid] = (time, [])
            continue
        else:
            for i in deps:
                if i not in maintree.keys():
                    maindeq.append((pid, time, deps))
                    break
                dep_times.append(maintree[i][0])
            else:
                maintree[pid] = (time + max(dep_times), deps)

maindeq = deque()
maintree = dict()


with open("йцййц.csv") as f:
    s = reader(f, delimiter=';', quotechar='"')
    next(s)
    for line in f:
        sp = line.strip().replace("\"", "").replace(" ", "").split(";")
        maindeq.append((int(sp[0]), int(sp[1]), [int(i) for i in sp[2:]]))

fill_tree(maindeq, maintree)

m = -1
for i in maintree:
    m = max(maintree[i][0], m)

print(m)