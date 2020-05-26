def lex_increase():
  x = int(input())
  y = int(input())
  z = int(input())
  n = int(input())
  
  print( [[ item1, item2, item3] for item1 in range(x+1) for item2 in range(y+1) for item3 in range(z+1) if item1+item2+item3 != n] )

  