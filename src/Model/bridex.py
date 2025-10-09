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
    status = {
        "A caminho" : "em andamento"
    }
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
    #CLIQUE EM DOWLOAD
    navegador.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div/div/button/a").click()
    
   
    p.sleep(4)
    

if __name__ == "__main__":
    transportadora_bridex("8584")
