import time, sys
lim=int(input("Quantos primos você quer? "))
s=time.time()

p = [2]
print(p[0])
nt = 3
while len(p) < lim:
     r=nt**0.5
     for nd in p:
          if nt%nd == 0:
               break
          elif nd > r:
               p = p+[nt]
               print(nt)
               break
     nt+=1
end=time.time()
print(str(lim)+ " primos em ",end-s)
a=input();

     
