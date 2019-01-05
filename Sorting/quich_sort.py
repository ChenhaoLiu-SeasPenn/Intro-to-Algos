from input_generator import randInt
import random
import sys
import math
import time

class quick_sort:

  def __init__(self):
    pass


  def sort(self, input):

    if len(input) <= 1:
      return input

    p = 0
    r = len(input) - 1
    q = self.partition(input, p, r)
    input[p:q] = self.sort(input[p:q])
    input[q:r+1] = self.sort(input[q:r+1])

    result = input

    return result


  def sort_random(self, input):

    if len(input) <= 1:
      return input

    p = 0
    r = len(input) - 1
    q = self.partition_random(input, p, r)
    input[p:q] = self.sort_random(input[p:q])
    input[q:r+1] = self.sort_random(input[q:r+1])

    result = input

    return result


  def partition(self, A, p, r):

    x = A[r]
    i = p - 1
    for j in range(p, r):
      if A[j] <= x:
        i += 1
        A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]

    return i+1


  def partition_random(self, A, p, r):

    rnew = random.randint(p, r)
    A[rnew], A[r] = A[r], A[rnew]

    x = A[r]
    i = p - 1
    for j in range(p, r):
      if A[j] <= x:
        i += 1
        A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]

    return i+1


if __name__ == '__main__':

  h = quick_sort()
  # input = randInt(100, [0, 1024])
  n = 1000000
  input = randInt(n, [-1000000, 1600000], pos=False)
  # input = [7, 6, 5, 13, 5, 1]
  start = time.clock()
  result = h.sort(input)
  end = time.clock()
  print "{0:.4g}s" .format(end - start)
  start = time.clock()
  result = h.sort_random(input)
  end = time.clock()
  print "{0:.4g}s".format(end - start)
  # print(result)