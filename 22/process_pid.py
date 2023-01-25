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
pids = dict()
forbiden = [16, ]# поменять на индекс из задачи
allowed = []
# 18 процесс

with open("22.csv") as f:
    s = reader(f, delimiter=';', quotechar='"')
    next(s)
    for line in f:
        sp = line.strip().replace("\"", "").replace(" ", "").split(";")
        maindeq.append([int(sp[0]), int(sp[1]), [int(i) for i in sp[2:]]])
        allowed.append(int(sp[0]))
        for j in [int(i) for i in sp[2:]]:
            if j not in pids.keys():
                pids[j] = [int(sp[0])]
            else:
                pids[j].append(int(sp[0]))
allowed = set(allowed)
sortdeq = deque()
if 16 in pids.keys(): # поменять на индекс из задачи
    sortdeq = deque([16])# поменять на индекс из задачи
while len(sortdeq) > 0:
    tmp = sortdeq.popleft()
    forbiden.extend(pids[tmp]) # ВАЖНО именно extend не append
    for i in pids[tmp]:
        if i in pids.keys():
            sortdeq.append(i)

allowed = allowed.difference(set(forbiden))

copy_deq = deepcopy(maindeq)

for i in allowed:
    maindeq[15][2] = [i] # здесь ОЧЕНЬ ВНИМАТЕЛЬНО, там где первые скобки убедитесь что это именно нужный инжекс
    fill_tree(maindeq, maintree)
    if get_min_time(maintree) == 138:
        print(i)
        break
    else:
        maindeq = deepcopy(copy_deq)
        maintree = dict()