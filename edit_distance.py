def distance(b, a):
    a = a.lower()
    b = b.lower()
    if len(b) < len(a):
        return distance(a, b)
    if len(a) == 0:
        return len(b)
    # declare size of list of lists
    d = [[0 for x in range(len(a))] for y in range(len(b))]
    for i in range(len(b)):
        d[i][0] = i
    for j in range(len(a)):
        d[0][j] = j
    # create distance matrix numbers
    for i in range(len(b)):
        for j in range(len(a)):
            if b[i] == a[j]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + 1)
    return d[-1][-1]

a = 'dog'
b = 'doggie'
count = distance(b, a)
print(count)
