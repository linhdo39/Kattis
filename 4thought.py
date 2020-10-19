ops = ['+','-','*','//']
expr = []
m= int(input())
for x in range(m):
  n = int(input())
  expression = None
  for op1 in ops:
    for op2 in ops:
      for op3 in ops:
        if n == eval('4 %s 4 %s 4 %s 4' % (op1, op2, op3)):
          expression = '4 %s 4 %s 4 %s 4' % (op1, op2, op3)
          if expression.__contains__('//'):
            expression = expression.replace('//','/')
          expr.append('%s = %i' %(expression,n))
          break;
      if(expression != None):
        break;
    if(expression != None):
      break;
      
  if expression == None:
    expr.append('no solution')
for x in range(0,len(expr)):
  inputfile = open("a.txt",'a+')
  if x == len(expr) -1:
    inputfile.write(expr[x])
    print(expr[x])
  else:
    inputfile.write(expr[x]+'\n')
    print(expr[x], end ='\n')
inputfile.close()
