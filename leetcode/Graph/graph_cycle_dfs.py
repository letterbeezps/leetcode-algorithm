# python program to detect cycle in an undirected graph

from collections import defaultdict

# this class represents a undirected graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # numbers of vertices
        self.graph = defaultdict(list)  # default a dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    # a recursive function that use visited[] and parent to detect
    # cycle in subgraph reachable from vertex v
    def isCycleUtil(self, v, visited, parent, cycle):
        if visited[v] == True:
            cycle.append(v)
            # Marked the current node as visited
        else:
            visited[v] = True

        # recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            # if the node is not visited the recurse on it
            if visited[i] == False:
                if(self.isCycleUtil(i, visited, v, cycle)):
                    # print(i)
                    # if v == 0:
                        #print(v)
                    if (len(cycle) <= 1 or cycle[0] != cycle[-1]):
                        cycle.append(v)
                    return True
            # if an adjacent vertex is visited and not parent of current vertex,
            # then there is a cycle
            elif parent != i:
                cycle.append(i)
                if (len(cycle) <= 1 or cycle[0] != cycle[-1]):
                    cycle.append(v)
                return True
        return False

    # return true if the graph contains a cycle, else false
    def isCycleic(self):
        cycle = []
        # marked all the vertices as not visited
        visited = [False] * (self.V)
        # call the recursive helper function to detect cycle in different
        # DFS tree
        for i in range(self.V):
            if visited[i] == False:
                if (self.isCycleUtil(i, visited, -1, cycle)) == True:
                    print(cycle)
                    return True
        return False



# create a graph
g = Graph(6)
g.addEdge(0, 1)
# g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(2, 5)
g.addEdge(4, 5)


if g.isCycleic():
    print ('yes')
else:
    print ('no cycle')

# print(g.graph.items())