import requests
from bs4 import BeautifulSoup as bs

github_user =  input('Input GitHub user: ')
url = 'https://github.com/'+github_user
print(url)
r = requests.get(url)
soup = bs(r.content, 'html.parser') 
profile_image = soup.find('img', {'alt':'Avatar'})['src']
print(profile_image)