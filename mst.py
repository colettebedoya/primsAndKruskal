'''
Constructs the minimum spanning tree using both
Prim's and Kruskal's algorithms.

Usage:
    python mst.py [input file] [prims | kruskals]

Colette Bedoya
11/16/2015
'''

import sys
import heapq
from DisjointSet import DisjointSet
'''
An implementation of Prim's algorithm for finding
the MST of a connnected, weighted, undirected graph.
'''
def prims(inputFile):
    '''
    input file containing weighted graph

    file contents is
    [vertex 1] [vertex 2] [weight]
    '''
    graph = open(inputFile)

    '''
    an initially empty dictionary containing mapping
    [vertex]:[adjacency list]
    '''
    adjacency = { }
    unvisited_set = set()
    '''
    the collection of vertices (there may be duplicates)
    '''
    nodes = [ ]

    '''
    The following reads in the input file
    and constructs an adjacency list of
    the graph.
    '''
    for line in graph:
        entry = line.split()

        if entry[0] not in adjacency:
            adjacency[entry[0]] = []
            unvisited_set.add(entry[0])
        # construct an edge for the adjacency list
        edge = (entry[1], int(entry[2]))
        adjacency[entry[0]].append(edge)
        unvisited_set.add(entry[1])
        # add the nodes
        nodes.append(entry[0])
        nodes.append(entry[1])

    '''
    output the adjacency list
    '''
    for v in adjacency:
        print v, adjacency[v]

    '''
    Now construct the MST using Prim's algorithm:'''

    current_vertex = (0,nodes[0])
    distance = {nodes[0]:0}

    previous = {nodes[0]:'-'}
    solutions = {}
    unvisited = list(unvisited_set)
    queue = []
    for v in unvisited:
        solutions[v]= (0,'-')
    heapq.heappush(queue,current_vertex)
    unvisited.remove(nodes[0])
    cost = 1
    while queue:

        current_vertex = heapq.heappop(queue)
        adjacentVertex = adjacency.get(current_vertex[1], list())

        #adds vertices in heap
        for v in adjacentVertex:

        #checks to see if in unvisited list
            if v[0] in unvisited:
                heapq.heappush(queue,(v[1], v[0]))
                distance[v[0]]= v[1]
                previous[v[0]]=current_vertex[1]
                unvisited.remove(v[0])
                solutions[v[0]] = (v[1],v[0], current_vertex[1])

            else:
                if v[0] not in distance:
                    distance [v[0]] = sys.maxint
                if  v[1]<= distance [v[0]]:
                    distance [v[0]] = v[1]
                    previous [v[0]] = current_vertex[1]
                    solutions[v[0]] = (v[1],v[0], current_vertex[1])
                    cost += v[1]
    print "Prims total cost: %d with edges:" %(cost)
    return  solutions

'''
An implementation of Kruskal's algorithm for finding
the MST of a connnected, weighted, undirected graph.
'''
def kruskals(inputFile):
    graph = open(inputFile)
    edges = [ ]
    nodes = {}
    count = 0
    '''
    The following reads in the input file
    and constructs an adjacency list of
    the graph.
    '''
    for line in graph:
        entry = line.split()
        edges.append((entry[2],entry[0],entry[1]))
        if entry[0] not in nodes.keys():
            nodes[entry[0]]= count
            count = count + 1
    total = 0
    solutions =[]
    disjoint = DisjointSet(len(nodes))
    edges.sort()
    for edge in edges:
        if disjoint.find(nodes[edge[1]]) != disjoint.find(nodes[edge[2]]):
            if disjoint.find(nodes[edge[1]]) < disjoint.find(nodes[edge[2]]):
                disjoint.union(nodes[edge[1]], nodes[edge[2]])
            else:
                disjoint.union(nodes[edge[2]], nodes[edge[1]])
            solutions.append(edge)
            total += int(edge[0])
    return total, solutions

'''
The main function
'''

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Usage python mst1.py [input file] [prims | kruskals]'
        quit()

    if sys.argv[2] == 'prims':
        print prims(sys.argv[1])
    elif sys.argv[2] == 'kruskals':
        print kruskals(sys.argv[1])
    else:
        print 'Illegal algorithm. Must be either \'prims\' or \'kruskals\' '

