import requests
from bs4 import BeautifulSoup


url_source = "https://github.com/dfjung4254"

url_html = requests.get("https://github.com/dfjung4254").text
soup = BeautifulSoup(url_html, "html.parser")
# # # repo 개수


contributions = soup.find('h2', class_="f4 text-normal mb-2").text
print(contributions)

# file = open("C:/Users/dfjun/OneDrive/바탕 화면/Git_info.txt", 'w')
# file.write(contributions)
# file.close()