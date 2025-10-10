import json



def pegar_dados(tipo_dados):
    with open(r"C:\RPA\RPA-ACOMPANHAMENTO-DE-ENTREGA2\armazenamentos.json", 'r') as file:
        dados = json.load(file)
    return dados[tipo_dados]

def alterar_dados(chave, valos):
    with open(r"C:\RPA\RPA-ACOMPANHAMENTO-DE-ENTREGA2\armazenamentos.json", 'r') as file:
        dados = json.load(file)

    dados[chave].append(valos)

    with open(r"C:\RPA\RPA-ACOMPANHAMENTO-DE-ENTREGA2\armazenamentos.json", 'w') as file:
        json.dump(dados, file, indent=4)


alterar_dados("codigos_feitos", "teste")
# pegar_dados("codigos_feitos")