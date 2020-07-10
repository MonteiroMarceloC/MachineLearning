from sklearn import tree

#Iniciando básico
X=[]
Y=[]
O = input("Respostas: ").split()
I = input("Perguntas: ").split()
numEx = int(input("Número de exemplos iniciais: "))
X+=[[]]*numEx
maxErros = 3

#Pegando exemplos
for n in range(numEx):
	print ('\nExemplo'+str(numEx)+'...')
	for i in I:
		X[n] += [input(str(i)+': ')]
	Y+=input('Output: ')
	print(X)
	print(Y)
	#validar Y

