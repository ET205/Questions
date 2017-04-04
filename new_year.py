import sys
Q=[2,1,5,3,4]
c=0
for j in Q:
    if(j<Q.index(j)+1):
        c=c+(Q.index(j)-j)
        if (Q.index(j)+1-j)>=3:
            print("too chaotic")
            sys.exit();
print(c)
