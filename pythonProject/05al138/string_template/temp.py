from string import Template
from datetime import datetime
      #     nome arquivo  leitura  variavel
with open('template.html', 'r') as html:
    template = Template(html.read())
    #variavel            agora   formatacao da data
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Daniel Wolter', data=data_atual)

print(corpo_msg)
