# restart_hotspot300_intelbras

Script que Loga e reinicia o hotspot300 remotamente, 
usado para automatizar rotina de logar nos roteadores para reinciar em caso de travamento do serviço de hotspot.

## Como Usar:

1. Instale o Selenium:

```
pip3 install selenium
```

2. Faça o Download do google chromedrive:


## https://chromedriver.chromium.org/downloads


3. Deve ser criado um arquivo chamado config.py com as seguintes variaveis abaixo:

```
usr = 'usuario'
passwd = 'senha'
login = 'http://IP-DO-HOTSPOT/cgi-bin/firmware.cgi?formNumber=200'
hotspot = 'http://IP-DO-HOTSPOT/cgi-bin/firmware.cgi?formNumber=10'
loc = 'caminho-do-seu-chromedriver'
```
