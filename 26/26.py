def archive(): #https://inf-ege.sdamgia.ru/problem?id=27423
    with open("26.txt") as file:
        s, n = [int(i) for i in file.readline().strip().split()]
        sizes = [int(line.strip()) for line in file.readlines()]
    sizes.sort()
    summ = 0
    count = 0
    for i in range(n):
        if summ + sizes[i] <= s:
            summ += sizes[i]
            count += 1
        else:
            break
    last_element = sizes[i-1]
    remainder = s - summ
    max_element = last_element
    for j in range(i,n):
        if sizes[j] - last_element <= remainder:
            max_element = sizes[j]
    print(count, max_element)


def cargo_truck(): #https://inf-ege.sdamgia.ru/problem?id=33198
    with open("26.txt") as file:
        n, m = [int(i) for i in file.readline().strip().split()]
        sizes = [int(line.strip()) for line in file.readlines()]
    priority = list(filter(lambda x: 200 <= x <= 210, sizes))
    other = list(filter(lambda x: x not in priority, sizes))
    other.sort()
    summ = sum(priority)
    count = len(priority)
    for i in range(len(other)):
        if summ + other[i] <= m:
            summ += other[i]
            count += 1
        else:
            break
    taken = other[:i].copy()
    not_taken = other[i:].copy()
    for j in range(i-1, 0, -1):
        last_element = taken[j]
        remainder = m - summ
        max_element = last_element
        for k in range(len(not_taken)):
            if not_taken[k] - last_element <= remainder:
                max_element = not_taken[k]
        taken[j] = max_element
        not_taken[j] = last_element
        summ += max_element - last_element
    print(count, summ)


def packing(): #https://inf-ege.sdamgia.ru/problem?id=47230
    with open("26.txt") as file:
        n = int(file.readline().strip())
        boxes = [int(line.strip()) for line in file.readlines()]
    boxes.sort(reverse=True)
    count = 1
    previous_box = boxes[0]
    for i in range(1,n):
        if previous_box - boxes[i] >= 3:
            previous_box = boxes[i]
            count += 1
    print(count, previous_box)


def trees(): #https://inf-ege.sdamgia.ru/problem?id=45260
    tree_rows = [[] for i in range(100000)]
    with open("26.txt") as file:
        n = int(file.readline().strip())
        data = [line.strip() for line in file.readlines()]
    for i in data:
        row, place = [int(j) for j in i.split()]
        tree_rows[row].append(place)
    max_row, min_place = 0, 0
    for i in range(len(tree_rows)):
        row = tree_rows[i]
        if len(row) < 2:
            continue
        row.sort(reverse=True)
        for j in range(len(row)-1):
            if row[j] - row[j+1] - 1 == 13:
                max_row, min_place = i, row[j+1] + 1
    print(max_row, min_place)


def experiment(): #https://inf-ege.sdamgia.ru/problem?id=46984
    with open("26.txt") as file:
        n = int(file.readline().strip())
        data = [line.strip() for line in file.readlines()]
    screen = [[] for i in range(10001)]
    for i in data:
        row, place = [int(j) for j in i.split()]
        screen[row].append(place)
    min_row, max_len = 0,0
    for i in range(len(screen)):
        row = list(set(screen[i]))
        row.sort()
        cnt = 1
        for j in range(len(row)-1):
            if row[j+1] - row[j] == 1:
                cnt += 1
                if cnt > max_len:
                    max_len = cnt
                    min_row = i
            else:
                cnt = 1
    print(max_len, min_row)


def buying_product_ab() #https://inf-ege.sdamgia.ru/problem?id=33528
    with open("26.txt") as file:
        n, m = [int(i) for i in file.readline().strip().split()]
        data = [line.strip().split() for line in file.readlines()]
    products_a, products_b = list(), list()
    for i in range(n):
        price, quantity, ptype = int(data[i][0]), int(data[i][1]), data[i][2]
        if ptype == "A":
            products_a.append((price, quantity))
        else:
            products_b.append((price, quantity))
    products_a.sort()
    products_b.sort()
    summ, count_a, count_b = 0, 0, 0

    for i in range(len(products_a)):
        price, quantity = products_a[i][0], products_a[i][1]
        if summ + price * quantity > m:
            if summ + price <= m:
                for j in range(quantity):
                    if summ + price > m:
                        break
                    else:
                        summ += price
                        count_a += 1
            break
        else:
            summ += price * quantity
            count_a += quantity

    for i in range(len(products_b)):
        price, quantity = products_b[i][0], products_b[i][1]
        if summ + price * quantity > m:
            if summ + price <= m:
                for j in range(quantity):
                    if summ + price > m:
                        break
                    else:
                        summ += price
                        count_b += 1
            break
        else:
            summ += price * quantity
            count_b += quantity
    print(count_b, m-summ)


def discount(): #https://inf-ege.sdamgia.ru/problem?id=29674
    from math import ceil
    with open("26.txt") as file:
        n = int(file.readline().strip())
        prices = [int(line.strip()) for line in file.readlines()]
    no_discount = list(filter(lambda x: x <= 50, prices))
    possible_discount = list(filter(lambda x: x > 50, prices))
    possible_discount.sort()
    discounted_items_count = len(possible_discount) // 2
    summ = sum(no_discount) + sum(possible_discount[discounted_items_count:])
    max_price = 0
    for i in range(discounted_items_count):
        new_price = possible_discount[i] * 0.75
        max_price = max(possible_discount[i], max_price)
        summ += new_price
    summ = ceil(summ)
    print(summ, max_price)