# tipo =  "ola"
# import os
# print(tipo.upper())

import pyautogui as p
# package_dir = os.path.dirname("C:\RPA\RPA_ACOMPANHAMENTO_ENTREGAS")

# print(package_dir)

# import pyautogui as p

# explorer = p.locateCenterOnScreen(f"{img}nome_Arquivos_explorer.png", confidence=0.95)

# print("ola")
# numero = "1000008395"

# print(numero[-4:])

import pandas as pd


# planilha_rota_entregas = pd.read_excel("planilha_rota_entregas.xlsx")
# planilha_online = pd.read_excel("vamos.xlsx")

# df_controlog = pd.read_csv(r"D:\RPA\RPA_ACOMPANHAMENTO_ENTREGAS_2\controlog\Controlog_Relatorio_Cargas_e_Entregas_18_10_2025_168f38b7202105.csv",delimiter=";",encoding="latin1")
# df_controlog["Transportadora"] = "Controlog"
# print(df_controlog.columns)
# df_controlog.columns = (
#     df_controlog.columns
#     .str.replace(r'\s+', ' ', regex=True)  # substitui múltiplos espaços por um
#     .str.strip()                           # remove espaços do início/fim
# )
# df_controlog = df_controlog[["Nota Fiscal","Data Carga","Data Entrega","Obs"]]
# df_controlog["Data Carga"] = [str(x.replace(" ","")[:-8]) for x in df_controlog["Data Carga"]]

# print(df_controlog["Data Carga"])

# # df_controlog.rename(columns={
# # "NOTA FISCAL" : "notaFiscal",
# # "Data Carga" :"previsaoEntrega",
# # "Data Entrega": "dataEntrega",
# # "Obs" : "nomeOcorrencia"
# # }) 

# # df_controlog.to_excel("calcinha_preta.xlsx")



# df = pd.read_excel(r"D:\RPA\RPA_ACOMPANHAMENTO_ENTREGAS_2\planilha_rota_entregas.xlsx", dtype=str)

# filtro = df.loc[df["notaFiscal"] == "151671"]

# print(filtro.index[0])

# import os
# planilha = ''
# while True:
#     arquivos = os.listdir(r"D:\RPA\RPA_ACOMPANHAMENTO_ENTREGAS_2\braspress")
#     print(arquivos)
#     if ".xlsx" in arquivos:
#         planilha = arquivos
#         break

# print(planilha)


ar = ["aruiv.xlsx"]

if ".xlsx" in ar:
    print('ola')