import requests
from bs4 import BeautifulSoup

r = requests.get('https://testrecaptcha.github.io/')

print(r)
#
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

# a = soup.find_all('a')
# script = soup.find('script')
#
# s = script.find(src='*captcha*')

# s = soup.find('div', class_="g_recaptcha")
#
# print(s)
