import random
n=int(input("Digite a largura: "))
m=int(input("Digite a altura: "))
m
with open("f.txt","w") as f:
    for i in range(n):
        for j in range(m):
            n=random.randint(0,i)
            m[i][j] = n
            print (n)

