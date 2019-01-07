# coding=utf-8
import sys
import math

Inf = 0XFFFFFF


def rev_dict(dicti):
  dicto = dict()
  for key in dicti.keys():
    if dicti[key] in dicto.keys():
      dicto[dicti[key]].append(key)
    else:
      dicto[dicti[key]] = [key, ]
  return dicto


def exploreNeighbor(node, explored, map):
  sorted_neighbors = node.neighbors.keys()
  sorted_neighbors.sort()
  neighbors = []
  ncosts = []
  nacts = []
  for n in sorted_neighbors:
    for nn in node.neighbors[n]:
      if nn == 0 and not explored[node.x - 1][node.y]:
        neighbors.append(map[node.x - 1][node.y])
        ncosts.append(node.cost + 1)
        nacts.append(0)
      if nn == 1 and not explored[node.x + 1][node.y]:
        neighbors.append(map[node.x + 1][node.y])
        ncosts.append(node.cost + 1)
        nacts.append(1)
      if nn == 2 and not explored[node.x][node.y-1]:
        neighbors.append(map[node.x][node.y - 1])
        ncosts.append(node.cost + 1)
        nacts.append(2)
      if nn == 3 and not explored[node.x][node.y+1]:
        neighbors.append(map[node.x][node.y + 1])
        ncosts.append(node.cost + 1)
        nacts.append(3)
  return neighbors, ncosts, nacts


def argmin(lst):
  return lst.index(min(lst))


def argmax(lst):
  return lst.index(max(lst))


class node:
  def __init__(self, x, y, barriers, tx, ty, H, W):
    self.cost = Inf
    if [x, y] in barriers:
      return
    self.x = x
    self.y = y
    cost_point = [1, 1, 1, 1]  # U, D, L, R
    rev_neighbors = dict()
    self.last = -1
    if x == 0 or [x - 1, y] in barriers:
      cost_point[0] = Inf
    else:
      rev_neighbors[0] = math.fabs(x - 1 - tx) + math.fabs(y - ty)
    if x == H or [x + 1, y] in barriers:
      cost_point[1] = Inf
    else:
      rev_neighbors[1] = math.fabs(x + 1 - tx) + math.fabs(y - ty)
    if y == 0 or [x, y - 1] in barriers:
      cost_point[2] = Inf
    else:
      rev_neighbors[2] = math.fabs(x - tx) + math.fabs(y - 1 - ty)
    if y == W or [x, y + 1] in barriers:
      cost_point[3] = Inf
    else:
      rev_neighbors[3] = math.fabs(x - tx) + math.fabs(y + 1 - ty)
    self.neighbors = rev_dict(rev_neighbors)
    self.explored = False
    self.last = None


if __name__ == "__main__":
  line = sys.stdin.readline().strip()
  splits = line.split(' ')
  H, W = int(splits[0][0]), int(splits[0][2])
  bx, by = int(splits[1][0]), int(splits[1][2])
  tx, ty = int(splits[2][0]), int(splits[2][2])
  nBarriers = int(splits[3])
  barriers = list()
  path = list()
  last = list()
  neighbors = list()
  explored = list()
  map = list()

  cost = list()
  acts = list()
  cost_map = list()
  for i in range(nBarriers):
    barriers.append([int(splits[4 + i][0]), int(splits[4 + i][2])])
  for i in range(H+1):
    explored.append([False] * (W+1))
    map_row = []
    for j in range(W+1):
      map_row.append(node(i, j, barriers, tx, ty, H, W))
    map.append(map_row)
  tmp = map[bx][by]
  map[bx][by].cost = 0
  explored[bx][by] = True
  newneighbors, newcosts, newacts = exploreNeighbor(tmp, explored, map)
  neighbors += newneighbors
  cost += newcosts
  acts += newacts
  while len(neighbors) > 0:
    best = argmin(cost)
    n = neighbors.pop(best)
    ncost = cost.pop(best)
    action = acts.pop(best)
    if explored[n.x][n.y]:
      continue
    explored[n.x][n.y] = True
    map[n.x][n.y].last = action
    map[n.x][n.y].cost = ncost
    newneighbors, newcosts, newacts = exploreNeighbor(n, explored, map)
    neighbors += newneighbors
    cost += newcosts
    acts += newacts

  path = '[' + str(tx) + ',' + str(ty) + ']'
  n = map[tx][ty]
  if n.cost >= Inf:
    print('no way out')
  else:
    while True:
      if n.last is None:
        break
      if n.last == 0:
        path = '[' + str(n.x + 1) + ',' + str(n.y) + ']' + path
        n = map[n.x + 1][n.y]
      elif n.last == 1:
        path = '[' + str(n.x - 1) + ',' + str(n.y) + ']' + path
        n = map[n.x - 1][n.y]
      elif n.last == 2:
        path = '[' + str(n.x) + ',' + str(n.y + 1) + ']' + path
        n = map[n.x][n.y + 1]
      elif n.last == 3:
        path = '[' + str(n.x) + ',' + str(n.y - 1) + ']' + path
        n = map[n.x][n.y - 1]

    print(path)