import collections
import math
import random
import copy

def remove_all(y,fromlist):
    for x in fromlist:
        print(x)
        if x == y: fromlist.remove(y)

def replace_all(x,y,fromlist):
    for z in fromlist:
        if z == x:
            fromlist.remove(x)
            fromlist.append(y)

def edgeContraction(dic, nodeA, nodeB):
    dic[nodeA] = dic[nodeA] + dic[nodeB]
    dic.pop(nodeB)
    # Cleanup of loopback nodes
    for i in dic:
        for j in range(len(dic[i])):
            if dic[i][j] == nodeB:
                 dic[i][j] = nodeA
    dic[nodeA] = list(filter(lambda x: x != nodeA, dic[nodeA]))

    return dic

def findMinCut(dic):
    if len(dic) == 2:
        return len(list(dic.values())[0])
    else:
        nodeA = random.choice(list(dic.keys()))
        nodeB = random.choice(dic[nodeA])
        findMinCut(edgeContraction(dic, nodeA, nodeB))
        return len(list(dic.values())[0])

if __name__=="__main__":
    with open("graph_contraction.txt", 'r') as f:
        original_graph = {}
        for line in f:
            dic = list(map(int,line.strip().split("\t")))
            original_graph[dic.pop(0)] = dic

    i = 0
    length = len(original_graph)
    mincuts = length**2

    while i < length**2*math.log(length):
        graph = copy.deepcopy(original_graph)
        newMinCut = findMinCut(graph)
        if newMinCut < mincuts:
            mincuts = newMinCut
            print(mincuts)
        i += 1
