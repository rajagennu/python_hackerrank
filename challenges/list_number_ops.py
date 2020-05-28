def listops():
  N = int(input())
  """
  List of operations
    1. insert
    2. print
    3. remove
    4.append
    5.sort
    6.pop 
    7.reverse 
  """
  lst = []
  operations_list = [];

  for iter in range(N):
    operations_list.append(input())
  
  print(operations_list)

  for op in operations_list:
    op_split = op.split(" ")
    print(op_split)
    if op_split[0] == "insert" :
      lst.insert(int(op_split[1]), int(op_split[2]))
    elif op_split[0] == "append" :
      lst.append(int(op_split[1]))
    elif op_split[0] == "remove" : 
      lst.remove(int(op_split[1]))
    elif op_split[0] == "sort" :
      lst.sort()
    elif op_split[0] == "pop" :
      lst.pop()  
    elif op_split[0] == "reverse" :
      lst.reverse()
    elif op_split[0] == "print" :
      print(lst)    
    




