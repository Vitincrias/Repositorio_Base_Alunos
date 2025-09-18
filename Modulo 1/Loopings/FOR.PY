L=[8, 9, 15, 16, 17, 22, 60, 79, 48, 99]
for vitor in L:
    print(vitor)
        
def pprt():
    L=["apple", "pears", "kiwis"]
    for s in L:
        for letra in s:
            print(letra)

def acaba_pelo_amor_de_deus():
    L=[1, 7, 2, 4, 9, 17, 23, -2, 200, -900]
    máximo=L[0]
    for e in L:
        if e > máximo:
            máximo = e
    print(máximo)        
    
def mn_para():
    L=[1, 7, 2, 4, 9, 17, 23, -2, 200, -900]
    menor=L[0]
    for e in L:
        if e < menor:
            menor = e
    print(menor)    
    
# for v in range(11):
#    print(v)
    
# for v in range(5, 8):
#    print(v)

# for t in range(3, 33, 3):
#    print(t, end=" ")

def shiny():
    Nome= "Vitor"
    Idade= 15
    Dinheiro= 51.34
    print("%20s tem %010d anos e R$%f no bolso." % (Nome, Idade, Dinheiro))
    print("%12s tem %03d anos e R$%5.2f no bolso. " % (Nome, Idade, Dinheiro))
    print("%-12s tem %-3d anos e R$%-5.2f no bolso. " % (Nome, Idade, Dinheiro))

def divide(x,y):
    try:
     result = x/y
    except ZeroDivisionError:
        print ("Por favor, não utilize zeros!")
    except :
        print("\033[91m Algo deu errado ... ")
    else:
        print (f"Seu resultado é: {result}")
    finally:
      print ("\033[92m Vamos de novo?")
divide(13,13)
divide(100,-5)
divide("A", "B")

