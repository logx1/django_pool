from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

print("=========================")
lol = soup.find(string="baad")
print(lol)