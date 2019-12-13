items=list('abcde')
#cant have equalnames
users=['ana','bob','car','dog']
# ana: a,b->bob | bob: a,d,c-> car |...| dog: e->a
marks=[[5,4,0,0,0],[5,0,0,4,0],[0,0,0,4,5],[0,5,0,0,4]

user0='dog' #recebe o valor do usuário atual
ind0=users.idenx(user0)

o_users=users[:]
o_users.remove(user0)

#mapeanddo user0 (matriz de 5s, 4s, 3s, 2s, 1s e 0s)
marks0 = [['a'],['b'],[],[],[],[]]

#quem são os mais parecidos com user0
'''
pontos = u0mark - unmark

'''
pontos = [0 for u in users]
u=0
for m in marks:
	if not marks.index(m) == ind0:
		for i in items:
			pontos[u]+= m[items.index(i)]-
		pontos[u]+=[[]]


#quais filmes user0 não viu, mas essa galera viu?