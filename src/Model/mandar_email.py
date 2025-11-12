from dotenv import load_dotenv
from src.Model.utilizado import emails
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.Model.estilo import estilo
import os
import smtplib as sm
import pandas as pd
import logging

def enviar_email(dados,vendedor):


    load_dotenv()
    with open(os.getenv("Crendeciais_email"), "r") as file:
        chaves = file.readlines()
        usuario = chaves[0].strip()
        senha = chaves[1].strip()
    try:
        email = sm.SMTP("smtp.gmail.com", 587)
        email.starttls()
        email.login(usuario,senha)
    except:
        print("Erro ao tentar conectar com planiha")
        exit()
    receiver = (f'{emails[vendedor]}, janderamancio@gmail.com')
    message = MIMEMultipart("alternative")
    message["From"] = usuario
    message["To"] = receiver
    message["Subject"] = f"RPA ACOMPANHAMENTO ENTREGA"
    tabela = dados.to_html(index=False)
    mgsAlternative = MIMEMultipart("alternative")
    message.attach(mgsAlternative)

    mgsText = MIMEText(estilo(tabela), "html")
    mgsAlternative.attach(mgsText)

    text = message.as_string()
    email.sendmail(usuario,receiver.split(","),text)
    print(f"EMAIL ENVIADO EMAIL PARA {vendedor}")

def enviar_email_transporadora(titulo, dados,sender):

    load_dotenv()
    with open(os.getenv("Crendeciais_email"), "r") as file:
        chaves = file.readlines()
        usuario = chaves[0].strip()
        senha = chaves[1].strip()
    try:
        email = sm.SMTP("smtp.gmail.com", 587)
        email.starttls()
        email.login(usuario,senha)
    except:
        print("Erro ao tentar conectar com planiha")
        exit()
    receiver = (f"{sender},janderamancio@gmail.com")
    message = MIMEMultipart("alternative")
    message["From"] = usuario
    message["To"] = receiver
    message["Subject"] = f"RPA ACOMPANHAMENTO ENTREGA {titulo}"

    mgsAlternative = MIMEMultipart("alternative")
    message.attach(mgsAlternative)
    corpo = ""
    dados = dados.fillna("vazio")
    nomes_dos_representantes = dados["Representante da venda"].unique()
    
    for nome in nomes_dos_representantes:
        dados_representando = dados.loc[dados["Representante da venda"] == nome]
        tabela = dados_representando.to_html(index=False)
        corpo = corpo + f"<h1>{nome}</h1><br>{tabela}"


    mgsText = MIMEText(estilo(corpo), "html")
    mgsAlternative.attach(mgsText)

    text = message.as_string()
    email.sendmail(usuario,receiver.split(','),text)
    print("EMAIL DE PEDIDOS SEM TRANSPORTADORA ENVIADO!!!")
    logging.info("email de transportadora enviando com sucesso!!!")







if __name__ == "__main__":
    enviar_email()