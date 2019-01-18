class linked_list_node:

  def __init__(self, val):
    self.val = val
    self.pre = None
    self.nex = None

  def inspect(self):
    string = str(self.val)
    if self.pre is not None:
      string = str(self.pre.val) + ' <- ' + string
    else:
      string = 'None <- ' + string
    if self.nex is not None:
      string += ' -> ' + str(self.nex.val)
    else:
      string += ' -> None'
    print(string)


class bn_tree_node:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None

  def inspect(self):
    string = ''
    if self.parent is not None:
      string += '\t' + str(self.parent.val) + '\t\n'
    else:
      string += '\tNone\t\n'
    string += '\t' + str(self.val) + '\t\n'
    if self.left is not None:
      string += str(self.left.val) + '\t'
    else:
      string += 'None\t'
    if self.right is not None:
      string += str(self.right.val)
    else:
      string += 'None'
    string += '\n'
    print(string)


class rb_tree_node(bn_tree_node):
  def __init__(self, val):
    bn_tree_node.__init__(self, val)
    self.color = 1 # 0 for red, 1 for black
    self.isNull = False # Use a flag to mark Nil node
    self.size = 1

  def inspect(self):
    bn_tree_node.inspect(self)
    if self.color == 0:
      print('RED')
    else:
      print('BLACK')
