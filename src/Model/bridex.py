from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import pyautogui as p
import os
import logging
import pandas as pd

def transportadora_bridex():
    load_dotenv()
    arquivos = ["brindx","brindx_filial"]
    chrome_options = Options()
    prefs = {
        "download.default_directory": f"{os.getenv('RAIZ')}brindx",  # Pasta de destino
        "download.prompt_for_download": False,        # Não perguntar onde salvar
        "download.directory_upgrade": True,           # Permitir sobrescrever
        "safebrowsing.enabled": True,                 # Evitar bloqueios
    }
    chrome_options.add_experimental_option("prefs", prefs)
    navegador = webdriver.Chrome(options=chrome_options)
    #Abrindo arquivo de credencias:

    navegador.get("https://cliente.cbirdex.com.br/login")
    navegador.maximize_window()
    p.sleep(2)
    #TELA DE LOGN DO SITE
    for x in arquivos:
        with open(os.getenv(f"CredenciaisC{x}")) as file:
            chaves = file.readlines()
            usuario = chaves[0].strip()
            senha = chaves[1].strip()
        #tempo de espera
        WebDriverWait(navegador, 15).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/section/div/form/div/div/input")))
        #Campo input usuario
        navegador.find_element(By.XPATH, "/html/body/div[1]/main/div/div/section/div/form/div/div/input").send_keys(usuario, Keys.ENTER)
        p.alert("vamos ver isso ")
        WebDriverWait(navegador, 20).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/section/div/form/div[2]/div/input")))
        #Campo input senha
        navegador.find_element(By.XPATH, "/html/body/div[1]/main/div/div/section/div/form/div[2]/div/input").send_keys(senha, Keys.ENTER)
        #Buttom de rastreamento
        WebDriverWait(navegador, 15).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/button")))
        p.sleep(3)
        navegador.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/button").click()
        p.sleep(5)
        #BTN REMETENTE
        navegador.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/ul/li[1]/a").click()
        p.sleep(5)
    
        #CLIQUE EM DOWLOAD
        navegador.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div/div/button/a").click()

        while True:
            arquivos = os.listdir(f"{os.getenv('RAIZ')}brindx")
            print(arquivos)

            # Verifica se existe algum arquivo .xlsx na pasta
            planilhas = [f for f in arquivos if f.endswith(".csv")]
            
            if planilhas:
                planilha = planilhas[0]  # pega a primeira encontrada
                caminho_planilha = os.path.join(f"{os.getenv('RAIZ')}brindx", planilha)
                print("Arquivo encontrado:", caminho_planilha)
                break
            else:
                p.sleep(3)
        df = pd.read_csv(caminho_planilha, delimiter=";")
        df.to_excel(f"{os.getenv('RAIZ')}{x}\\planilha_{x}.xlsx", index=False)
        #CLICANDO EM SAIR DO SISTEMA
        navegador.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div").click()
        p.sleep(3)
        #CLICA EM SAIR 
        navegador.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div[2]/button[2]").click()
    
    p.sleep(4)
    

if __name__ == "__main__":
    transportadora_bridex()
