from sklearn import tree

#Iniciando básico
X=[]
Y=[]
O = input("Respostas: ").split()
I = input("Perguntas: ").split()
numEx = int(input("Número de exemplos iniciais: "))
maxErros = 2

#Pegando exemplos
for n in range(numEx):
	print ('\nExemplo'+str(n+1)+'...')
	X+=[[]]
	for i in I:
		X[n] += [input(str(i)+': ')]
	Y+=[input('Output: ')]
	#validar Y
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

#Iniciando testes
play = True
erros = 0
while (play):
	#Adicionar input
	if erros > maxErros:
		print('\nO sistema alcançou o '+str(maxErros)+'º erro.')
		addI = input('Adicionar novo input: ')
		print('Autualizar exemplos...')
		for a in X:
			print(str(a)+' -> '+str(Y[X.index(a)]))
			a += [input(addI+": ")]
		I+=[addI]
		print('Input adicionado')
		print(X)
		print(Y)
		clf = clf.fit(X,Y)
		erros = 0

	print('\nIniciando teste...')
	addX = []
	for i in I:
		addX += [input(str(i)+': ')]
	addY = clf.predict([addX])
	print('Resposta: '+str(addY[0]))

	#Verificando resposta
	res = input('Foi uma boa resposta? ')
	if not res.lower() in ['sim','s','sim.']:
		erros+=1
		addY=input('Qual a melhor resposta? ')
		#validar Y
	X+=[addX]
	Y+=[addY[0]]
	print(X)
	print(Y)
	clf = clf.fit(X,Y)

	on = input('Deseja continuar? ')
	if not on.lower() in ['sim','s','sim.']:
		play=False
print('Programa finalizado.')
#Deseja salvar em arquivo?