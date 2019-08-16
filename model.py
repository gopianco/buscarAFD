import time
import os

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options


class Secao:
    """
    Esta classe cria uma seção no Firefox para fazer a busca e download do arquivo AFD do relogio de ponoto ID CLASS
    Utilizando a bilioteca Selenium para simular o acesso real ao navegador e à página de download.
    """

    __author__ = 'Giovane Pianco'
    __version__ = "3.0"
    __email__ = 'gopianco@hotmail.com'
    __maintainer__ = 'Giovane Pianco'

    def __init__(self, path, url, usuario, senha, nome_arquivo):

        """
        Construtor padrão
        """
        self.path = path

        self.url = url
        self.usuario = usuario
        self.senha = senha
        self.nome_arquivo = nome_arquivo
        self.path = path

    def config_driver(self):
        """
        Configurações padão do fireFox
        :return: objeto webDriver
        """

        fp = webdriver.FirefoxProfile(r'C:\Users\User\AppData\Roaming\Mozilla'
                                      r'\Firefox\Profiles\l4yjb85n.relogio')  # Perfil de usuario do FireFox
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.download.dir", self.path)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")

        binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
        options = Options()
        options.headless = False  # Ativa navegador 'invisivel'
        config = webdriver.Firefox(firefox_profile=fp, options=options, firefox_binary=binary,
                                        executable_path=r'C:\\geckodriver.exe')

        return config

    def log(self, drive):
        """
        Faz login na pagina inicial do relogio de ponto.

        """

        drive.get(self.url)
        teste = drive.find_element_by_tag_name('h3')
        if teste:
            username = drive.find_element_by_id('input_user')
            username.send_keys(self.usuario)
            password = drive.find_element_by_id('input_password')
            password.send_keys(self.senha)
            logar = drive.find_element_by_id('logar')
            logar.click()
            return True
        else:
            return False

    def verifica_arquivo(self):
        """
        Verifica se o arquivo ja existe, se sim ele remove.
        """
        if os.path.exists(self.path + self.nome_arquivo):
            os.remove(self.path + self.nome_arquivo)
            return True

    def baixar(self, driver):
        """
        Faz o redirecionamento para a url da modal do download completo do AFD

        """

        driver.get(self.url + '#page=users&modal=afd_completo')  # redireciona o link da pagina
        driver.switch_to.active_element  # alterna para o elemento ativo na tela - modal
        time.sleep(2)  # aguarda a modal aparecer na tela
        driver.find_element_by_xpath("//button[contains(.,'Continuar')]").click()
        return True

    def fechar_navegador(self, drive):
        """
        Fecha o navegador quando encontra o arquivo na pasta.
        """

        count = 0
        while not os.path.exists(self.path + self.nome_arquivo):
            time.sleep(1)
            count += 1
            if count == 120:
                drive.quit()
                return False


        if os.path.isfile(self.path + self.nome_arquivo):
            drive.quit()
            return True

        else:
            raise ValueError('Arquivo nao encontrado em ' + self.path)
