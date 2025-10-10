import logging
import os
import pandas as pd
from traceback import format_exc
from src.Model.emal_transportadora import email_transportadora
from src.Model.armazenamento import pegar_dados,alterar_dados
from dotenv import load_dotenv
from datetime import date

import gspread as gs
import gspread_dataframe as gsd
import pyautogui as p

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
    # gc = gs.service_account(os.getenv("Crendeciais"))
    # workbook = gc.open_by_key(os.getenv("Id_planilha"))
    # sheet = workbook.worksheet("Desenvolvimento")
    # df_planilha_online = pd.DataFrame(sheet.get_all_records())
    df_planilha_online = pd.read_excel(r"C:\RPA\RPA-ACOMPANHAMENTO-DE-ENTREGA2\vamos.xlsx").fillna("")
    




    df_filtrado_por_nao_feitos = df_planilha_online.loc[df_planilha_online['Finalizado'] == ""]

    df_planilha_dados_Entragas = pd.read_excel(r"C:\RPA\RPA-ACOMPANHAMENTO-DE-ENTREGA2\planilha_rota_entregas.xlsx")
    data_atual = date.today().strftime("%d/%m/%Y")
    print(df_planilha_dados_Entragas)
    for dp in range(len(df_filtrado_por_nao_feitos.index)):
        p.alert(df_filtrado_por_nao_feitos["Nr. nota"][dp])
        df_busca = df_planilha_dados_Entragas.loc[df_planilha_dados_Entragas["notaFiscal"] == df_filtrado_por_nao_feitos["Nr. nota"][dp]]
        print(df_busca)
        if not df_busca.empty:
            print("entrou aqui")
            transportadora = df_busca["Transportadora"][0]
            previsao_entrega = df_busca["previsaoEntrega"][0]
            data_entrega = df_busca['dataEntrega'][0]
            if previsao_entrega == "":
                print("sem previsao de entrega")
            else:
                
                
            

        
        else:
            df_filtrado_por_nao_feitos["Transportadora"][dp] = "NÃO ENCONTRADO"
            alterar_dados("sem_transportadoreS", df_filtrado_por_nao_feitos["Nr. nota"][dp])











    # df_entraga_pela_matriz = df_filtrado_por_nao_feitos[df_filtrado_por_nao_feitos["Unidade de negócio"].isin(["Entrega Matriz", "Retira Matriz"])] 

    # df_transportadora = df_filtrado_por_nao_feitos[~df_filtrado_por_nao_feitos["Unidade de negócio"].isin(["Entrega Matriz", "Retira Matriz"])]    

    
    
  

  


    


except:
    print("Erro ao tenta se conectar com google planilha")
    logging.info("Erro ao tenta se conectar com google planilha")
    print(format_exc())