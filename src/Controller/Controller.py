import logging
import os
import pandas as pd
from traceback import format_exc
from src.Model.emal_transportadora import email_transportadora
from dotenv import load_dotenv

import gspread as gs
import gspread_dataframe as gsd

load_dotenv()


with open(f"{os.getenv('RAIZ')}log.txt", "w") as file:
    pass

logging.basicConfig(
    filename=f"{os.getenv('RAIZ')}log.txt",  # Use raw string (r"") para evitar erro com "\"
    filemode="a",  # Adiciona ao final do arquivo
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato da mensagem
    datefmt="%d/%m/%Y %H:%M:%S",  # Formato da data e hora
    level=logging.INFO  # Nível mínimo das mensagens que serão registradas
)

logging.info("Iniciando Processo de acompanhamento de entrega")
print("Iniciando Processo de acompanhamento de entrega")

try:
    #CONECTANDO A PLANILHA
    gc = gs.service_account(os.getenv("Crendeciais"))
    workbook = gc.open_by_key(os.getenv("Id_planilha"))
    sheet = workbook.worksheet("Desenvolvimento")
    df_planilha_online = pd.DataFrame(sheet.get_all_records())
    df_filtrado_por_nao_feitos = df_planilha_online.loc[df_planilha_online['Finalizado'] == ""]

    df_planilha_dados_Entragas = pd.read_excel("C:\RPA\RPA-ACOMPANHAMENTO-DE-ENTREGA2\planilha_rota_entregas.xlsx")
    for dp in range(len[df_filtrado_por_nao_feitos.index]):
        df_busca = df_planilha_dados_Entragas.loc[df_planilha_dados_Entragas["notaFiscal"] == dp["Nr. nota"][dp]]
        if not df_busca.empty:
            print("tem")
        else:
            print("nao tem ")










    # df_entraga_pela_matriz = df_filtrado_por_nao_feitos[df_filtrado_por_nao_feitos["Unidade de negócio"].isin(["Entrega Matriz", "Retira Matriz"])] 

    # df_transportadora = df_filtrado_por_nao_feitos[~df_filtrado_por_nao_feitos["Unidade de negócio"].isin(["Entrega Matriz", "Retira Matriz"])]    

    
    
  

  


    


except:
    print("Erro ao tenta se conectar com google planilha")
    logging.info("Erro ao tenta se conectar com google planilha")
    print(format_exc())