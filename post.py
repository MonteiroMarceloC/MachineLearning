#primos1
import time, sys
numero=int(input("Quantos primos você quer? "))
lim=numero-1
time.sleep(3)
p=[]
p.append(2)
p.append(3)
nt=5
start = time.time()
while len(p)<lim:
    i=0
    nd=2
    b=True
    r=nt**(0.5)
    for nd in p:
        if nt%nd==0:
            b=False
            break
    if b:
        print(nt)
        p.append(nt)
    nt=nt+1
end = time.time()
print(str(numero)+ " primos encontrados em "+str(end-start)+" segundos.")
    
    

    
