from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import config

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
nav = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/wesllen/Documentos/webdriver/chromedriver')
#Coloca o navegador novamente em estado de execucao normal.
#nav = webdriver.Chrome(executable_path='/home/wesllen/Documentos/webdriver/chromedriver')
nav.get(config.login)
try:
    print ("""
    =============================================================
             SCRIPT DE REINICIO DO HOTSPORT300
    =============================================================
           """)
    ec = nav.find_element_by_id("user")
    ec.click()
    ec.send_keys(config.usr)
    ps = nav.find_element_by_id('password')
    ps.send_keys(config.passwd)
    ps.send_keys(Keys.RETURN)
    sleep(1)
    nav.get(config.hotspot)
    rs = nav.find_elements_by_tag_name('a_sub_menu')
    rs[1].click()
    btn_restart = nav.find_element_by_class_name('buttonBig')
    btn_restart.click()
except Exception as erro:
    print('Houve um erro ao carregar a página: \n\n{erro.__class__}')
else:
    print('Reiniciando o roteador, aguarde 80 segundos e tente acessar novamente.')
