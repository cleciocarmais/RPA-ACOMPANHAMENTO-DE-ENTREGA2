import logging
import os
import pandas as pd
from traceback import format_exc
from src.Model.email_transportadora import email_transportadora
from src.Model.armazenamento import alterar_dados, pegar_dados
from src.Model.mandar_email import enviar_email, enviar_email_transporadora
from src.Model.braspress import brasspress
from src.Model.Controlog import transportadora_controlog
from src.Model.bridex import transportadora_bridex
from dotenv import load_dotenv
from datetime import date, datetime
from src.Model.tratar_planilha import tratar_planilhas

import gspread as gs
import gspread_dataframe as gsd
import pyautogui as p

load_dotenv()


with open(f"{os.getenv('RAIZ')}log.log", "w") as file:
    pass

logging.basicConfig(
    filename=f"{os.getenv('RAIZ')}log.log",  # Use raw string (r"") para evitar erro com "\"
    filemode="a",  # Adiciona ao final do arquivo
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato da mensagem
    datefmt="%d/%m/%Y %H:%M:%S",  # Formato da data e hora
    level=logging.INFO  # Nível mínimo das mensagens que serão registradas
)

logging.info("Iniciando Processo de acompanhamento de entrega")
print("Iniciando Processo de acompanhamento de entrega")

