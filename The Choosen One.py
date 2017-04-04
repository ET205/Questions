f = open("case.txt", "r") 
n = int(f.readline())
a = list(map(int, f.read().strip('\n').split()))
a.sort();
common_prime_factors=[]
temp_common_prime_factors=[]
primes=[2]
for i in range(3,int(a[n-1])):
    prime_length=len(primes)
    prime_yn=True
    for q in range(0,prime_length):
        if i%primes[q]==0:
            prime_yn=False
            break
    if prime_yn==True:
        primes.append(i)
        
print(primes)

def prime(num):
    if num in primes:
        return True
    else:
        return False

a=sorted(a, key=int, reverse=True)

def prime_factors(num):
    factors=[]
    print(num)
    for i in range(0,len(primes)):
        if num%primes[i]==0:
            factors.append(primes[i])
    print(factors)
    return factors


for i in range(0,n):
    '''if i%10000==0:
        print(i,end=" ")'''
    if prime(a[i])==False:
        factors=prime_factors(a[i])
        for q in range(0,len(factors)):
            if i==0:
                temp_common_prime_factors.append(factors[q])
            else:
                if factors[q] in common_prime_factors:
                    temp_common_prime_factors.append(factors[q])
        if len(temp_common_prime_factors)!=0:
            common_prime_factors=temp_common_prime_factors
            temp_common_prime_factors=[]
    if len(common_prime_factors)==1:
            break

if a[i] in common_prime_factors and i!=n-1 and len(common_prime_factors)!=1:
    del common_prime_factors[common_prime_factors.index(a[i])]

if n==1:
    print(n)
else:
    out=1
    for i in range(0,len(common_prime_factors)):
        out=out*common_prime_factors[i]
    print(out)
