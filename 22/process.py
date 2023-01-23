from collections import deque

maindeq = deque()
maintree = dict()

with open("qq.txt") as f:
    for line in f:
        sp = line.strip().replace("\"", "").replace(" ", "").split(";")[:-1]
        maindeq.append((int(sp[0]), int(sp[1]), [int(i) for i in sp[2:]]))

while len(maindeq) > 0:
    dep_times = []
    pid, time, deps = maindeq.popleft()
    if len(deps) == 1 and deps[0] == 0:
        maintree[pid] = (time, [])
        continue
    for i in deps:
        if i not in maintree.keys():
            maindeq.append((pid, time, deps))
            break
        dep_times.append(maintree[i][0])
    else:
        maintree[pid] = (time + max(dep_times), deps)