def scrr():
    N = int(input("Tabuada de: "))
    X = 1

    while X <= N:         
        print(N, "x", X,"=", N*X)
        X=X+1  
        
def gg():
    s=0
    while True:
     v=int(input("Digite um número a somar ou 0 para sair: "))
     if v==0:
        break
        s= s+v
    print(s)    
