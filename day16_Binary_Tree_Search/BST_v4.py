#  create a binary search tree
class BinarySearchTree:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

newBranch = BinarySearchTree(None) # this is a type = <class '__main__.BinarySearchTree'>

# function to insert nodes in the Binary Search Tree
def node_value_insert(root_node, node_value):
  if root_node.data is None:
    root_node.data = node_value
    print(f'{node_value} is inserted at root node')
  elif node_value <= root_node.data:
    if root_node.leftChild is None:
      root_node.leftChild = BinarySearchTree(node_value)
      print(f'{node_value} is inserted at left subtree of {root_node.data}')
    else:
      node_value_insert(root_node.leftChild, node_value)
      # print(f'{node_value} is moved to lowest left subtree')
  elif root_node.rightChild is None:
    root_node.rightChild = BinarySearchTree(node_value)
    print(f'{node_value} is inserted at right subtree of {root_node.data}')
  else:
    node_value_insert(root_node.rightChild, node_value)
    # print(f'{node_value} is moved to lowest right subtree')


#Initializing the Binary Search Tree
newTree = BinarySearchTree(None)

node_value_insert(newTree, 70)
node_value_insert(newTree, 50)
node_value_insert(newTree, 90)
node_value_insert(newTree, 30)
node_value_insert(newTree, 80)
node_value_insert(newTree, 100)
node_value_insert(newTree, 20)
node_value_insert(newTree, 40)
