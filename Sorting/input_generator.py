import numpy as np

def randInt(nInts, drange=None, pos=True, dup=False):

  if not drange:
    if pos:
      drange = [0, nInts]
    else:
      drange = [-nInts, nInts]

  if dup:
    rand_int = np.random.randint(drange[0], drange[1], [nInts])
  else:
    sorted_int = np.arange(drange[0], drange[1], dtype=np.int32)
    np.random.shuffle(sorted_int)
    rand_int = sorted_int[:nInts]

  return rand_int.tolist()

if __name__ == '__main__':

  print(randInt(5))
  print(randInt(5, [-10, 10]))
  print(randInt(5, pos=False))
  print(randInt(5, dup=True))