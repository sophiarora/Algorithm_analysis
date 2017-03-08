import random
eight_list = [[1, 2, 5, 6], [2, 1, 3, 5], [3, 2, 4, 8], [4, 3, 7, 8],
[8, 7, 3, 4], [7, 4, 8, 6], [6, 1, 5, 7], [5, 1, 2, 6]]

def algo_graph(array):
    if len(array) <= 2:
        return array
    for i in array:
        group_array(i)
    while len(array) > 2:
        s = random.choice(array)
        array.remove(s)
        edge = random.choice(s[1:len(s)])
        for element in array: #should never make the list rotating here
            if edge in element[0]:
                s2 = element
        new = contraction(s, s2)
        array.remove(s2)
        array.append(new)
    return array

def count_array(s):
    if len(s[0]) > len (s[1]):
        return len(s[0]) - 1
    else:
        return len(s[1]) - 1

def group_array(array):
    array[0] = [array[0]]
    return array

def contraction(s1, s2):
    """Do the contraction of graphs.

    >>> s1 = group_array([1, 2, 5, 6])
    >>> s2 = group_array([2, 1, 3, 5])
    >>> contraction(s1, s2)
    [[1, 2], 5, 6, 3]
    """
    new = [s1[0]+s2[0]]
    new += s1[1:len(s1)]
    for i in s2[1:len(s2)]: #ensure that edges in contraction is unique
        if i not in s1:
            new.append(i)
    for i in new[1:len(new)]:#ensure that the edge in s1 is removed
        if i in new[0]:
            new.remove(i)
    return new

file = open('graph_contraction.txt', 'r')
a = []
for line in file.readlines():
    a.append(line.split('\t'))
for i in range(0, 500):
    a_int = []
    for line in a:
        row = []
        for i in line:
            if i != '\n':
                row.append(int(i))
        a_int.append(row)
    new = a_int
    print(count_array(algo_graph(new)))
