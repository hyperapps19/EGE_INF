from collections import deque
from csv import reader
from copy import deepcopy

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


def get_min_time(maintree):
    m = -1
    for i in maintree:
        m = max(maintree[i][0], m)

    return m

maindeq = deque()
maintree = dict()

with open("22-32.csv") as f:
    s = reader(f, delimiter=';', quotechar='"')
    next(s)
    for line in f:
        sp = line.strip().replace("\"", "").replace(" ", "").split(";")
        maindeq.append([int(sp[0]), int(sp[1]), [int(i) for i in sp[2:]]])

copy_deq = deepcopy(maindeq)
# время меняется у 13 пида
for i in range(1, 100):
    maindeq[15][1] = i # здесь ОЧЕНЬ ВНИМАТЕЛЬНО, там где первые скобки убедитесь что это именно нужный инжекс
    fill_tree(maindeq, maintree)
    if get_min_time(maintree) >= 134:
        print(i)
        break
    else:
        maindeq = deepcopy(copy_deq)
        maintree = dict()

