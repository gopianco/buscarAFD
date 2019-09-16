from model import Secao
from os import getcwd

def log_idclass():
    idclass = Secao
    idclass.url = 'https://192.168.0.179'
    idclass.usuario = 'admin'
    idclass.senha = 'admin'
    idclass.nome_arquivo = r'\AFD00014003750030058.txt'
    idclass.path = getcwd()

    drive = idclass.config_driver(idclass)
    idclass.log(idclass, drive)

    idclass.verifica_arquivo(idclass)

    idclass.baixar(idclass, drive)

    if idclass.fechar_navegador(idclass, drive) == False:
        drive.quit()
        log_idclass()
    
def main():
    log_idclass()

if __name__ == '__main__':
    main()