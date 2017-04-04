import time
t=time.clock()
n=int(input())
l=[]

def steps_req(fin):
    steps=(-1+(1+8*fin)**0.5)/2
    if(steps%1==0):
        return(int(steps))
    else:
        return(False)
for i in range(0,n):
    final=int(input())
    
    if(steps_req(final)==False):
        print("Better Luck Next Time")
    else:
        print("Go On Bob "+str(steps_req(final)))
t2=time.clock()
#print(t2-t)
