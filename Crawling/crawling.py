import urllib.request
from bs4 import BeautifulSoup

url ="http://www.naver.com"
sourcecode = urllib.request.urlopen(url).read()
soup = BeautifulSoup(sourcecode ,"html.parser")

for text in soup.find_all("span" , class_="ah_k" ) :
    print(text.get_text())



