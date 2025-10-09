import pandas as pd
import logging



def tratar_planilhas():
    print("Lendo planilhas")
    logging.info("Lendo planilhas")
    #LENDO PLANILHA BRINX
    df_bridex = pd.read_csv(r"D:\RPA\RPA_ACOMPANHAMENTO_ENTREGAS_2\brindx\MJ_5.csv", delimiter=";")
    df_bridex = df_bridex[["notaFiscal","previsaoEntrega","dataEntrega","nomeOcorrencia"]]
    df_braspres = pd.read_excel(r"D:\RPA\RPA_ACOMPANHAMENTO_ENTREGAS_2\braspress\export_minhas_encomendas_01-09-2025_19-09-2025 (1).xlsx",skiprows=6)
    index = len(df_braspres.index)
    index2 = index - 14
    df_braspres = df_braspres[:index2]
    df_braspres.to_excel("teste.xlsx")


if __name__ == "__main__":
    tratar_planilhas()