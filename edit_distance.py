# Edit Distance Assignment
# Tony Silva CS 5970


def distance(b, a):
    # I do this just so I know I am consistent in my function and
    # the actions being performed.
    if len(b) < len(a):
        return distance(a, b)
    # Obviously, if a is empty we return the size of the
    # non empty string
    if len(a) == 0:
        return len(b)
    # declare size of list of lists
    m = len(b)+1
    n = len(a)+1
    # easier to implement with a list, in my opinion
    d = {}
    # initialize the list from 0 to m and n
    # this way if the word is cat the size of d will be from
    # 0, 1 , 2, 3
    for i in range(m):
        d[i, 0] = i
    for j in range(n):
        d[0, j] = j
    # create distance matrix numbers
    for i in range(1, m):
        for j in range(1, n):
            # if the lets are not equal then we need to add the minimum of the costs
            if b[i-1] == a[j-1]:
                d[i, j] = d[i-1, j-1]
            else:
                d[i, j] = min(d[i-1, j] + 1, d[i, j-1] + 1, d[i-1, j-1] + 1)
    # return the last entry of the dictionary
    return d[m-1, n-1]

