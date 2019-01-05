from input_generator import randInt
import random
import sys
import math
import time

class radix_sort:

  def __init__(self):
    pass


  def sort(self, input, k=10):
    N = len(input)
    for i in range(k):
      result = self.digit_counting_sort(input, i)
      input = result

    return result

  def digit_counting_sort(self, input, d):
    N = len(input)
    C = [0] * 10
    B = [0] * N
    digit = [0] * N
    for i in range(N):
      digit[i] = int((input[i] / math.pow(10, d)) % 10)
      C[digit[i]] += 1

    for i in range(1, 10):
      C[i] += C[i-1]

    for i in range(N-1, -1, -1):
      B[C[digit[i]]-1] = input[i]
      C[digit[i]] -= 1

    return B


if __name__ == '__main__':

  h = radix_sort()
  # input = randInt(100, [0, 1024])
  n = 1000
  input = randInt(n, [0, 1600], pos=True, dup=True)
  # input = [7, 6, 5, 13, 5, 1]
  start = time.clock()
  result = h.sort(input)
  end = time.clock()
  print "{0:.4g}s" .format(end - start)
  print(result)