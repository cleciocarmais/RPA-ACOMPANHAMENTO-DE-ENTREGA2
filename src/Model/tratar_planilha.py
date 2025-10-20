import pandas as pd
import logging



def tratar_planilhas():
    print("Lendo planilhas")
    logging.info("Lendo planilhas")
    #LENDO PLANILHA BRINX matriz
    df_bridex = pd.read_csv(r"D:\RPA\RPA_ACOMPANHAMENTO_ENTREGAS_2\brindx\MJ_7.csv", delimiter=";")
    #Filtrar colunas desejadas 
    df_bridex["Transportadora"] = "bridex"
    df_bridex = df_bridex[["notaFiscal","previsaoEntrega","dataEntrega","nomeOcorrencia", "Transportadora"]]

    #Tratando coluna notaFiscal
    df_bridex["notaFiscal"] = [str(x.replace(" ","")[-6:]) for x in df_bridex["notaFiscal"]]

    ######################################## BRiDX FILIAL
    df_bridex_filial = pd.read_csv(r"D:\RPA\RPA_ACOMPANHAMENTO_ENTREGAS_2\bridx_filial\MJ_3.csv", delimiter=";")
    #Filtrar colunas desejadas 
    df_bridex_filial["Transportadora"] = "bridex"
    df_bridex_filial = df_bridex_filial[["notaFiscal","previsaoEntrega","dataEntrega","nomeOcorrencia", "Transportadora"]]

    #Tratando coluna notaFiscal
    df_bridex_filial["notaFiscal"] = [str(x.replace(" ","")[-4:]) for x in df_bridex_filial["notaFiscal"]]
    ############################################ BRASPRES ##########################################################
    df_braspres = pd.read_excel(r"D:\RPA\RPA_ACOMPANHAMENTO_ENTREGAS_2\braspress\export_minhas_encomendas_01-10-2025_20-10-2025.xlsx", skiprows=6)
    index2 =  len(df_braspres.index) - 14

    df_braspres = df_braspres[:index2]
    df_braspres["NOTA FISCAL"] = [str(x.replace(",","")) for x in df_braspres["NOTA FISCAL"]]
    df_braspres["Transportadora"] = "braspres"

    df_braspres = df_braspres[["NOTA FISCAL","PREVISÃO DE ENTREGA ORIGINAL","PREVISÃO DE ENTREGA","ULTIMA OCORRÊNCIA","Transportadora"]]
    df_braspres = df_braspres.rename(columns={
        "NOTA FISCAL" : "notaFiscal",
        "PREVISÃO DE ENTREGA ORIGINAL" :"previsaoEntrega",
        "PREVISÃO DE ENTREGA": "dataEntrega",
        "ULTIMA OCORRÊNCIA" : "nomeOcorrencia"

    })

    ####################################### CONTROLOG #######################33
    df_controlog = pd.read_csv(r"controlog/Controlog_Relatorio_Cargas_e_Entregas_18_10_2025_168f38b7202105.csv",delimiter=";",encoding="latin1")
    df_controlog["Transportadora"] = "Controlog"
    df_controlog.columns = (
    df_controlog.columns
    .str.replace(r'\s+', ' ', regex=True)  # substitui múltiplos espaços por um
    .str.strip()                           # remove espaços do início/fim
)
    df_controlog = df_controlog[["Nota Fiscal","Data Carga","Data Entrega","Obs","Transportadora"]]
    df_controlog["Data Carga"] = [str(x.replace(" ","")[:-8]) for x in df_controlog["Data Carga"]]
    df_controlog["Data Entrega"] = [str(x.replace(" ","")[:-8]) for x in df_controlog["Data Entrega"]]
    df_controlog["Data Entrega"] = [str(x.replace("A","")) for x in df_controlog["Data Entrega"]]

    df_controlog = df_controlog.rename(columns={
        "Nota Fiscal" : "notaFiscal",
        "Data Carga" :"previsaoEntrega",
        "Data Entrega": "dataEntrega",
        "Obs" : "nomeOcorrencia"
    })
  


    
    planilha_concat = pd.concat([df_braspres, df_bridex,df_bridex_filial,df_controlog], ignore_index=False)
    planilha_concat.to_excel(r"D:\RPA\RPA_ACOMPANHAMENTO_ENTREGAS_2\planilha_rota_entregas.xlsx", index=False)


if __name__ == "__main__":
    tratar_planilhas()
