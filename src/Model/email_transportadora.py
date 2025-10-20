import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
import logging
import os
from dotenv import load_dotenv



def email_transportadora():
    load_dotenv()
    print("Enviando Email de aviso transportadora")
    logging.info("Enviando Email de aviso transportadora")
    credenciais = open(os.getenv("Crendeciais_email"), 'r')
    chaves = credenciais.readlines()
    credenciais.close()

    email_probot = chaves[0][:-1]
    credencial = chaves[1]

    email_vendedor = '"cleciolimalive@gmail.com"' #TESTE 

    message = MIMEMultipart('related')
    message['From'] = email_probot
    message['To'] = email_vendedor
    message['Subject'] = 'RPA - ACOMPANHAMENTO DE ENTREGAS'
    msgAlternative = MIMEMultipart('alternative')
    message.attach(msgAlternative) 

    msgText = MIMEText('RPA - ACOMPANHAMENTO DE ENTREGAS')
    msgAlternative.attach(msgText) 
    html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Aviso Importante</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f4f4f4; margin:0; padding:0;">
  <table width="100%" cellpadding="0" cellspacing="0">
    <tr>
      <td align="center" style="padding: 20px 0;">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:8px; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
          <tr>
            <td style="background-color:#2563eb; padding:20px; text-align:center; color:#ffffff; font-size:22px; font-weight:bold;">
              Aviso Importante
            </td>
          </tr>
          <tr>
            <td style="padding: 30px; color:#333333; font-size:16px; line-height:1.5;">
              <p>Olá,</p>
              <p>Este é um aviso importante. Existem pedidos sem nome da transportadora:</p>
              <p style="text-align:center; margin:30px 0;">
                <a href="https://docs.google.com/spreadsheets/d/1slM2RSvBDFXY8yRxlpStTQQNhY0b8I9m-EmGQ22xzhM/edit?gid=1541386208#gid=1541386208" 
                   style="background-color:#2563eb; color:#ffffff; padding:12px 24px; text-decoration:none; border-radius:6px; font-weight:bold; display:inline-block;">
                  Responder Agora
                </a>
              </p>
              <p>Se você tiver alguma dúvida, entre em contato com nossa equipe.</p>
              <p>Atenciosamente,<br>Equipe de Suporte</p>
            </td>
          </tr>
          <tr>
            <td style="background-color:#f1f1f1; padding:15px; text-align:center; font-size:12px; color:#777;">
              © 2025 Sua Empresa. Todos os direitos reservados.
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""

    msgText = MIMEText(html, "html")

    msgAlternative.attach(msgText)

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(email_probot, credencial)

    text = message.as_string()
    session.sendmail(email_probot, email_vendedor.split(","), text)
    session.quit()

    print('Email Enviado!')
if __name__ == "__main__":
    email_transportadora()
