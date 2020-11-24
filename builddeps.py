from collections import defaultdict 
import sys
limit = sys.setrecursionlimit(100000)
def DFS(c, path):
  global change,visited
  for i in range(0, len(path[c])):
    if path[c][i] not in change:
      change.append(path[c][i])
      if(path[c][i] in visited):
        return
      visited.append(path[c][i])
    if i == len(path[c])-1:
      for neighbor in change:
        return DFS(path[c][i], path)

change = []
visited = []
n = int(input())
path = defaultdict(list)
for i in range(0,n,1):
  f = input()
  str1, str2 = f.split(':')
  for item in str2.split():
    path[item].insert(0,str1)
c = input()
change.append(c)
DFS(c, path)
for item in change:
  print(item)
