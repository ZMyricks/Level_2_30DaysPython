import sys

class Drag_Con_Graph(object):

  def __init__(self, nodes, init_graph):
    self.nodes = nodes
    self.graph = self.construct_graph(nodes, init_graph)

  def construct_graph(self, nodes, init_graph):
    '''symetrical graph.'''
    graph = {node: {} for node in nodes}

    graph |= init_graph

    for node, edges in graph.items():
      for adjacent_node, value in edges.items():
        if graph[adjacent_node].get(node, False) == False:
          graph[adjacent_node][node] = value
    return graph
  def get_nodes(self):
      "Returns the nodes of the graph."
      return self.nodes

  def get_outgoing_edges(self, node):
    "Returns the neighbors of a node."
    return [
        out_node for out_node in self.nodes
        if self.graph[node].get(out_node, False) != False]

  def value(self, node1, node2):
      "Returns the value of an edge between two nodes."
      return self.graph[node1][node2]

def dijkstra_algorithm(graph, start_node):
  unvisited_nodes = list(graph.get_nodes())

  # dictionary to save the shortest known path to a node found
  previous_nodes = {}

  # max_value is used to initialize the "infinity" value of the unvisited nodes
  max_value = sys.maxsize
  shortest_path = {node: max_value for node in unvisited_nodes}
  # initialize the starting node's value with 0
  shortest_path[start_node] = 0

  # algorithm executes until we visit all nodes
  while unvisited_nodes:
    # The code block below finds the node with the lowest score
    current_min_node = None
    for node in unvisited_nodes: # Iterate over the nodes
      if current_min_node is None or shortest_path[node] < shortest_path[
          current_min_node]:
        current_min_node = node
    # The code block below retrieves the current node's neighbors and updates their distances
    neighbors = graph.get_outgoing_edges(current_min_node)
    for neighbor in neighbors:
        tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
        if tentative_value < shortest_path[neighbor]:
            shortest_path[neighbor] = tentative_value
            # We also update the best path to the current node
            previous_nodes[neighbor] = current_min_node

    # After visiting its neighbors, we mark the node as "visited"
    unvisited_nodes.remove(current_min_node)

  return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
  path = []
  node = target_node

  while node != start_node:
      path.append(node)
      node = previous_nodes[node]

  # Add the start node manually
  path.append(start_node)

  print(
      f"We found the following best path with a value of {shortest_path[target_node]}."
  )
  print(" -> ".join(reversed(path)))

nodes = ["Tayce", "Pearl", "Spanky Jackson", "Raja", "JuJubee", "Trinity K. Bonet", "Katya", "Mo Heart"]

init_graph = {node: {} for node in nodes}
init_graph["Tayce"]["Pearl"] = 5
init_graph["Tayce"]["Raja"] = 4
init_graph["Pearl"]["Mo Heart"] = 1
init_graph["Pearl"]["Spanky Jackson"] = 3
init_graph["Spanky Jackson"]["Katya"] = 5
init_graph["Spanky Jackson"]["Trinity K. Bonet"] = 4
init_graph["Trinity K. Bonet"]["Katya"] = 1
init_graph["JuJubee"]["Mo Heart"] = 2
init_graph["JuJubee"]["Trinity K. Bonet"] = 2

graph = Drag_Con_Graph(nodes, init_graph)

previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Tayce")

print_result(previous_nodes, shortest_path, start_node="Tayce", target_node="Katya")
