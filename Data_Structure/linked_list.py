from node import linked_list_node as node

class linked_list:

  def __init__(self):
    self.head = None
    self.tail = None

  def search_list_key(self, k):
    if self.head is None:
      return None
    else:
      x = self.head
      while True:
        if x.val == k:
          return x
        x = x.nex
        if x is None:
          return None

  def search_list_by_key(self, x):
    return self.search_list_key(x.val)

  def append(self, x):
    if not self.head:
      self.head = x
      self.tail = x
    else:
      x.pre = self.tail
      self.tail.nex = x
      self.tail = x
    x.nex = None

  def insert_top(self, x):
    x.nex = self.head
    if self.head is not None:
      self.head.pre = x
    self.head = x
    x.pre = None

  def delete(self, x):
    if x.pre is not None:
      x.pre.nex = x.nex
    else:
      self.head = x.nex
    if x.nex is not None:
      x.nex.pre = x.pre
    else:
      self.tail = x.pre
    x.pre = None
    x.nex = None

  def delete_by_val(self, k):
    x = self.search_list_key(k)
    self.delete(x)

  def inspect(self):
    x = self.head
    string = '['
    while x is not None:
      if x.nex:
        string += str(x.val)+', '
      else:
        string += str(x.val)
      x = x.nex
    string += ']'
    print(string)

if __name__ == '__main__':
  nums = [1, 5, 4, 3, 3, 2]
  ll = linked_list()
  ll.inspect()
  nodes = list()
  for i in nums:
    ntmp = node(i)
    ll.append(ntmp)
    nodes.append(ntmp)
  ll.inspect()
  nd = ll.search_list_by_key(nodes[1])
  nd.inspect()
  ll.delete_by_val(5)
  ll.inspect()
  nd.inspect()
  ll.delete(nodes[2])
  ll.inspect()