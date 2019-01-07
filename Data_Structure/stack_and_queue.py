class stack:
  def __init__(self):
    self.data = list()

  def insert(self, x):
    self.data.append(x)

  def pop(self):
    if len(self.data) == 0:
      return None
    else:
      return self.data.pop(-1)

  def len(self):
    return len(self.data)

class queue:
  def __init__(self):
    self.data = list()

  def insert(self, x):
    self.data.append(x)

  def pop(self):
    if len(self.data) == 0:
      return None
    else:
      return self.data.pop(0)

  def len(self):
    return len(self.data)

class bi_queue:
  def __init__(self):
    self.data = list()

  def insert_back(self, x):
    self.data.append(x)

  def insert_front(self, x):
    self.data = [x, ] + self.data

  def pop_front(self):
    if len(self.data) == 0:
      return None
    else:
      return self.data.pop(0)

  def pop_back(self):
    if len(self.data) == 0:
      return None
    else:
      return self.data.pop(-1)

  def len(self):
    return len(self.data)