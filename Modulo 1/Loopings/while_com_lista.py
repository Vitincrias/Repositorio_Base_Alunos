L=[]
while True:
    n=(input("Digite uma cor: "))
    if n==("stop"):
        break
    L.append(n)
    
x=0
while x < len(L):
    x=x+1
print(L)
    