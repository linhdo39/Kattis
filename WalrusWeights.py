n = int(input())
X = []
for i in range (0,n,1):
    a = int(input())
    X.append(a)
X.sort()
weight = [False]*2000
temp = 0
for i in range (0,n,1):
    temp = X[i]
    weight[X[i]] = True
    for j in range(i+1,n,1):
        temp = temp + X[j]
        if temp < 2000:
            weight[temp] = True

maxWeight = 0
for i in range(0,1000):
    if weight[1000 + i] == True:
        maxWeight = 1000 + i
        break;
    elif weight[1000 - i] == True:
        maxWeight = 1000 -i
        break;

if(n == 1):
    maxWeight = X[0]
    
print(maxWeight)
