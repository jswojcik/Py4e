from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url= 'https://www.youtube.com/watch?v=NVUQia7Toos'
html=urlopen(url, context=ctx).read()
soup=BeautifulSoup(html,'html.parser')

print(soup.get_text())

