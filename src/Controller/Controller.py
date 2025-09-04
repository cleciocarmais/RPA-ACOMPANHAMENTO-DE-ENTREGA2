import logging
import os
import pandas as pd
from traceback import format_exc
from src.Model.emal_transportadora import email_transportadora
from dotenv import load_dotenv

import gspread as gs
import gspread_dataframe as gsd

load_dotenv()


with open(f"{os.getenv("RAIZ")}log.txt", "w") as file:
    pass

logging.basicConfig(
    filename=f"{os.getenv("RAIZ")}log.txt",  # Use raw string (r"") para evitar erro com "\"
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

    for index in range(len(df_planilha_online.index)):

        if df_planilha_online["Status"][index] == "":
            print(f"Processando linha N° {index}")
            logging.info(f"Processando linha N° {index}")
            if df_planilha_online["Transportadora"][index] != "":
                if df_planilha_online["Status"][index] in ["", "NÃO COLETADO"]:
                    print("Pesquisa codigo na empresa")

                if df_planilha_online["Status"][index] == "Não coletado":
                    print("Pesquisa novamente")

                if df_planilha_online["Status"] == "EM ANDAMENTO":
                    print("Fazer um if para verificar a data de entraga")

                if df_planilha_online["Status"] == "Atrasado":
                    print("Enviar email para")
                    

            else:
                print(f"Pedido N° {df_planilha_online["Nr. nota"][index]} sem transportadora")
                logging.info(f"Pedido N° {df_planilha_online["Nr. nota"][index]} sem transportadora")
                email_transportadora()
                continue


    


except:
    print("Erro ao tenta se conectar com google planilha")
    logging.info("Erro ao tenta se conectar com google planilha")
    print(format_exc())