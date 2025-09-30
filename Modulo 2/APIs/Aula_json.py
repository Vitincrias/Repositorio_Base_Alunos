import json
dados_json = '{"nome":"Vitor", "idade":15, "Cidade":"São paulo"}'
dados_json = json.loads(dados_json)

print(dados_json["nome"])
print(dados_json["idade"])
print(dados_json["Cidade"])

pythonValue = {'Floquinho': True, 'Cor': "Branco", 'Estado' : "animado", 'Peso': "1.4 - 3.2 kg",'Comida predileta': "Ração", 'Gênero': "Macho", 'Cor do olhos': "Azuis", 'Comportamento': "Extremamente dócil", 'Possui filhos:': False, 'Identifica como': "Therian"} 

pythonOfjsonData = json.dumps(pythonValue)
print(pythonOfjsonData)