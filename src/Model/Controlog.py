from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
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
    p.alert("ola")

if __name__ == "__main__":
    transportadora_controlog()
