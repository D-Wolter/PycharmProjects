from string import Template
from datetime import datetime


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import  MIMEImage
import smtplib

rementente_email = 'wolter.daniel@gmail.com'
remetente_senha = '343r3st4urs'
destinatario_email = 'danielwolter@hotmail.com'


with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Daniel Wolter', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Dwolter'
msg['to'] = destinatario_email
msg['subject'] = 'Atenção: este é um email de teste.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open ('Imag003.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(rementente_email, remetente_senha)
    smtp.send_mensage(msg)
    print('email enviado com sucesso')



