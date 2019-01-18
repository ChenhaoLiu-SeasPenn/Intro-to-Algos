def LCS(A, B):

  m = len(A)
  n = len(B)
  M = [[-1 for i in range(n)] for j in range(m)]
  for i in range(m):
    if A[i] == B[0]:
      M[i][0] = 1
    else:
      try:
        M[i][0] = max(0, M[i-1][0])
      except:
        M[i][0] = 0
  for j in range(n):
    if A[0] == B[j]:
      M[0][j] = 1
    else:
      try:
        M[0][j] = max(0, M[0][j-1])
      except:
        M[0][j] = 0
  for i in range(1, m):
    for j in range(1, n):
      if A[i] == B[j]:
        M[i][j] = M[i - 1][j - 1] + 1
      else:
        M[i][j] = max(M[i - 1][j], M[i][j - 1])

  return M

def LCS_consecutive(A, B):

  m = len(A)
  n = len(B)
  M = [[-1 for i in range(n)] for j in range(m)]
  max_length = 0
  max_end = -1
  for i in range(m):
    if A[i] == B[0]:
      M[i][0] = 1
      max_length = 1
      max_end = i
    else:
      M[i][0] = 0
  for j in range(n):
    if A[0] == B[j]:
      M[0][j] = 1
    else:
      M[0][j] = 0
  for i in range(1, m):
    for j in range(1, n):
      if A[i] == B[j]:
        M[i][j] = M[i - 1][j - 1] + 1
        if M[i][j] > max_length:
          max_length = M[i][j]
          max_end = i
      else:
        M[i][j] = 0

  return max_length, max_end


def buildOptSol(M, A, B):

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
  if i == 0 and j != 0 and M[i][j] == 1:
    sol = A[0] + sol
  elif j == 0 and i != 0 and M[i][j] == 1:
    sol = B[0] + sol
  elif i == j == 0 and A[0] == B[0]:
    sol = A[0] + sol
  return sol


if __name__ == '__main__':
  A = 'bc'
  B = 'c'
  M = LCS(A, B)
  print(buildOptSol(M, A, B))
  ml, me = LCS_consecutive(A, B)
  print(A[me-ml+1:me+1])