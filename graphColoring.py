#Written by Adriene Cuenco

#!/usr/bin/python
#Python Version: 3.3.6
#Compile and run with python graphColoring.py
 
#Explores the tradeoffs between two algorithms to solve the graph coloring problem
#   1) dfs-based greedy algorithm --->Tradeoffs: Colors used is beyond the chromatic index
#   2) backtracking method----------->Tradeoffs: Nodes generated in the state space tree is excessive
#                                                resulting in slower calculations
#Input:  The order of a graph to be randomly created and tested.
#Output: Returns the number of colors used for the greedy algorithm.
#        Also, returns the amount of nodes created from the backtracking algorithm.
from random import randint
import math
#Random graph has the following properties: undirected, a chromatic index of d, size m and order n.
def generateRandomGraph(n,m,d):
    graph = []
    edges = []
    preColorVertex =[0]*n
    #pre-color vertices to ensure chromatic index d
    j=1
    for i in range(n):
        if j is 8:
            j=1
        preColorVertex[i] = j
        j=j+1
    for i in range(m):
        prospectEdge = generateEdge(n)
        #if prospect edge already exists or edge connects two of the same colors, keep generating new edge
        while preColorVertex[prospectEdge[0]-1] is preColorVertex[prospectEdge[1]-1] or contains(prospectEdge,edges):
            prospectEdge = generateEdge(n)
        edges.append(prospectEdge)
    #Create neighbors from generated edges.
    for i in range(1,n+1):
        neighbors =[]
        for edge in edges:
            if edge[0] is i:
                neighbors.append(edge[1])
            if edge[1] is i:
                neighbors.append(edge[0])
        graph.append(neighbors)
    return graph;
#-------------------------------------------
def contains(edge,edges):
    if edge in edges:
        return True
    edge.reverse()
    if edge in edges:
        return True
    return False
#-------------------------
def generateEdge(order):
    edge = []
    firstVertex = randint(1,order)
    secondVertex = randint(1,order)
    #Exclude edges that connect the same vertex
    while firstVertex is secondVertex:
        firstVertex = randint(1,order)
        secondVertex = randint(1,order)
    edge.append(firstVertex)
    edge.append(secondVertex)
    return edge;
#----------------------------------------
def colorMeGreedyDFS(graph):
    coloredVerticies = [0]*(len(graph))
    currentVertex = 0
    for neighbors in graph:
        neighCol = []
        color = 0
        for i in neighbors:
            neighCol.append(coloredVerticies[i-1])
        while color in neighCol:
            color+=1
        coloredVerticies[currentVertex]= color
        currentVertex+=1
    return max(coloredVerticies) + 1
#----------------------------------------
def findMaxColors(order):
    maximum = 0
    d = 7
    for i in range(1, 11):
        n=order
        if n == 10:
            maxEdges=n * int(math.log(n ,10))
        else:
            maxEdges= (5*n) * int(math.log(n,10))
        graph = generateRandomGraph(n,maxEdges,d)
        maxColor=colorMeGreedyDFS(graph)
        if maxColor > maximum:
            maximum = maxColor
    print("order is " + str(n))
    print("Maximum colors used is " + str(maximum))
    return
#----------------------------------------
def colorMeBacktrack(graph):
    w = makeBacktrackGraph(graph);
    vcolor = [1] * (len(graph))
    #edit start
    #m_coloring(0,w,vcolor)
    for i in range(1,order+1):
        if done:
            return
        #record option
        if option is feasible:
            if soultion is found:
                done = True
                record solution
            else:
                m_coloring()
    #edit end
    return nodeCount
#----------------------------------------
def m_coloring(i,w,vcolor):
    global nodeCount
    global solutionFound
    n = len(vcolor)
    if promising(i,w,vcolor):
        if i is n-1:
            nodeCount+=n
            solutionFound = True
        else:
            for color in range(1,d+1):
                if solutionFound:
                    solutionFound = False
                    break
                vcolor[i+1] = color
                nodeCount+=1
                m_coloring(i+1,w,vcolor)
    nodeCount+=1
#----------------------------------------
def promising(i,w,vcolor):
    switch = True
    j = 1
    while j < i and switch:
        if w[i][j] and vcolor[i] is vcolor[j]:
            switch = False
        j+=1
    return switch
#------------------------------------------
def makeBacktrackGraph(graph):
    n = len(graph)
    w =[[False for x in range(n)] for y in range(n)]
    currentVertex = 0
    for neighbors in graph:
        for i in neighbors:
            w[currentVertex][i-1] = True
        currentVertex+=1
    return w
#------------------------------------------
def findAvgNodes(n):
    global d
    d = 7
    avg = 0
    for i in range(1,11):
        if n <= 10:
            maxEdges=int(n * math.log10(n))
        else:
            maxEdges= int((5*n) * math.log10(n))
        graph = generateRandomGraph(n,maxEdges,d)
        avg+=colorMeBacktrack(graph)
    avg = int(avg / n)
    print("order is " + str(n))
    print("Avg Nodes = " + str(avg))
    return
#*********************************************
print("****Greedy results****")
#findMaxColors(10)
#findMaxColors(20)
#findMaxColors(50)
#findMaxColors(100)
#findMaxColors(200)
#findMaxColors(400)
#findMaxColors(500)
#findMaxColors(1000)
 
solutionFound = False
print()
print("****Backtrack results*******")
nodeCount= 0
findAvgNodes(5)
 
#nodeCount = 0
#findAvgNodes(6)
 
#nodeCount = 0
#findAvgNodes(7)
 
#nodeCount = 0
#findAvgNodes(8)
 
#nodeCount = 0
#findAvgNodes(9)
 
#nodeCount = 0
#findAvgNodes(10)


