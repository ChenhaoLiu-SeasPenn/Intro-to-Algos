from input_generator import randInt
import time

class heap_sort:

  def __init__(self):
    pass

  def sort(self, input):

    d_heap = heap(input)
    d_heap.build_max_heap()
    result = [0] * len(input)
    for i in range(d_heap.size-1, 0, -1):
      result[i] = d_heap.struc[0].val
      # result.append(d_heap.struc[0].val)
      d_heap.swap_hpoint(d_heap.struc[0], d_heap.struc[i])
      d_heap.size -= 1
      # d_heap.build_max_heap(
      d_heap.maxify(0)
    result[0] = d_heap.struc[0].val
    # result.append(d_heap.struc[0].val)

    return result


class heap:

  def __init__(self, data):
    self.size = len(data)
    self.struc = self.build_heap(data)

  def build_heap(self, data):
    struc = []
    for i in range(self.size):
      l = None
      r = None
      if 2*i+1 < self.size:
        l = 2*i+1
      if 2*i+2 < self.size:
        r = 2*i+2
      struc.append(heap_point(data[i], l, r))

    return struc

  def build_max_heap(self):
    for i in range(self.size/2+1, 0, -1):
      self.maxify(i-1)

  def swap_hpoint(self, lp, rp):
    tmp_val = lp.val
    lp.val = rp.val
    rp.val = tmp_val

  def maxify(self, i):
    l = self.struc[i].lchild
    r = self.struc[i].rchild
    if not l:
      return
    if l < self.size and self.struc[i].val <= self.struc[l].val:
      largest = l
    else:
      largest = i
    if r:
      if r < self.size and self.struc[largest].val <= self.struc[r].val:
        largest = r
    if i != largest:
      self.swap_hpoint(self.struc[i], self.struc[largest])
      self.maxify(largest)


class heap_point:

  def __init__(self, value, lc=None, rc=None):

    self.val = value
    self.lchild = lc
    self.rchild = rc


if __name__ == '__main__':

  h = heap_sort()
  # input = randInt(100000, [0, 16777216])
  input = randInt(1000000, [-1000000, 1600000], pos=False)
  # input = [7, 6, 5, 13, 1]
  start = time.clock()
  result = h.sort(input)
  # result = input.sort()
  end = time.clock()
  print "{0:.4g}s" .format(end - start)
  # print(result)