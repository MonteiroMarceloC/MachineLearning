from sklearn import tree

O = input("Possibles outputs: ").split()
I = input("Necessary inputs: ").split()
sizeI = len(I)
sizeO = len(O)
sizeD = int(input("How many exemples: "))
X,Y=[],[]

#Input exemples
for e in range(sizeD):
	print("Exemple "+str(e+1)+"...")
	ex = []
	for i in range(sizeI):
		ex += [int(input(I[i]+": ")) ]
	o1 = input("Output: ")

	#Test Output
	while (o1 not in O):
		print ("Incorrect output. Outputs can be:", end = ' ')
		for o in range(sizeO):
			print(str(O[o]), end = ' ')
		print('\n')
		o1 = input("Output: ")
	Y += [o1]
	X += [ex]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

cont=0
play = True
while(play):

	#New input
	print("Add input...")
	newi = []
	for i in range(sizeI):
		newi += [int(input(I[i]+": "))]
	newo = clf.predict([newi])
	print ("I think output is " + newo[0]) #0 pois só há 1 elemento no output, caso o output seja composto, tirar o [0]

	#Check output
	r = input("Output ok? (1 for Yes. 0 for No) ")
	while(r not in ['0','1']):
		print("Incorrect. Please type 1 or 0.")
		r = input("Output ok? (1 for Yes. 0 for No) ")
	if(r=='1'):
		X += [newi]
		Y.append(newo[0]) #idem
		clf = clf.fit(X,Y)
	elif(r=='0'):
		cont+=1
		print(cont)
		newo=input("What is the best output? ")

		#validar novo output
		while (newo not in O):
			print ("Incorrect output. Outputs can be:", end = ' ')
			for o in range(sizeO):
				print(str(O[o]), end = ' ')
			print('\n')
			newo = input("What is the best output? ")

		X += [newi]
		Y.append(newo) #idem
		clf = clf.fit(X,Y)

		#adicionar novo input em caso de 3 erros
		if cont>1:
			cont = 0
			newinp= input("Please, add one more input: ")
			I+= [newinp]
			sizeI +=1
			print("Now, this input for the past outputs...")
			for i in range(len(Y)):
				aux = input(str(Y[i])+" -> "+str(X[i])+" "+newinp+": ")#criar código com todos os campos
				X[i]+=[int(aux)]
			print(X)
			clf = clf.fit(X,Y)

	#Run again
	r2 = input("Thanks! Keep running? (1 for Yes. 0 for No) ")
	while(r2 not in ['0','1']):
		print("Incorrect. Please type 1 or 0.")
		r2 = input("Keep running? (1 for Yes. 0 for No) ")
	if(r2=='0'):
		play = False
fim = input("End of program. ")

#save or upload data
#test if there is at list one for each output
