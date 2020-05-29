def hashit():
  n = int(input())
  integer_list = map(int, input().split())
  print(integer_list)
  print(hash(tuple(integer_list)))

