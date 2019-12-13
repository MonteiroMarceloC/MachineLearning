import matriz
l=int(input("Quantas linhas: "))
c=int(input("Quantas colunas: "))
m=matriz.cria(l,c)
matriz.imprime(m)
pivo=max(m)[0] #Achar o pivo
mult=[] #Matriz de multiplicadores
for i in range(l):
    mult.append(m[i][0]/pivo)
print(mult)

