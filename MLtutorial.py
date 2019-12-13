from sklearn import tree
''' X vai ser aidade da pessoa e qual ano do
ensino médio´a pessoa está.
	Y vai dizer se a pesoa é maior ou menor de idade
'''
X = [[16,1],[18,2],[15,2],[19,1],[17,3]]
Y=[['m'],['M'],['m'],['M'],['m']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

play = True
while play:
	idade = int(input('Digite sua idade: '))
	ano = int(input('Digite seu ano: '))
	resposta = clf.predict([idade,ano])
	print('A resposta é: ' + str(resposta))

	#Verificando
	foi_bom = input('Foi uma boa resposta? ')
	if foi_bom.lower() in ['sim','s','yes','y']:
		X+=[[idade,ano]]
		Y+=[[resposta]]
	else:
		resposta = input('Qual a melhor resposta? 0- menor 1-maior')
		if resposta == '0':
		X+=[[idade,ano]]
		Y+=[['m']]
		elif resposta == '1':
		X+=[[idade,ano]]
		Y+=[['M']]
	continuar = input('Deseja continuar? ')
	if continuar.lower() in ['não','nao','n','no']:
		play=False
 