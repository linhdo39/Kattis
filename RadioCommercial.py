string = input()
n,p = string.split()
n = int(n)
p = int(p)
comBreak = []
string2 = input()
for com in string2.split():
  comBreak.append(int(com)-p)
maxProfit = 0
profit = 0
for i in range (n):
  profit = profit + comBreak[i]
  if(comBreak[i] > profit):
    profit = comBreak[i]
  if(maxProfit < profit):
    maxProfit = profit

print(maxProfit)
