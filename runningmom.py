from collections import defaultdict 

def Cycle(city,visited,timeclock, clock):
    global flight
    clock +=1
    timeclock[city].append(clock)
    for neighbor in flight[city]: 
      if neighbor not in visited: 
          visited.append(neighbor)
          clock = Cycle(neighbor,visited,timeclock, clock)
    clock +=1
    timeclock[city].append(clock)
    return clock

n = int(input())
flight = defaultdict(list)

for i in range (0,n,1):
    line = input().split()
    flight[line[0]].insert(0,line[1])
    
result = {}
n =0
while n <3:
    visited = []
    timeclock = defaultdict(list)
    try:
        city = input()
        visited.append(city)
        Cycle(city,visited,timeclock,0)
        for element in visited:
          if(city in flight[element]):
            if timeclock[city][0] < timeclock[element][0] and timeclock[element][1] < timeclock[city][1]:
                result[city] = "safe"
                break;
          else:
                result[city] = "trapped"
    except EOFError:
        break;
    n+=1
for element in result:
  print(element+' '+result[element])
