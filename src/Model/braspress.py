from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
import pyautogui as p
import os
import logging
from datetime import date, timedelta




def brasspress(nota):
    load_dotenv()
    with open(os.getenv("CredenciaisBrasspress")) as file:
        chaves = file.readlines()
        usuario = chaves[0].strip()
        senha = chaves[1].strip()
    print("Acessando Site de Braspress")
    logging.info("Acessando Site de Braspress")
    navegador = webdriver.Chrome()
    navegador.get("https://www.braspress.com/area-do-cliente/minha-conta/")
  
    p.sleep(2)
    navegador.maximize_window()
    p.sleep(1)
    #ESPERANDO TELA DE COOCKIES APARECE:
    # p.alert("teste")
    try:
        WebDriverWait(navegador, 20).until(ec.visibility_of_element_located((By.XPATH, "/html/body/footer/div[6]/div[3]/div")))
        p.sleep(1)
        navegador.find_element(By.XPATH, "/html/body/footer/div[6]/div[3]/div/div[3]/button").click()
        p.sleep(2)
    except:
        pass

    try:
        navegador.find_element(By.XPATH, "/html/body/footer/div[2]/div[1]").click()
    except:
        pass

    p.alert("conde")
    p.sleep(2)
    navegador.switch_to.frame(navegador.find_element(By.XPATH, "/html/body/main/div/div/div/iframe"))
    WebDriverWait(navegador, 20).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/form/div[2]/div/div[1]/div/input")))
    p.sleep(2)
    #CAMPO USUARIO
    navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/form/div[2]/div/div[1]/div/input").send_keys(usuario)
    p.sleep(2)
    #CAMPO SENHA
    navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/form/div[2]/div/div[2]/div/input").send_keys(senha)
    p.sleep(2)
    #BTN ENTRAR
    navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/form/div[2]/div/div[3]/input").click()
    p.sleep(2)
    #PAGINA PRINCIPAL
    WebDriverWait(navegador, 15).until(ec.visibility_of_element_located((By.XPATH, "/html/body/main/div/div[2]/div/div[2]/div[4]/button")))
    #BTN DE ENCOMENDADS
    navegador.find_element(By.XPATH, "/html/body/main/div/div[2]/div/div[2]/div[4]/button").click()
    p.sleep(5)

    
    #CAMPO DATA INICIAL
    # navegador.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div/div/div/div[1]/div[1]/div/input").send_keys("01/09/2025", Keys.ENTER)
    # p.sleep(2)
    # #CAMPO DATA FINAL
    # navegador.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div/div/div/div[1]/div[2]/div/input").send_keys("19/09/2025",Keys.ENTER)
    navegador.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div/div/div/div[4]/div[2]/input").send_keys(nota)
    p.sleep(2)
    #CAMPO DE RADIO 
    navegador.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div/div/div/div[7]/div/label[1]").click()
    p.alert(2)
    p.sleep(2)
    #CAMPO PESQUISA
    navegador.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div/div/div/div[10]/button").click()
    p.sleep(2)
    #Esperando carregar tabela
    WebDriverWait(navegador, 20).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[3]/div[1]/table")))
    items_tabela = navegador.find_elements(By.XPATH, "/html/body/div[1]/div[4]/div[3]/div[1]/table/tbody/tr")
    if len(items_tabela) > 0:
        previsao_entrega = navegador.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[3]/div[1]/table/tbody/tr[1]/td[9]").text
        Ultima_ocorrencia = navegador.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[3]/div[1]/table/tbody/tr[1]/td[11]").text

        return {previsao_entrega, Ultima_ocorrencia}

    else:
        print("nenhum dados encontrado")

if __name__ == "__main__":
    print(brasspress(150038))