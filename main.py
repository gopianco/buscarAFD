from page import Page


ip = 'https://192.168.0.179'
user = 'admin'
senha = 'admin'

page = Page
if Page.login(page, user, senha, ip):
    print('Login realizado')
    page.baixar(page, ip)
else:
    print('Erro de login')

page.fechar_navegador(page)


