n = int(input())
X = []
sum = 0
for i in range (0,n,1):
  a = int(input())
  X.append(a)
X.sort()
temp = 0
minDiff = 10000
for i in range (0,n,1):
  temp = X[i]
  for j in range(i+1,n,1):
    temp = temp + X[j]
    if temp > 1000 and X[i] > 1000:
      minDiff = -min(minDiff, 1000 - temp,1000 - X[i])
    elif temp > 1000 and X[i] < 1000:
      minDiff = -min(minDiff, 1000 - temp,1000 - X[i])
    elif temp < 1000 and X[i] > 1000:
      minDiff = -min(minDiff, 1000 - temp,abs(1000 - X[i]))
    else:
      minDiff = min(minDiff, 1000 -temp, 1000 -X[i])
if(n == 1):
    minDiff = X[0] - 1000
print(1000 - minDiff)
