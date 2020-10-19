def findIndex(k, n):
  if (n==1):
    return 'N'
  elif (n == 2):
    return 'A'
  a = length[n-2]
  if(k > a):
    return findIndex(k-a,n-1)
  return findIndex(k,n-2)

n , k = input().split(' ')
n = int(n)
k = int(k)
length=[]
for i in range (0,n,1):
  if(i== 0):
    length.append(0)
  elif (i ==1):
    length.append(i)
  else:
    length.append(length[i-2] +length[i-1])
print(length[n-1])
print(findIndex(k,n))
