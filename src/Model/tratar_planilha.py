import pandas as pd
import logging
import os
from traceback import format_exc
def tratar_planilhas():
    dataframes = []
    # #LENDO PLANILHA BRINX matriz ##################################################################################
    try:
        print("LENDO PLANILHA DA BRINX MATRIZ")
        logging.info("LENDO PLANILHA DA BRINX MATRIZ")
        df_bridex = pd.read_excel(f"{os.getenv('RAIZ')}brindx\\planilha_brindx.xlsx")
        #Filtrar colunas desejadas 
        df_bridex["Transportadora"] = "bridex"
        df_bridex = df_bridex[["notaFiscal","previsaoEntrega","dataEntrega","nomeOcorrencia", "Transportadora"]]

        #Tratando coluna notaFiscal
        df_bridex["notaFiscal"] = [str(x.replace(" ","")[-6:]) for x in df_bridex["notaFiscal"]]





        ######################################## BRiDX FILIAL ##############################################################
        print("LENDO PLANILHA DA BRINX MATRIZ")
        logging.info("LENDO PLANILHA DA BRINX MATRIZ")
        df_bridex_filial = pd.read_excel(f"{os.getenv('RAIZ')}brindx_filial\\planilha_brindx_filial.xlsx")
        #Filtrar colunas desejadas 
        df_bridex_filial["Transportadora"] = "bridex"
        df_bridex_filial = df_bridex_filial[["notaFiscal","previsaoEntrega","dataEntrega","nomeOcorrencia", "Transportadora"]]

        #Tratando coluna notaFiscal
        df_bridex_filial["notaFiscal"] = [str(x.replace(" ","")[-4:]) for x in df_bridex_filial["notaFiscal"]]
        dataframes.append(df_bridex)
        dataframes.append(df_bridex_filial)
    except:
        print(format_exc())
        pass




    ########################################### BRASPRES ##########################################################
    try:
        print("LENDO PLANILHA BRASPRES")
        logging.info("LENDO PLANILHA BRASPRES")
        df_braspres = pd.read_excel(f"{os.getenv('RAIZ')}braspress\\planilha_braspres.xlsx", skiprows=6)
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
        dataframes.append(df_braspres)
    except:
        print(format_exc())
        logging.error(format_exc())
        pass

    ####################################### CONTROLOG #######################33########################################################
    try: 
        print("Lendo planilha da controlog")
        logging.error("Lendo planilha da controlog")
        df_controlog = pd.read_excel(f"{os.getenv('RAIZ')}controlog\\planilha_controlog.xlsx")
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
        dataframes.append(df_controlog)
    
    except:
        print(format_exc())
        logging.error(format_exc())

    
    planilha_concat = pd.concat(dataframes, ignore_index=False)
    planilha_concat.to_excel(f"{os.getenv('RAIZ')}planilha_rota_entregas.xlsx", index=False)


if __name__ == "__main__":
    tratar_planilhas()
