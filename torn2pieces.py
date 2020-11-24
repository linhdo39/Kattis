from collections import defaultdict 

def path(starting,visited,destination):
    global town,shortestPath, mark
    visited.append(starting)
    mark.append(starting)
    for neighbor in town[starting]: 
      if neighbor == destination:
          if(starting in town[neighbor]):
            visited.append(neighbor)
            if(len(visited) < len(shortestPath)):
              shortestPath = visited
            return shortestPath
      elif neighbor not in mark:
          visited = path(neighbor,visited,destination)
          if not not visited:
            if(len(visited) < len(shortestPath)):
              shortestPath = visited
            return shortestPath
          else:
            return 0
    return 0

n = int(input())
town = defaultdict(list)

for i in range (0,n,1):
    line = input().split()
    for j in range (1,len(line)):
      if(line[j] not in town[line[0]]):
        town[line[0]].append(line[j])
      if(line[0] not in town[line[j]]):
        town[line[j]].append(line[0])
string = input().split()
starting = string[0]
destination = string[1]
shortestPath = [None]*641
visited = []
mark = []
if (starting not in town):
  print('no route found')
elif path(starting,visited,destination):
  print(" ".join([str(i) for i in shortestPath]))
else:
  print('no route found')
