import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site pudim com sucesso!')