from itertools import groupby

def grouped():
  n = input()
  for item in [list(g) for k, g in groupby(n)] :
    print( (len (item) , int(item[0]) ), end=" ")
  print('')