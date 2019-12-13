def cria(num_linhas, num_colunas):

    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: "))
            linha.append(valor)

        matriz.append(linha)
    return matriz

def imprime(matriz):

    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas - 1):
                print("%d" %matriz[i][j])
            else:
                print("%d" %matriz[i][j], end = " ")
    print()

def SS(m,v):
    #Validação da entrada (quadrada e triangular inf, vetor mesmo tam)
    r[0] = v[0]/m[0]
    for i in range(1,len(m)):
        aux= v[i]
        for j in range(i):
            aux = aux - m[i][j]*v[j]
        r[i] = aux/m[i][i]
    return r
            
def SR(m,v):
    l = len(m)
    #Validação da entrada (quadrada e triangular sup, vetor mesmo tam)
    r[l-1] = v[l-1]/m[l-1]
    for i in range(l-2, -1, -1): #criar um rengeneg
        aux = v[i]
        for j in range(l-1,i,-1):
            aux = aux - m[i][j]*v[j]
        r[i] = aux/m[i][i]
    return r

def EG
def LU
def CH
