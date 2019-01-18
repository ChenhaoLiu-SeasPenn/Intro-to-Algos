from input_generator import randInt

def best_matrix_chain(inputs):
  nMatrices = len(inputs) - 1
  nComputes = [[0xffffff for i in range(nMatrices)]for j in range(nMatrices)]
  splits = [[0 for i in range(nMatrices)]for j in range(nMatrices)]
  for i in range(nMatrices):
    nComputes[i][i] = 0
  for l in range(1, nMatrices + 1):
    for i in range(nMatrices - l + 1):
      j = i + l - 1
      for k in range(i, j):
        q = nComputes[i][k] + nComputes[k+1][j] + inputs[i] * inputs[k+1] * inputs[j+1]
        if q < nComputes[i][j]:
          nComputes[i][j] = q
          splits[i][j] = k

  return nComputes, splits

def getOptimalSol(splits, i, j, string):
  if i == j:
    string += str(i)
  else:
    string += '[' + getOptimalSol(splits, i, splits[i][j], string) + ',' + getOptimalSol(splits, splits[i][j]+1, j, string) + ']'
  return string


if __name__ == '__main__':
  matrices = [i*5 for i in randInt(31, drange=(1, 10), dup=True)]
  m, s = best_matrix_chain(matrices)
  print(getOptimalSol(s, 0, 29, ''))