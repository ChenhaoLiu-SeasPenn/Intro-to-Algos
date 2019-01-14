from node import bn_tree_node as node
from stack_and_queue import stack, queue

class rooted_bn_tree(object):
  def __init__(self, input, bs=True):
    self.root = None
    parent = self.root
    for n in input:
      if bs:
        self.insert_compare(self.root, node(n))
      else:
        parent = self.insert_fill(parent, node(n))

  def insert(self, x):
    self.insert_compare(self.root, x)

  def insert_left(self, parent, x):
    if parent is None:
      self.root = x
      return
    if parent.left is None:
      parent.left = x
      x.parent = parent
    else:
      parent.left.parent = x
      x.left = parent.left
      parent.left = x
      x.parent = parent

  def insert_right(self, parent, x):
    if parent is None:
      self.root = x
      return
    if parent.right is None:
      parent.right = x
      x.parent = parent
    else:
      parent.right.parent = x
      x.left = parent.right
      parent.right = x
      x.parent = parent

  def insert_fill(self, parent, x):
    if parent is None:
      self.insert_left(parent, x)
      return x
    if parent.left is not None and parent.right is None:
      self.insert_right(parent, x)
      return parent.left
    else:
      self.insert_left(parent, x)
      if parent.right is None:
        return parent
      if x.left is not None:
        return x.left
      else:
        return x

  def insert_compare(self, parent, x):
    if parent is None:
      self.insert_left(parent, x)
    elif x.val > parent.val:
      if parent.right is None:
        self.insert_right(parent, x)
      else:
        self.insert_compare(parent.right, x)
    else:
      if parent.left is None:
        self.insert_left(parent, x)
      else:
        self.insert_compare(parent.left, x)

  def bfs(self):
    '''
    :return: List of nodes given by BFS
    '''
    bfs_queue = list()
    bfs_out = list()
    bfs_queue.append(self.root)
    while len(bfs_queue) > 0:
      tmp = bfs_queue.pop(0)
      bfs_out.append(tmp)
      if tmp.left is not None:
        bfs_queue.append(tmp.left)
      if tmp.right is not None:
        bfs_queue.append(tmp.right)
    return bfs_out

  def preorder_walk(self):
    explored = list()
    self.preorder_unit(self.root, explored)
    return explored

  def preorder_unit(self, x, explored):
    explored.append(x.val)
    if x.left is not None:
      self.preorder_unit(x.left, explored)
    if x.right is not None:
      self.preorder_unit(x.right, explored)

  def inorder_walk(self):
    explored = list()
    self.inorder_unit(self.root, explored)
    return explored

  def inorder_unit(self, x, explored):
    if x.left is not None:
      self.inorder_unit(x.left, explored)
    explored.append(x.val)
    if x.right is not None:
      self.inorder_unit(x.right, explored)

  def postorder_walk(self):
    explored = list()
    self.postorder_unit(self.root, explored)
    return explored

  def postorder_unit(self, x, explored):
    if x.left is not None:
      self.postorder_unit(x.left, explored)
    if x.right is not None:
      self.postorder_unit(x.right, explored)
    explored.append(x.val)

  def iterative_preorder_walk(self):
    explored = queue()
    explore_stack = stack()
    current = self.root
    current = self.preorder_dive(current, explore_stack, explored)

    while explore_stack.len() > 0:
      tmp = explore_stack.pop()
      if tmp.right is not None:
        current = self.preorder_dive(tmp.right, explore_stack, explored)
    return explored.data

  def preorder_dive(self, x, explore_stack, explored):
    while True:
      while x.left is not None:
        explored.insert(x.val)
        explore_stack.insert(x)
        x = x.left
      explored.insert(x.val)
      if x.right is not None:
        x = x.right
      else:
        break
    return x

  def iterative_inorder_walk(self):
    explored = queue()
    explore_stack = stack()
    current = self.root
    current = self.inorder_dive(current, explore_stack, explored)

    while explore_stack.len() > 0:
      tmp = explore_stack.pop()
      explored.insert(tmp.val)
      if tmp.right is not None:
        current = self.inorder_dive(tmp.right, explore_stack, explored)
    return explored.data

  def inorder_dive(self, x, explore_stack, explored):
    while True:
      while x.left is not None:
        explore_stack.insert(x)
        x = x.left
      explored.insert(x.val)
      if x.right is not None:
        x = x.right
      else:
        break
    return x

  def iterative_postorder_walk(self):
    explored = queue()
    explore_stack = stack()
    current = self.root
    current = self.postorder_dive(current, explore_stack, explored)
    while explore_stack.len() > 0:
      tmp = explore_stack.pop()
      if tmp.left is not None:
        current = self.postorder_dive(tmp.left, explore_stack, explored)
    return explored.data[::-1]

  def postorder_dive(self, x, explore_stack, explored):
    while True:
      while x.right is not None:
        explored.insert(x.val)
        explore_stack.insert(x)
        x = x.right
      explored.insert(x.val)
      if x.left is not None:
        x = x.left
      else:
        break
    return x

  def inquire(self, v, x=None):
    if x is None:
      # If x unspecified, search whole tree, otherwise search subtree with root x
      x = self.root
    while x is not None and x.val != v:
      if v < x.val:
        x = x.left
      else:
        x = x.right
    return x

  def minimum(self, x=None):
    if x is None:
      x = self.root
    while x.left is not None:
      x = x.left
    return x

  def maximum(self, x=None):
    if x is None:
      x = self.root
    while x.right is not None:
      x = x.right
    return x

  def predecessor(self, x):
    if x.left is not None:
      return self.maximum(x.left)
    y = x.parent
    while y is not None and x.val == y.left.val:
      x = y
      y = y.parent
    return y

  def succeesor(self, x):
    if x.right is not None:
      return self.minimum(x.right)
    y = x.parent
    while y is not None and x.val == y.right.val:
      x = y
      y = y.parent
    return y

  def delete(self, x):
    if x.left is None and x.right is None:
      y = x.parent
      if y is None:
        self.root = None
      else:
        if x == y.left:
          y.left = None
        else:
          y.right = None
    elif x.left is None:
      if x.parent is None:
        self.root = x.right
      else:
        self.transplant(x, x.right)
    elif x.right is None:
      if x.parent is None:
        self.root = x.left
      else:
        self.transplant(x, x.left)
    else:
      y = self.minimum(x.right)
      if y.parent != x:
        self.transplant(y, y.right)
        y.right = x.right
        y.right.parent = y
      self.transplant(x, y)
      y.left = x.left
      y.left.parent = y

  def transplant(self, x, y):
    if x.parent is None:
      self.root = y
      return
    if x == x.parent.left:
      x.parent.left = y
    else:
      x.parent.right = y
    if y is not None:
      y.parent = x.parent


if __name__ == '__main__':
  nums = [3, 5, 1, 2, 4, 6]
  bn_tree = rooted_bn_tree(nums)
  bn_tree.insert(node(7))
  bn_nodes = bn_tree.bfs()
  bn_tree.delete(bn_nodes[0])
  bn_nodes = bn_tree.bfs()
  for n in bn_nodes:
    n.inspect()
  explored = bn_tree.preorder_walk()
  print(explored)
  explored = bn_tree.iterative_preorder_walk()
  print(explored)
  explored = bn_tree.inorder_walk()
  print(explored)
  explored = bn_tree.iterative_inorder_walk()
  print(explored)
  explored = bn_tree.postorder_walk()
  print(explored)
  explored = bn_tree.iterative_postorder_walk()
  print(explored)
  # print(bn_tree.predecessor(bn_nodes[2]).val)
  # print(bn_tree.succeesor(bn_nodes[2]).val)
  # print(bn_tree.minimum().val, bn_tree.maximum().val, bn_tree.minimum(bn_nodes[2]).val)