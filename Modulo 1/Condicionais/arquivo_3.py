import os
print (os.getcwd())

#os.mkdir("d")
#os.mkdir("e")
#os.mkdir("f")

def plmds():
    arquivo_path = ""
    try:
        os.rmdir(arquivo_path)
        print(f"""\033[0;32m Pasta '{arquivo_path}'
            removida com sucesso! ;D""")
    except FileNotFoundError:
        print(f"""\033[0;33m Pasta '{arquivo_path}'
    não encontrada... @@""")
    except OSError:
        print(f"""\033[0;34m '{arquivo_path}'
    é um arquivo, não uma pasta!!! + +""")
    
try:
    for n in range(1,51):
        os.mkdir("pasta_%d" % n)
        os.chdir("pasta_%d" % n)
    arquivo = open ("arquivo_1.txt", "w")
    arquivo.write("Oi")
    arquivo.close()
except FileNotFoundError:
    print('Arquivo não encontrado!')