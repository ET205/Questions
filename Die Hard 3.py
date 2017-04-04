import fractions
n=int(input())
for i in range(0,n):
    a,b,c=map(int, input().split())
    if(c%(fractions.gcd(a,b))==0 ) and (c<=a or c<=b):
         print("yes")
    else:
        print("no")
