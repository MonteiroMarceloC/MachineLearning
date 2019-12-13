import math
def f(x):
    return 2*x+5

def f1(x):
    return x
def f2(t):
    e = math.e
    return 80*e**(-2*t) + 20*e**(-0.1*t) -10

def f3(t):
    e = math.e
    return -160*e**(-2*t) -2*e**(-0.1*t)

def MN():
    print('Começando o método de Newton...')
    x0 = float(input('x0: '))
    e = float(input('e: '))
    m = float(input('Número máximo de iterações: '))

    Fx ,DFx,x,i =  f(x0),f1(x0),x0,0
    d = Fx/DFx
    x = x-d
    while((abs(d) > e or abs(Fx)>e)and i<m  and not DFx==0):
        Fx , DFx = f(x),f1(x)
        d = Fx/DFx
        x ,i= x-d,i+1
        print ('x: '+str(x),'    Fx: '+str(Fx)+'    d: '+str(d))
    if (DFx == 0 or abs(Fx)>e or abs (d)>e):
        print('Error')
    else:
        print ('A raiz é: '+str(x))

def MB():
    print("Começando métod da Bisceção...")
    a=float(input('a: '))
    b=float(input('b: '))
    e=float(input('e: '))
    m=int(input('número máximo de iterações: '))
    x=0
    Fa = f(a)
    Fb=f(b)
    if(Fa*Fb>0):
        print("Erro: Sinal não muda")
    elif(Fa==0 or Fb==0):
        print("a ou b são raizes")
    else:
        d=abs((b-a)/2)
        i=0
        while(d >e and i < m):
            x=(a+b)/2
            Fx = f(x)
            if (Fa * Fx >0):
                a,Fa = x,Fx
            else:
                b=x
            d,i = d/2,i+1
            print('x: '+str(x),'    Fx: '+str(Fx)+'    d: '+str(d))
    print ('A raiz é: '+str(x))


MB()
