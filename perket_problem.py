totalSour = []
totalBitter = []
Sour = []
Bitter = []

def Product(Sour, totalSour, i, n, product = 1):
  if(i == n):
    if product != 0:
      totalSour.append(product)
    return
  Product(Sour, totalSour, i + 1, n, product * Sour[i])  
  Product(Sour, totalSour, i + 1, n, product) 

def Sums(Bitter, totalBitter, i, n, sum = 0):
  if(i == n):
    if sum != 0:
      totalBitter.append(sum)
    return
  Sums(Bitter, totalBitter, i + 1, n, sum + Bitter[i])  
  Sums(Bitter, totalBitter, i + 1, n, sum)

N = int(input())  
for i in range(N):
  S,B = str(input()).split(' ')
  Sour.append(int(S))
  Bitter.append(int(B)) 
Product(Sour, totalSour, 0, len(Sour))
Sums(Bitter, totalBitter, 0, len(Bitter))
diff = 10**9
for i in range(len(totalBitter)):
  if abs(totalBitter[i]-totalSour[i]) < diff: 
    diff = abs(totalBitter[i]-totalSour[i])
print(diff)
