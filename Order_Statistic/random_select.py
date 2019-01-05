from input_generator import randInt
import random
import sys
import math
import time

class random_select:

  def __init__(self):
    pass


  def random_select(self, input, order):

    if len(input) == 1:
      return input[0]

    p = 0
    r = len(input)
    q, val = self.random_partition(input, p, r)
    if q == order-1:
      return val
    elif q < order-1:
      val = self.random_select(input[q+1:r], order-1-q)
      return val
    else:
      val = self.random_select(input[p:q], order)
      return val


  def random_partition(self, input, p, r):

    rnew = random.randint(p, r-1)
    input[r-1], input[rnew] = input[rnew], input[r-1]

    x = input[r-1]
    i = p - 1
    for j in range(p, r):
      if input[j] < x:
        i += 1
        input[i], input[j] = input[j], input[i]

    input[i+1], input[r-1] = input[r-1], input[i+1]

    return i+1, x


if __name__ == '__main__':

  h = random_select()
  input, order = randInt(100, [0, 1024])
  # n = 1000000
  # input = randInt(n, [-1000000, 1600000], pos=False)
  # input = [6, 5, 4, 3, 2, 1]
  for i in range(100):
    start = time.clock()
    result = h.random_select(input, i+1)
    end = time.clock()
    print "{0:.4g}s" .format(end - start)
    print result