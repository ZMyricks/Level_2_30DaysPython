#  Depth First Search (A recursive approach)
# recursion calls the function within itself

'''
define the graph as an adjacency list
adjacency list = a way for representing a graph.
efficient in terms of space / only have to store the edges for a given node
'''
myGraph = {
  '1' : ['6','8'],
  '6' : ['5', '7'],
  '8' : ['4'],
  '5' : ['7'],
  '7' : ['5'],
  '4' : []
}

# declare a set to track all visited vertices
traversed = set()
def DFS(traversed, graph, vertex):
  if vertex not in traversed:
    # if not traversed, print and add to traversed set
    print (vertex)
    traversed.add(vertex)
    for adjacent in graph[vertex]:
      DFS(traversed, graph, adjacent)

# call function and specify the root vertex
print("Depth First Search:")
DFS(traversed, myGraph, '1')
