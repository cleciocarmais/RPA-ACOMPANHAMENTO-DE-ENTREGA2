import json
from dotenv import load_dotenv
import os





load_dotenv()
def pegar_dados(tipo_dados):
    with open(f"{os.getenv('RAIZ')}armazenamentos.json", 'r') as file:
        dados = json.load(file)
    return dados[tipo_dados]



def alterar_dados(chave, valos):
    with open(f"{os.getenv('RAIZ')}armazenamentos.json", 'r') as file:
        dados = json.load(file)
    print(valos)
    dados[chave].append(valos)

    with open(f"{os.getenv('RAIZ')}armazenamentos.json", 'w') as file:
        json.dump(dados, file, indent=4)


# alterar_dados("codigos_feitos", {"ID" : "teste", "condo" : "ola"})
# codigos_feitos

# pegar_dados("codigos_feitos")