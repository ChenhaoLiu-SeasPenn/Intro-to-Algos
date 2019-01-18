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

def generatePriceList(length=30, max_leap=5, min_leap=0):

  leap_list = np.asarray(randInt(length, drange=(min_leap, max_leap), dup=True))
  p_list = np.zeros_like(leap_list)
  p_list[0] = leap_list[0]
  for i in range(length-1):
    p_list[i+1] = p_list[i] + leap_list[i+1]

  return [0,] + p_list.tolist()

if __name__ == '__main__':

  print(generatePriceList())
  print(generatePriceList(length=20, max_leap=25, min_leap=5))

