import time
import os

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options


class Page:
    """Esta classe cria uma seção no Firefox para fazer a busca e download do arquivo AFD do relogio de ponoto ID CLASS
    Utilizando a bilioteca Selenium para simular o acesso real ao navegador e à página de download.
    """

    __author__ = 'Giovane Pianco'
    __version__ = "2.0"
    __email__ = 'gopianco@hotmail.com'
    __maintainer__ = 'Giovane Pianco'

    def config(self, profile, binary, driver, path):

        """
        Configura o driver e opçoes do navegador.

        :param profile: path do perfil criado para o firefox
        :param binary: path da instalação do firefor
        :param driver: configurações do geckodriver
        :param path: path padrao para o download
        :return localdriver: driver ja configurado

        """
        fp = webdriver.FirefoxProfile(profile)  # Perfil de usuario do FireFox
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.download.dir", path)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")

        binary = FirefoxBinary(binary)
        options = Options()
        options.headless = False  # Ativa navegador 'invisivel'
        local_driver = webdriver.Firefox(firefox_profile=fp, options=options, firefox_binary=binary,
                                        executable_path=driver)

        return local_driver

    def log(self, usuario, senha, url, driver):
        """
        Faz login na pagina inicial do relogio de ponto.

        :param usuario: usuario valido que tenha acesso a interface web do ponto.
        :param senha: senha do usuario.
        :param url: geralmente IP do relogio de ponto.
        :param path: path local.
        :return: True se conseguir logar.

        """

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

    def verifica_arquivo(self, path, nome_arquivo):
        """
        Verifica se o arquivo ja existe, se sim ele remove.
        :param path: pasta local
        :param nome_arquivo: nome padrão do arquivo AFD
        :return True se remover o arquivo

        """
        if os.path.exists(path + nome_arquivo):
            os.remove(path + nome_arquivo)
            return True

    def baixar(self, url, driver):
        """
        Faz o redirecionamento para a url da modal do download completo do AFD

        :param url: geralmente IP do relogio de ponto.
        :param driver: configurações do geckodriver

        """

        driver.get(url + '#page=users&modal=afd_completo')  # redireciona o link da pagina
        driver.switch_to.active_element  # alterna para o elemento ativo na tela - modal
        time.sleep(2)  # aguarda a modal aparecer na tela
        driver.find_element_by_xpath("//button[contains(.,'Continuar')]").click()
        return True

    def fechar_navegador(self, path, driver, nome_arquivo):
        """

        :param path: pasta local
        :param driver: configurações do geckodriver
        :return: True se o donwload for concluido e fechou o navegador
        """

        while not os.path.exists(path + nome_arquivo):
            time.sleep(1)


        if os.path.isfile(path + nome_arquivo):
            driver.quit()
            return True

        else:
            raise ValueError('Arquivo nao encontrado em ' + path)
