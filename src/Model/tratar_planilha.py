import pandas as pd
import logging



def tratar_planilhas():
    print("Lendo planilhas")
    logging.info("Lendo planilhas")
    #LENDO PLANILHA BRINX
    df_bridex = pd.read_csv(r"C:\RPA\RPA-ACOMPANHAMENTO-DE-ENTREGA2\brindx\MJ_5.csv", delimiter=";")
    #Filtrar colunas desejadas 
    df_bridex = df_bridex[["notaFiscal","previsaoEntrega","dataEntrega","nomeOcorrencia"]]

    #Tratando coluna notaFiscal
    df_bridex["notaFiscal"] = [str(x.replace(" ","")[-4:]) for x in df_bridex["notaFiscal"]]

    df_braspres = pd.read_excel(r"C:\RPA\RPA-ACOMPANHAMENTO-DE-ENTREGA2\braspress\export_minhas_encomendas_01-09-2025_19-09-2025 (1).xlsx", skiprows=6)
    index2 =  len(df_braspres.index) - 14

    df_braspres = df_braspres[:index2]
    df_braspres["NOTA FISCAL"] = [str(x.replace(",","")) for x in df_braspres["NOTA FISCAL"]]

    df_braspres = df_braspres[["NOTA FISCAL","PREVISÃO DE ENTREGA ORIGINAL","PREVISÃO DE ENTREGA","ULTIMA OCORRÊNCIA"]]
    df_braspres = df_braspres.rename(columns={
        "NOTA FISCAL" : "notaFiscal",
        "PREVISÃO DE ENTREGA ORIGINAL" :"previsaoEntrega",
        "PREVISÃO DE ENTREGA": "dataEntrega",
        "ULTIMA OCORRÊNCIA" : "nomeOcorrencia"

    })
    planilha_concat = pd.concat([df_braspres, df_bridex], ignore_index=False)
    planilha_concat.to_excel(r"C:\RPA\RPA-ACOMPANHAMENTO-DE-ENTREGA2\planilha_rota_entregas.xlsx", index=False)


if __name__ == "__main__":
    tratar_planilhas()
