def pizza(prohibition, X, index):
  global count
  if  index == n+1:
    return
  A = []
  X.append(index)
  for i in range(0,len(X)):
    A.append(index not in prohibition[X[i]])
  if all(A):
      count += 1
      pizza(prohibition,X,index+1)
  X.remove(index)
  pizza(prohibition,X,index+1)
  
n, m = input().split()
n = int(n)
m = int(m)
prohibition = {}
X = []
count = 1
for i in range (1,n+1,1):
  prohibition[i] = set()
for i in range (0,m,1):
  a, b = input().split()
  a = int(a)
  b = int(b)
  if a > b:
    x = a
    a = b
    b = x
  prohibition[a].add(b)
pizza(prohibition,X,1)
print(count)
