import time
import os

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

path = r'D:\Desktop'

fp = webdriver.FirefoxProfile(r'C:\Users\User\AppData\Roaming\Mozilla'
                              r'\Firefox\Profiles\l4yjb85n.relogio')  # Perfil de usuario do FireFox
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", path)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")

binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
options = Options()
options.headless = True  # Ativa navegador 'invisivel'
driver = webdriver.Firefox(firefox_profile=fp, options=options, firefox_binary=binary,
                           executable_path=r'C:\\geckodriver.exe')


class Page:

    def login(self, usuario, senha, url):
        # Se o arquivo existir ele deleta
        if os.path.exists(path + '\AFD00014003750030058.txt'):
            os.remove(path + '\AFD00014003750030058.txt')

        driver.get(url)
        teste = driver.find_element_by_tag_name('h3')
        if teste:
            username = driver.find_element_by_id('input_user')
            username.send_keys(usuario)
            password = driver.find_element_by_id('input_password')
            password.send_keys(senha)
            logar = driver.find_element_by_id('logar')
            logar.click()
            return True
        else:
            return False
            print('Não foi possivel fazer login')

    def baixar(self, url):

        driver.get(url + '#page=users&modal=afd_completo')  # redireciona o link da pagina
        driver.switch_to.active_element #alterna para o elemento ativo na tela - modal
        time.sleep(2)
        driver.find_element_by_xpath("//button[contains(.,'Continuar')]").click()

    def fechar_navegador(self):

        while not os.path.exists(path + r'\AFD00014003750030058.txt'):
            time.sleep(1)
            print('Aguardando download...')

        if os.path.isfile(path + r'\AFD00014003750030058.txt'):
            driver.quit()
            print('Download concluído')
        else:
            raise ValueError('Arquivo nao encontrado em ' + path)