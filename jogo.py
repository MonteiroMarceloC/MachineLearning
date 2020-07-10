#Collecting data
start = "a"
while start!=" ":
    start = input("Pressione espaço e enter para começar...")
print("Inicializando sistema")
nome = input("Qual o seu nome? ")
if " " not in nome:
    print(nome+" de que?")
    snome = input()
    if nome not in snome and nome.lower() not in snome:
        nome= nome+" "+snome
    else:
        nome = snome
print("Olá "+nome+". Sou IAM. Vamos jogar um jogo?\n\t1- Sim\n\t2- Não")
r=[0,0,0,0,0,0,0,0,0,0]
n=1
r[n]=input()
if r[1]==1:
    while (n<10):
        n=n+1
        r[n]=input("Escolha um desses números:\n\t1- "+ 2*r[n-1] +"\n\t2- "+2*r[n-2]+1)
        print("Obrigado. Agora...")

else:
    print("Blz. Flw "+nome)
    
print("Fim do jogo, por enquanto")
