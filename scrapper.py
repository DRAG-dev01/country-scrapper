import requests
from bs4 import BeautifulSoup

response  =  requests.get('https://scrapethissite.com/pages/simple/')

soup = BeautifulSoup(response.content, 'html.parser')

user = input('enter your country here: ').title()

found = False

countries = soup.find_all('div', class_ ='col-md-4 country')
for country in countries:
    name = country.find('h3', class_='country-name')
    name2 = name.get_text(strip=True)
    if user == name2:

        name = country.find('h3', class_='country-name')
        capital = country.find('span', class_='country-capital')
        population = country.find('span', class_='country-population')
        print(f'{name.get_text(strip=True)} | capital: {capital.get_text(strip=True)} | population: {population.get_text(strip=True)}')
        found = True

if not found:
    print('country not found!')
        
    
