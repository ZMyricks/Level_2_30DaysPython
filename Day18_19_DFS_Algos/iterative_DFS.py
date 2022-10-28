#  Depth First Search (iterative approach) (A non-recursive approach)
# using a loop to iterate over the graph's vertices.
# keep a stack of unvisited vertices

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


def DFS(graph, root_node):
  traversed = [root_node] # traverse root node
  stack = [root_node] # push it into the stack
  while stack:
    # while stack not empty / look at top vertex in stack / if not traversed, it will be
    vertex = stack[-1]
    if vertex not in traversed:
      traversed.extend(vertex)
    pop = True
    for adjacent in graph[vertex]:
      # read adjacent vertex of recently traversed vertex, and push to stack if not traversed
      if adjacent not in traversed:
        stack.extend(adjacent)
        pop = False
        break
    if pop:
      stack.pop()
  return traversed

print (DFS(myGraph, '1'))
