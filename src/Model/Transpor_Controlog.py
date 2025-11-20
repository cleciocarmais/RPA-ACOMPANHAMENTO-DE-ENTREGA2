import os
import pandas as pd
import pyautogui as p
from dotenv import load_dotenv
from traceback import format_exc
from selenium import webdriver
from datetime import date, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def transportadora_controlog():
    try:
        meses = {
        '1': "JAN",
        '2': "FEV",
        '3': "MAR",
        '4': "ABR",
        '5': "MAI",
        '6': "JUN",
        '7': "JUL",
        '8': "AGO",
        '9': "SET",
        '10': "OUT",
        '11': "NOV",
        '12': "DEZ"
    }
        load_dotenv()
        #Abrindo arquivo de credencias:
        with open(os.getenv("CredenciaisControlog")) as file:
            chaves = file.readlines()
            usuario = chaves[0].strip()
            senha = chaves[1].strip()

        
        chrome_options = Options()
        prefs = {
            "download.default_directory": f"{os.getenv('RAIZ')}controlog",  # Pasta de destino
            "download.prompt_for_download": False,        # Não perguntar onde salvar
            "download.directory_upgrade": True,           # Permitir sobrescrever
            "safebrowsing.enabled": True,                 # Evitar bloqueios
        }
        chrome_options.add_experimental_option("prefs", prefs)
        navegador = webdriver.Chrome(options=chrome_options)
        navegador.get("https://www.appcontrolog.com.br/login/")
        navegador.maximize_window()
        p.sleep(2)
        #TELA DE LOGN DO SITE

        #tempo de espera
        WebDriverWait(navegador, 15).until(ec.visibility_of_element_located((By.ID, "email")))
        #Campo input usuario
        navegador.find_element(By.ID, "email").send_keys(usuario)
        p.sleep(1)
        #Campo input senha
        navegador.find_element(By.ID, "senha").send_keys(senha)
        p.sleep(1)
        navegador.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div[1]/button").click()
        p.sleep(2)
        #ESPERANDO CARREGA ICONE DE RELATORIO
        WebDriverWait(navegador, 20).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div[11]/nav/div/div[2]/ul[1]/li[6]/a")))
        p.sleep(1)
        #CLICANDO EM RELATORIOS
        navegador.find_element(By.XPATH, "/html/body/div/div[11]/nav/div/div[2]/ul[1]/li[6]/a").click()
        p.sleep(3)
        #CLIQUE EM RELATOPRIO GERAL DE ENTREGAS
        navegador.find_element(By.XPATH, "/html/body/div/div[11]/nav/div/div[2]/ul[1]/li[6]/ul/li[1]/a").click()
        p.sleep(4)
        #SELECT DATA INICIAL
        Elemento1 = navegador.find_element(By.XPATH,"/html/body/div/div[12]/div/div/div[3]/div/nav/div[2]/div/div[11]/div[5]/ul/li[1]/select")
        select_mes_inicial = Select(Elemento1)

        Elemento2 = navegador.find_element(By.XPATH,"/html/body/div/div[12]/div/div/div[3]/div/nav/div[2]/div/div[11]/div[5]/ul/li[2]/select")
        select_dia_inicial = Select(Elemento2)
        Elemento3 = navegador.find_element(By.XPATH,"/html/body/div/div[12]/div/div/div[3]/div/nav/div[2]/div/div[11]/div[5]/ul/li[4]/select")
        select_mes_final = Select(Elemento3)
        Elemento4 = navegador.find_element(By.XPATH,"/html/body/div/div[12]/div/div/div[3]/div/nav/div[2]/div/div[11]/div[5]/ul/li[5]/select")
        select_dia_final = Select(Elemento4)
        data_inicial =date.today() - timedelta(20)
        data_final = date.today()

        if data_inicial.weekday() in [5]:
            data_inicial = data_inicial - timedelta(1)

        if data_inicial.weekday() in [6]:
            data_inicial = data_inicial - timedelta(2)

        if data_final.weekday() in [5]: #=> se for em sabado
            data_final = data_final - timedelta(1)
        if data_final.weekday() in [5,6]:#=> se for em domingo 
            data_final = data_final - timedelta(2)


        mes_inicial = data_inicial.strftime("%m")
        dia_inicial =  data_inicial.strftime("%d")
        if int(dia_inicial) < 10:
            dia_inicial = dia_inicial.replace("0", "")


        if int(mes_inicial) < 10:
            mes_inicial = mes_inicial.replace("0", "")
    

        mes_final = data_final.strftime("%m")
        dia_final =  data_final.strftime("%d")

        if int(mes_final) < 10:
            mes_final = mes_final.replace("0", "")
        if int(dia_final) < 10:
            dia_final = dia_final.replace("0", "")

        select_mes_inicial.select_by_value(mes_inicial)
        select_dia_inicial.select_by_value(dia_inicial)
        p.sleep(5)
      
        select_mes_final.select_by_value(mes_final)
        select_dia_final.select_by_value(dia_final)
    
        navegador.find_element(By.XPATH, "/html/body/div/div[12]/div/div/div[3]/div/nav/div[2]/div/div[13]/button").click()
        p.sleep(1)
        #ESPERA A TABEL CARREGAR
        

        WebDriverWait(navegador, 30).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div[12]/div/div/div[8]/div/div/div/div/table/tbody")))
        # CLICAR EM EXPORTAR DADODS
        navegador.find_element(By.XPATH, "/html/body/div/div[12]/div/div/div[4]/div[1]/ul/li[4]/div/i").click()
        try:
            # MENSAGEM BOX
            WebDriverWait(navegador, 10).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div[9]")))
            navegador.find_element(By.XPATH, "/html/body/div/div[9]/div/div/div/div/div[2]/div[3]/div/ul/li[1]/button").click()
            p.sleep(2)
        except:
            pass
        #ESPERANDO BUTTON DA EXPORTA APARECER
        WebDriverWait(navegador, 15).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div[6]/div[1]/div/div/div[2]/div[2]/a")))
        navegador.find_element(By.XPATH, "/html/body/div/div[6]/div[1]/div/div/div[2]/div[2]/a").click()
        while True:
            arquivos = os.listdir(f"{os.getenv('RAIZ')}controlog")
            print(arquivos)

            # Verifica se existe algum arquivo .xlsx na pasta
            planilhas = [f for f in arquivos if f.endswith(".csv")]
            
            if planilhas:
                planilha = planilhas[0]  # pega a primeira encontrada
                caminho_planilha = os.path.join(f"{os.getenv('RAIZ')}controlog", planilha)
                print("Arquivo encontrado:", caminho_planilha)
                break
            else:
                p.sleep(3)
        df = pd.read_csv(caminho_planilha, delimiter=";", encoding="latin1")
        df.to_excel(f"{os.getenv('RAIZ')}controlog\\planilha_controlog.xlsx", index=False)
        os.remove(caminho_planilha)
        navegador.quit()
        p.sleep(2)
    except:
        print(format_exc())
        pass
if __name__ == "__main__":
    transportadora_controlog()
