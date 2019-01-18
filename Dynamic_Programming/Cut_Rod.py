from input_generator import generatePriceList

def cut_rod(inputs, length, showList=False):
  Inf = 0xffffff
  l = length
  best_prices = [0, ]
  cuts = [0, ]
  for i in range(1, l+2):
    q = 0
    first = 0
    for j in range(1, i):
      if inputs[j]+best_prices[i-j] > q:
        q = inputs[j]+best_prices[i-j]
        first = j
    cuts.append(first)
    best_prices.append(q)

  if showList:
    return best_prices[1:], cuts[1:]
  return best_prices[length+1], generate_cut(cuts, length)

def generate_cut(cuts, length):
  cut_method = []
  i = length + 1
  while True:
    j = cuts[i]
    i = i - j
    cut_method.append(j)
    if i == 1:
      # cut_method.append(i)
      break

  return cut_method

if __name__ == '__main__':
  # price_list = [0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30]
  price_list = generatePriceList(length=43)
  print(price_list)
  price, method = cut_rod(price_list, 43, showList=False)
  print(price)
  print(method)