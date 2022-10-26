theTree = {
  '5' : ['2','9'],
  '2' : ['3', '7'],
  '9' : ['6'],
  '3' : [],
  '7' : ['6'],
  '6' : []
}

visited_nodes = []
nodes_in_queue = []

def Breadth_First_Search(visited_nodes, theTree, node):
    visited_nodes.append(node)
    nodes_in_queue.append(node)

    while nodes_in_queue:
      z = nodes_in_queue.pop(0)
      print (z, end = " ")

      for adjacent_node in theTree[z]:
        if adjacent_node not in visited_nodes:
          visited_nodes.append(adjacent_node)
          nodes_in_queue.append(adjacent_node)

print('The order of the Breadth First Search is: ')
Breadth_First_Search(visited_nodes, theTree, '5')
print(f'\nThe list of visited nodes: {visited_nodes}. \nThe list of nodes left in the queue: {nodes_in_queue}')
