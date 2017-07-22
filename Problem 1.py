# floyd-warshall algorithm taken from Dr. Varahan lecture. Also, with inspiration for the structure of the algorithm in python from codingjunkie
# note the structure that I learned to use from coding junkie was how to set up the undirected graph. It led me to the idea
# to use the graph as a dictionary - which in python is like a hashmap. key-value relationship
def algorithm(g):
    # since the graph is set up as a dictionary, the keys are the vertices
    vertices = g.keys()

    # this algorithm uses the reccurence for dij, thus this dictionary will be used to hold the values for shortest distance to each node
    dist = {}
    dist = g

    # simply find the smallest distance as we work through the nodes.
    # This algorithm is the one found on the online lecture about Floyd-Warshall - last slide.
    for v in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][v] + dist[v][j] < dist[i][j]:
                    dist[i][j] = dist[i][v]+dist[v][j]

    return dist


#### MAIN ######
# set up the graph with the nodes and their weights, note this is a dictionary
undirected_graph = {
         'A':{'A':0,'B':2,'C':float('inf'),'D':float('inf'),'E':float('inf'),'F':3,'G':float('inf'),'H':float('inf')},
         'B':{'A':2,'B':0,'C':5,'D':float('inf'),'E':4,'F':float('inf'),'G':3,'H':float('inf')},
         'C':{'A':float('inf'),'B':5,'C':0,'D':float('inf'),'E':2,'F':float('inf'),'G':float('inf'),'H':4},
         'D':{'A':float('inf'),'B':float('inf'),'C':float('inf'),'D':0,'E':2,'F':4,'G':2,'H':float('inf')},
         'E':{'A':float('inf'),'B':4,'C':2,'D':2,'E':0,'F':float('inf'),'G':float('inf'),'H':3},
         'F':{'A':3,'B':float('inf'),'C':float('inf'),'D':4,'E':float('inf'),'F':0,'G':1,'H':float('inf')},
         'G':{'A':float('inf'),'B':3,'C':float('inf'),'D':2,'E':float('inf'),'F':1,'G':0,'H':1},
         'H':{'A':float('inf'),'B':float('inf'),'C':4,'D':float('inf'),'E':3,'F':float('inf'),'G':1,'H':0}
            }

# now we have our distance matrix
distance = algorithm(undirected_graph)

# simply print the result to get the shortest path.
for key,tuple in distance.iteritems():
    print key, tuple