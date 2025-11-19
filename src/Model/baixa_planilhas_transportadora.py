from src.Model.Transpor_Controlog import transportadora_controlog
from src.Model.Tranpor_brindx import transportadora_bridex
from src.Model.Transpor_braspres import transportadora_braspres


def baixa_planilhas_transportadoras(*transportadores):
    """
        Recebe nome das empresa para gegar os relatorios
    
    
    """
    listas_funcoas_transpordoras = {
        "braspres" : transportadora_braspres,
        "controlog" : transportadora_controlog,
        "bridex" : transportadora_bridex
    }

    for transpo in transportadores:
       funcao =  listas_funcoas_transpordoras[transpo]
       funcao()

if __name__ == "__main__":
    baixa_planilhas_transportadoras("controlog")