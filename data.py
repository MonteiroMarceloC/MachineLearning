mind={}
t=True
while(t):
    r=input('1- Adc \n2-Pesquisar\n3- Sair\n')
    if (r=='1'):
        v = input().split()
        for i in range((len(v)-1)):
            mind[v[i]]=v[i+1]
            mind[v[i+1]]=v[i]
    elif (r=='2'):
        r1 = input('Digite uma palavra chave')
        if (r1 in mind):
            print(r1 +' --- ' + mind[r1])
        else:
            print("Not in mind.")
    elif (r=='3'):
        t = False
    else:
        print('Digite uma dentre as opções 1, 2 ou 3')

    
