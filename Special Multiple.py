'''Special Multiple:
   To find the least positive integer X made up of only 9's and 0's, 
   such that, X is a multiple of N.
'''
T=int(input())
S=[]
for div in range(0,T):
    var=int(input())
    S.append(var)
for div in S:
  count=1
  while(count>0):
    a=bin(count)
    a=int(a[2: ])*9
    if(a%div)==0:
        print(a)
        break
    count=count+1
