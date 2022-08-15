import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('/' * 60)
    print('    O site Pudim NAO ESTA ACESSIVEL no momento.')
    print('/' * 60)
else:
    print('='*30)
    print('Consegui acessar o site Pudim com sucesso!')
    print('=' * 30)