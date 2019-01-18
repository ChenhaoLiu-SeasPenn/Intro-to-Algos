from node import rb_tree_node as node

from stack_and_queue import stack, queue

class rb_tree(object):
  def __init__(self, input):
    tmp = node(-1)
    tmp.size = 0
    tmp.isNull = True
    self.Null = tmp
    self.Null.parent = self.Null
    self.Null.left = self.Null
    self.Null.right = self.Null
    self.root = self.Null
    for n in input:
      self.insert_compare(self.root, node(n))

  def insert(self, x):
    self.insert_compare(self.root, x)

  def insert_compare(self, parent, z):
    y = self.Null
    x = self.root
    while not x.isNull:
      y = x
      x.size += 1
      if z.val < x.val:
        x = x.left
      else:
        x = x.right
    if y.isNull:
      self.root = z
      y.left = z
    else:
      if z.val < y.val:
        y.left = z
      else:
        y.right = z
    z.parent = y
    z.left = self.Null
    z.right = self.Null
    z.color = 0
    self.fixup(z)

  def fixup(self, z):
    while z.parent.color == 0:
      if z.parent == z.parent.parent.left:
        y = z.parent.parent.right
        # Case 1: both parent and uncle are RED, revert color, point grandfather
        if y.color == 0:
          z.parent.color = 1
          y.color = 1
          y.parent.color = 0
          z = y.parent
        # Case 2: right child, parent RED, uncle BLACK, right-rotate
        elif z == z.parent.right:
          z = z.parent
          self.left_rotate(z)
        # Case 3: left child, parent RED, uncle BLACK, right-rotate
        if not z.parent.isNull:
          z.parent.color = 1
          z.parent.parent.color = 0
          self.right_rotate(z.parent.parent)
      else:
        y = z.parent.parent.left
        # Case 1: both parent and uncle are RED, revert color, point grandfather
        if y.color == 0:
          z.parent.color = 1
          y.color = 1
          y.parent.color = 0
          z = y.parent
        # Case 2: right child, parent RED, uncle BLACK, right-rotate
        elif z == z.parent.left:
          z = z.parent
          self.right_rotate(z)
        # Case 3: left child, parent RED, uncle BLACK, right-rotate
        if not z.parent.isNull:
          z.parent.color = 1
          z.parent.parent.color = 0
          self.left_rotate(z.parent.parent)
    self.root.color = 1
    self.Null.color = 1

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
      if not tmp.left.isNull:
        bfs_queue.append(tmp.left)
      if not tmp.right.isNull:
        bfs_queue.append(tmp.right)
    return bfs_out

  def preorder_walk(self):
    explored = list()
    self.preorder_unit(self.root, explored)
    return explored

  def preorder_unit(self, x, explored):
    explored.append(x.val)
    if x.left.isNull != True:
      self.preorder_unit(x.left, explored)
    if x.right.isNull != True:
      self.preorder_unit(x.right, explored)

  def inorder_walk(self):
    explored = list()
    self.inorder_unit(self.root, explored)
    return explored

  def inorder_unit(self, x, explored):
    if x.left.isNull != True:
      self.inorder_unit(x.left, explored)
    explored.append(x.val)
    if x.right.isNull != True:
      self.inorder_unit(x.right, explored)

  def postorder_walk(self):
    explored = list()
    self.postorder_unit(self.root, explored)
    return explored

  def postorder_unit(self, x, explored):
    if x.left.isNull != True:
      self.postorder_unit(x.left, explored)
    if x.right.isNull != True:
      self.postorder_unit(x.right, explored)
    explored.append(x.val)

  def iterative_preorder_walk(self):
    explored = queue()
    explore_stack = stack()
    current = self.root
    current = self.preorder_dive(current, explore_stack, explored)

    while explore_stack.len() > 0:
      tmp = explore_stack.pop()
      if tmp.right.isNull != True:
        current = self.preorder_dive(tmp.right, explore_stack, explored)
    return explored.data

  def preorder_dive(self, x, explore_stack, explored):
    while True:
      while x.left.isNull != True:
        explored.insert(x.val)
        explore_stack.insert(x)
        x = x.left
      explored.insert(x.val)
      if x.right.isNull != True:
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
      if tmp.right.isNull != True:
        current = self.inorder_dive(tmp.right, explore_stack, explored)
    return explored.data

  def inorder_dive(self, x, explore_stack, explored):
    while True:
      while x.left.isNull != True:
        explore_stack.insert(x)
        x = x.left
      explored.insert(x.val)
      if x.right.isNull != True:
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
      if tmp.left.isNull != True:
        current = self.postorder_dive(tmp.left, explore_stack, explored)
    return explored.data[::-1]

  def postorder_dive(self, x, explore_stack, explored):
    while True:
      while x.right.isNull != True:
        explored.insert(x.val)
        explore_stack.insert(x)
        x = x.right
      explored.insert(x.val)
      if x.left.isNull != True:
        x = x.left
      else:
        break
    return x

  def inquire(self, v, x=None):
    if x is None:
      # If x unspecified, search whole tree, otherwise search subtree with root x
      x = self.root
    while x.isNull != True and x.val != v:
      if v < x.val:
        x = x.left
      else:
        x = x.right
    return x

  def minimum(self, x=None):
    if x is None:
      x = self.root
    while x.left.isNull != True:
      x = x.left
    return x

  def maximum(self, x=None):
    if x is None:
      x = self.root
    while x.right.isNull != True:
      x = x.right
    return x

  def predecessor(self, x):
    if x.left.isNull != True:
      return self.maximum(x.left)
    y = x.parent
    while y.isNull != True and x.val == y.left.val:
      x = y
      y = y.parent
    return y

  def succeesor(self, x):
    if x.right.isNull != True:
      return self.minimum(x.right)
    y = x.parent
    while y.isNull != True and x.val == y.right.val:
      x = y
      y = y.parent
    return y

  def delete(self, x):
    y = x
    y_original_color = y.color
    v = x
    while v != self.root:
      v = v.parent
      v.size -= 1

    if y.left.isNull:
      z = y.right
      self.transplant(x, x.right)
    elif y.right.isNull:
      z = y.left
      self.transplant(x, x.left)
    else:
      y = self.minimum(x.right)
      y_original_color = y.color
      z = y.right
      if y.parent == x:
        z.parent = y
      else:
        self.transplant(y, y.right)
        y.right = x.right
        y.right.parent = y
      self.transplant(x, y)
      y.left = x.left
      x.left.parent = y
      y.color = x.color
    if y_original_color == 1:
      self.delete_fixup(z)

  def delete_fixup(self, x):
    while x != self.root and x.color == 1:
      # x has an extra color +B. if x is RB, we can change x to B and finish, if x is root we can simply remove +B
      # without changing RBTree character
      if x == x.parent.left:
        w = x.parent.right
        # check sibling color
        if w.color == 0:
          # Case 1: if sibling red, it must have two black children, so revert w, x.p, then left-rotate
          w.color = 1
          x.parent.color = 0
          self.left_rotate(x.parent)
          w = x.parent.right
        # Case 1 converted to 2/3/4
        if w.left.color == 1 and w.right.color == 1:
          # Case 2: both nephews black, change sibling to red, pointer moveup
          w.color = 0
          x = x.parent
        else:
          if w.right.color == 1:
            # Case 3: right nephew is black, revert color, right-rotate. convert to case 4
            w.left.color = 1
            w.color = 0
            self.right_rotate(w)
            w = x.parent.right
          # Case 4: left nephew is black
          w.color = x.parent.color
          x.parent.color = 1
          w.right.color = 1
          self.left_rotate(x.parent)
          x = self.root
      else:
        # revert left and right with the same operations
        w = x.parent.left
        if w.color == 0:
          w.color = 1
          x.parent.color = 0
          self.right_rotate(x.parent)
          w = x.parent.right
        if w.left.color == 1 and w.right.color == 1:
          w.color = 0
          x = x.parent
        else:
          if w.left.color == 1:
            w.right.color = 1
            w.color = 0
            self.left_rotate(w)
            w = x.parent.left
          w.color = x.parent.color
          x.parent.color = 1
          w.left.color = 1
          self.right_rotate(x.parent)
          x = self.root
    # keep root color black
    x.color = 1

  def transplant(self, x, y):
    if x.parent.isNull:
      self.root = y
    elif x == x.parent.left:
      x.parent.left = y
    else:
      x.parent.right = y
    y.parent = x.parent

  def left_rotate(self, x):
    if x.isNull:
      return
    y = x.right
    x.right = y.left
    if not y.left.isNull:
      y.left.parent = x
    y.parent = x.parent
    if x.parent.isNull:
      self.root = y
    elif x == x.parent.left:
      x.parent.left = y
    else:
      x.parent.right = y
    y.left = x
    x.parent = y
    y.size = x.size
    x.size = x.left.size + x.right.size + 1

  def right_rotate(self, x):
    if x.isNull:
      return
    y = x.left
    x.left = y.right
    if not y.right.isNull:
      y.right.parent = x
    y.parent = x.parent
    if x.parent.isNull:
      self.root = y
    elif x == x.parent.left:
      x.parent.left = y
    else:
      x.parent.right = y
    y.right = x
    x.parent = y
    y.size = x.size
    x.size = x.left.size + x.right.size + 1

  def check_rb_status(self):
    # TODO: check the status of rb tree
    if self.root.color == 0:
      return False
    if self.Null.color == 0:
      return False
    nodes = self.bfs()
    for node in nodes:
      if node.color == 0:
        if node.left.color == 0 or node.right.color == 0:
          return False

  def select(self, i, x=None):
    if x is None:
      x = self.root
      if i > x.size:
        raise ValueError('Order number larger than tree size')
    r = x.left.size + 1
    if r == i:
      return x
    elif r < i:
      return self.select(i - r, x.right)
    else:
      return self.select(i, x.left)

  def select_it(self, i):
    x = self.root
    if i > x.size:
      raise ValueError('Order number larger than tree size')
    r = x.left.size + 1
    while i != r:
      if i < r:
        x = x.left
      else:
        x = x.right
        i -= r
      r = x.left.size + 1
    return x

  def rank(self, x):
    r = x.left.size + 1
    while x != self.root:
      if x == x.parent.right:
        r += x.parent.left.size + 1
      x = x.parent

    return r


if __name__ == '__main__':
  nums = [3, 5, 1, 2, 4, 6]
  rb_tree = rb_tree(nums)
  rb_tree.insert(node(7))
  bn_nodes = rb_tree.bfs()
  rb_tree.delete(bn_nodes[2])
  bn_nodes = rb_tree.bfs()
  for n in bn_nodes:
    n.inspect()
  explored = rb_tree.iterative_preorder_walk()
  print(explored)
  explored = rb_tree.iterative_inorder_walk()
  print(explored)
  explored = rb_tree.iterative_postorder_walk()
  print(explored)
  print(rb_tree.predecessor(bn_nodes[2]).val)
  print(rb_tree.succeesor(bn_nodes[2]).val)
  print(rb_tree.minimum().val, rb_tree.maximum().val, rb_tree.minimum(bn_nodes[2]).val)
  print(rb_tree.select_it(1).val, rb_tree.rank(bn_nodes[3]))