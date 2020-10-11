#!python

import cgi, requests
from bs4 import BeautifulSoup

form = cgi.FieldStorage()
url_source = form["url"].value

# get할 때 url_source에 따옴표 붙이면 안됨
# .text로 안불러오면 response has no len 오류 발생
url_html = requests.get(url_source).text 
soup = BeautifulSoup(url_html, "html.parser")

# class에 언더스코어 붙여야 함
contributions = soup.find('h2', class_="f4 text-normal mb-2").text

file = open("C:/Users/dfjun/OneDrive/바탕 화면/Git_info.txt", 'w')
file.write(' '.join(contributions.split()))
file.write("\n")
for repo in soup.find_all('span', class_="repo"):
  file.write(repo.get_text())
  file.write("\n")
file.close()

print("Location: index.py")
print()