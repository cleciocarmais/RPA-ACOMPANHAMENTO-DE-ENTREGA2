from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from dotenv import load_dotenv
import pyautogui as p
import os

def transportadora_controlog():
    load_dotenv()
    #Abrindo arquivo de credencias:
    with open(os.getenv("CredenciaisControlog")) as file:
        chaves = file.readlines()
        usuario = chaves[0].strip()
        senha = chaves[1].strip()

    navegador =  webdriver.Chrome()
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
    p.sleep(2)
    #SELECT DATA INICIAL
    Elemento1 = navegador.find_element(By.XPATH,"/html/body/div/div[12]/div/div/div[3]/div/nav/div[2]/div/div[11]/div[5]/ul/li[1]/select")
    select_mes_inicial = Select(Elemento1)

    Elemento2 = navegador.find_element(By.XPATH,"/html/body/div/div[12]/div/div/div[3]/div/nav/div[2]/div/div[11]/div[5]/ul/li[2]/select")
    select_dia_inicial = Select(Elemento2)
    
    
    Elemento3 = navegador.find_element(By.XPATH,"/html/body/div/div[12]/div/div/div[3]/div/nav/div[2]/div/div[11]/div[5]/ul/li[4]/select")
    select_mes_final = Select(Elemento3)
    Elemento4 = navegador.find_element(By.XPATH,"/html/body/div/div[12]/div/div/div[3]/div/nav/div[2]/div/div[11]/div[5]/ul/li[5]/select")
    select_dia_final = Select(Elemento4)


    select_mes_inicial.select_by_value("5")
    select_dia_inicial.select_by_value("2")
    p.sleep(2)
    select_mes_final.select_by_value("4")
    select_dia_final.select_by_value("2")
    p.sleep("vamso ver")
    p.sleep(2)

if __name__ == "__main__":
    transportadora_controlog()
