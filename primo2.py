import time, sys
lim=int(input("Até qual número você quer? "))
n=0
s=time.time()
   
for nt in range(2, lim+1):
    r = int(nt**0.5)
    for nd in range(2, r+1):
        if nt % nd == 0:
            break
    else:
        print (nt)
        n=n+1
end=time.time()
print(str(n)+" primos em ",end-s)
a=input();
