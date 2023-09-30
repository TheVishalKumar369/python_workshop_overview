import requests
from bs4 import BeautifulSoup

res=requests.get("https://pypi.org/project/requests/")
print(res)

soup = BeautifulSoup(res.text,"html.parser")
command = soup.find("span",{"id":"pip-command"})

# print(command)
# if command == None:
#     print("Command not found")
# else:
#     print(command.text)

quotes = soup.find_all("span",{"class":"text"})

for q in quotes:
    print(q.text)