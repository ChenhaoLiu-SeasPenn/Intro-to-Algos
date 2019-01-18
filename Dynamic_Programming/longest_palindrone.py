def LPL(A):
  n = len(A)
  B = A[-1:0:-1] + A[0]
  M = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
    if A[i] == B[0]:
      M[i][0] = 1
    else:
      M[i][0] = 0
  for j in range(n):
    if A[0] == B[j]:
      M[0][j] = 1
    else:
      M[0][j] = 0
  for i in range(1, n):
    for j in range(1, n):
      if A[i] == B[j]:
        M[i][j] = M[i - 1][j - 1] + 1
      else:
        M[i][j] = max(M[i - 1][j], M[i][j - 1])

  return M

def buildOptSol(M, A):

  B = A[-1:0:-1] + A[0]

  sol = str()
  i = len(A) - 1
  j = len(B) - 1
  while i !=0 and j != 0:
    if i != 0 and M[i][j] == M[i - 1][j]:
      i -= 1
    elif j != 0 and M[i][j] == M[i][j - 1]:
      j -= 1
    else:
      if not M[i][j] == M[i - 1][j - 1] + 1:
        raise ValueError('Something is wrong!')
      sol = A[i] + sol
      i -= 1
      j -= 1
  if i == 0 and j != 0:
    sol = B[j] + sol
  elif j == 0 and i != 0:
    sol = A[i] + sol
  return sol


if __name__ == '__main__':
  A = 'bestalgorithmever'
  M = LPL(A)
  print(buildOptSol(M, A))