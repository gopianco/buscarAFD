from model import Page
from os import getcwd



def set_firefox(self):

    perfil = r'C:\Users\User\AppData\Roaming\Mozilla' r'\Firefox\Profiles\l4yjb85n.relogio'
    exe = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    driver = r'C:\\geckodriver.exe'
    local_donwload = getcwd()

    secao = self.config(self, perfil, exe, driver, local_donwload)

    return secao


def log_idclass(self, sec):

    usuario = 'admin'
    senha = 'admin'
    url = 'https://192.168.0.179'

    if self.log(self, usuario, senha, url, sec):
        return True
    else:
        return False


def verifica_arquivo(self):


    local_donwload = getcwd()
    nome_arquivo = r'\AFD00014003750030058.txt'

    if self.verifica_arquivo(self, local_donwload, nome_arquivo):
        return True


def baixar(self, sec):

    url = 'https://192.168.0.179'

    if self.baixar(self,url, sec):
        return True

def close(self, sec):

    local_donwload = getcwd()
    nome_arquivo = r'\AFD00014003750030058.txt'

    if self.fechar_navegador(self, local_donwload, sec, nome_arquivo):
        return True


def main():
    secao = Page
    sec = set_firefox(secao)

    if log_idclass(secao, sec):
        print('Login realizado...')
    else:
        print('Não foi possivel realizar o login!')

    if verifica_arquivo(secao):
        print('Arquivo encontrado e removido')
    else:
        print('Arquivo não encontrado, pronto para download!')

    if baixar(secao, sec):
        print('Fazendo download, aguarde...')
    else:
        print('Problema no download')

    if close(secao, sec):
        print('Donwload concluido, fechando navegador...')
        print('ok')
    else:
        print('Problema de download')






if __name__ == '__main__':
    main()



