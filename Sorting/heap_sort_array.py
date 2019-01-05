from input_generator import randInt
import math
import time

class heap_sort:

  def __init__(self):
    pass


  def sort(self, input):

    N = len(input)
    self.build_max_heap(input, N)
    size = N
    result = []
    for i in range(N - 1, 0, -1):
      # start = time.clock()
      # tmp = input[0]
      # input[0] = input[-1]
      # input[-1] = tmp
      result = [input[0]] + result
      input[0], input[-1] = input[-1], input[0]
      size -= 1
      self.max_heapify2(input, 0, size)
      # end = time.clock()
      # print "{0:.4g}s".format(end - start)

    return result


  def max_heapify(self, heap, i, size):

    # size = len(heap)
    if not 2*i+1 < size:
      return

    lc = heap[2*i+1]
    if lc > heap[i]:
      largest = 2 * i + 1
      maximum = lc
    else:
      largest = i
      maximum = heap[i]

    if 2*i+2 < size:
      rc = heap[2*i+2]
      if rc > maximum:
        largest = 2 * i + 2

    if largest != i:
      heap[i], heap[largest] = heap[largest], heap[i]
      # tmp = heap[i]
      # heap[i] = heap[largest]
      # heap[largest] = tmp
      self.max_heapify(heap, largest, size)


  def max_heapify2(self, heap, parent, size):
    child = 2 * parent + 1  # left child
    while child < size:
      if child + 1 < size:
        if heap[child + 1] > heap[child]:
          child += 1  # right child
      if heap[parent] >= heap[child]:
        break
      heap[parent], heap[child] = heap[child], heap[parent]
      parent, child = child, 2 * child + 1
    # tmp = heap[start]
    #
    # i = start
    # j = i * 2 + 1
    # while j <= size-1:
    #   if (j < size-1) and (heap[j] < heap[j+1]):
    #     j += 1
    #   if tmp < heap[j]:
    #     heap[i] = heap[j]
    #     i = j
    #     j = 2 * i + 1
    #   else:
    #     break
    #
    # heap[i] = tmp


  def build_max_heap(self, heap, size):

    for i in range(size/2, -1, -1):
      self.max_heapify2(heap, i, size)


if __name__ == '__main__':

  h = heap_sort()
  # input = randInt(100, [0, 1024])
  n = 100000
  input = randInt(n, [-1000000, 1600000], pos=False)
  # input = [7, 6, 5, 13, 1]
  start = time.clock()
  result = h.sort(input)
  # result = input.sort()
  end = time.clock()
  print "{0:.4g}s" .format(end - start)
  print (end - start) / n / math.log(n)
  # print(result)