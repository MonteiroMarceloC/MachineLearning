#primo2
import time, sys
lim=int(input("Até qual número você quer? "))
s=time.time()
for nt in range(2, lim):
     for nd in range(2, nt):
         if nt % nd == 0:
             break
     else:
         # loop fell through without finding a factor
         print (nt)
end=time.time()
print("...em ",end-s)