# df_planilha_online = pd.read_excel(f"{os.getenv('RAIZ')}vamos.xlsx").fillna("")
try:
    # #CONECTANDO A PLANILHA
    gc = gs.service_account(os.getenv("Crendeciais"))
    workbook = gc.open_by_key(os.getenv("Id_planilha"))
    sheet = workbook.worksheet("Desenvolvimento")
    df_planilha_online = pd.DataFrame(sheet.get_all_records())
    brasspress() 
    p.sleep(2)
    transportadora_controlog()
    p.sleep(2) 
    transportadora_bridex()
    p.alert("GERANDO RELATORIO DE TRANSPORTADORA")
    tratar_planilhas()
    # p.alert("GERADO PLANILHA DE DADOS PARA CONSULTA")

    pd.options.mode.chained_assignment = None
    df_planilha_dados_Entragas = pd.read_excel(f"{os.getenv('RAIZ')}planilha_rota_entregas.xlsx")
    data_atual = date.today()
   

    for dp in range(len(df_planilha_online.index)):
        if df_planilha_online["Finalizado"][dp] == "":


            print(f"LInha : {dp}")
            #PESQUISA NUMERO DA NOTA QUEM VEM DA PLANILHA NA PLANILHA DE DADOS.
            df_busca = df_planilha_dados_Entragas.loc[df_planilha_dados_Entragas["notaFiscal"] == df_planilha_online["Nr. nota"][dp]].fillna("")          
            #VEIRIFICAR SE PLANILHA NÃO ESTAR VAZIA
            if not df_busca.empty:
               
      
                index_busca = df_busca.index[0]
                
                #VERIFICAR SE CAMPO DE PRECISA DE ENTREGA NÃO VAZIO
                if df_planilha_online['Previsão de Chegada'][dp] != "":
                    data_previsao =  df_planilha_online["Previsão de Chegada"][dp]
                    data_previsao = datetime.strptime(data_previsao,"%d/%m/%Y").date()
                    print("Verificando Previsao de Entrega")
                    logging.info("Verificando Previsao de Entrega")
                    
                    if df_busca["dataEntrega"][index_busca] != "":
                        if df_planilha_online["Previsão de Chegada"][dp] == df_busca["dataEntrega"][index_busca]:
                            print("Pedido entregue na data correta")
                            logging.info("Pedido entregue na data correta")
                            df_planilha_online["Finalizado"][dp] = "Sim"
                            df_planilha_online["Status"][dp] = "ENTREGUE"
                            df_planilha_online["Observação"][dp] = str(df_busca["nomeOcorrencia"][index_busca])
                            df_planilha_online["Data da entrega"][dp] = df_busca["dataEntrega"][index_busca]
                            alterar_dados("codigos_feitos", {
                            "Nota" : str(df_planilha_online["Nr. nota"][dp]),
                            "Representante da venda" : str(df_planilha_online["Representante da venda"][dp]).strip(),
                            "Observacao" : str(df_busca["nomeOcorrencia"][index_busca]),
                            "Status" : "ENTREGUE"
                        })
                        else:
                            print("Entrega realizada com atrasado")
                            logging.info("Entrega realizada com atrasado")
                            df_planilha_online["Finalizado"][dp] = "sim"
                            df_planilha_online["Status"][dp] = "ENTREGUE COM ATRASO"
                            df_planilha_online["Observação"][dp] = str(df_busca["nomeOcorrencia"][index_busca])

                            df_planilha_online["Data da entrega"][dp] = df_busca["dataEntrega"][index_busca]
                            
                            alterar_dados("codigos_feitos", {
                                            "Nota" : str(df_planilha_online["Nr. nota"][dp]),
                                            "Representante da venda" : str(df_planilha_online["Representante da venda"][dp]).strip(),
                                            "Observacao" : str(df_busca["nomeOcorrencia"][index_busca]),
                                            "Status" : "ENTREGUE COM ATRASO"
                })
                            

            
                    elif data_atual > data_previsao:
                            print("Pedido atrasado")
                            logging.info("Pedido atrasado")
                           
                            df_planilha_online["Observação"][dp] = str(df_busca["nomeOcorrencia"][index_busca])
                            df_planilha_online["Status"][dp] = "ATRASADO"
                            alterar_dados("codigos_feitos", {
                    "Nota" : str(df_planilha_online["Nr. nota"][dp]),
                    "Representante da venda" : str(df_planilha_online["Representante da venda"][dp]).strip(),
                    "Observacao" : str(df_busca["nomeOcorrencia"][index_busca]),
                    "Status" : "PEDIDO ATRASADO"
                })
                else:
                    print(f"Cadastrando previsa de entrega {df_planilha_online["Nr. nota"][dp]}")
                    logging.info(f"Cadastrando previsa de entrega {df_planilha_online["Nr. nota"][dp]}")

                    df_planilha_online["Previsão de Chegada"][dp] = df_busca["previsaoEntrega"][index_busca]
                    df_planilha_online["Transportadora"][dp] = df_busca["Transportadora"][index_busca]
                    df_planilha_online["Status"][dp] =  "EM ANDAMENTO"
                    df_planilha_online["Observação"][dp] = df_busca['nomeOcorrencia'][index_busca]

                    alterar_dados("codigos_feitos", {
                    "Nota" : str(df_planilha_online["Nr. nota"][dp]),
                    "Representante da venda" : str(df_planilha_online["Representante da venda"][dp]).strip(),
                    "Observacao" : str(df_busca["nomeOcorrencia"][index_busca]),
                    "Status" : "EM ANDAMENTO"
                })
            else:
                print(f"Notal fiscal {df_planilha_online["Nr. nota"][dp]} sem transportadora")
                df_planilha_online["Transportadora"][dp] = "NÃO ENCONTRADO"
                alterar_dados("codigos_feitos", {
                    "Nota" : str(df_planilha_online["Nr. nota"][dp]),
                    "Representante da venda" : str(df_planilha_online["Representante da venda"][dp]).strip(),
                    "Status" : "Sem transportadora"
                })











    df_email = pd.DataFrame(pegar_dados("codigos_feitos"))
    df_email = df_email.loc[df_email["Status"] != "EM ANDAMENTO"]

    # df_emaii_trans_vazia = df_email.loc[df_email["Status"] == "Sem transportadora"]
    # enviar_email_transporadora("Inserir Transportadores",df_emaii_trans_vazia,"cleciolimalive@gmail.com")

    df_outros_status = df_email.loc[df_email["Status"] != "Sem transportadora"]
    vendores = df_outros_status["Representante da venda"].unique()

    for vendendor in vendores:
        daddos = df_outros_status.loc[df_outros_status["Representante da venda"] == vendendor]
        enviar_email(daddos,vendendor)


    


  
    
    
  

  


    


except:
    print("Erro ao tenta se conectar com google planilha")
    logging.info("Erro ao tenta se conectar com google planilha")
    print(format_exc())

finally:
    print("fi")
    df_planilha_online = df_planilha_online.astype(str)
    gsd.set_with_dataframe(sheet,df_planilha_online)
    df_planilha_online.to_excel(f"{os.getenv('RAIZ')}vamos2.xlsx", index=False)