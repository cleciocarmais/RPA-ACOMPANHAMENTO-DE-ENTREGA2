from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
import pyautogui as p
import os
import logging

def transportadora_bridex(codigo):
    load_dotenv()
    #Abrindo arquivo de credencias:
    with open(os.getenv("CredenciaisCBirdex")) as file:
        chaves = file.readlines()
        usuario = chaves[0].strip()
        senha = chaves[1].strip()

    navegador =  webdriver.Chrome()
    navegador.get("https://cliente.cbirdex.com.br/login")
    navegador.maximize_window()
    p.sleep(2)
    #TELA DE LOGN DO SITE

    #tempo de espera
    WebDriverWait(navegador, 15).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/section/div/form/div/div/input")))
    #Campo input usuario
    navegador.find_element(By.XPATH, "/html/body/div[1]/main/div/div/section/div/form/div/div/input").send_keys(usuario, Keys.ENTER)
    p.sleep(5)
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
    #CAMPO PESQUISA
    navegador.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div/section[1]/div[1]/div[1]/div/input").send_keys(codigo, Keys.ENTER)
    p.sleep(4)
    #Verficar se ouve algum retorno da pesquisa

    listas = navegador.find_elements(By.XPATH, "/html/body/div[1]/main/div/div/div/div/section[2]/div/div[2]/a")
    if len(listas) > 0:
        for x in listas:
            print(x.text)
        
    else:
        print("Objeto nao coletado")
        logging.info("Objeto nao coletado")
        return "Nao Coletado"
    p.alert("ola")
if __name__ == "__main__":
    transportadora_bridex("00148724")
