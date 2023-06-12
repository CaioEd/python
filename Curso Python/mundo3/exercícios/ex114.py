import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('Acesso ao site indisponível')
else:
    print('Tudo OK')