import tkinter as tk
import requests
from bs4 import BeautifulSoup


window = tk.Tk()
window.title("Country App")
window.geometry("300x200")

label = tk.Label(window, text="Enter a Country name in the box below!")
label.pack()
entry = tk.Entry(width=30, )
entry.pack()


def search_country():
    
    
    response =  requests.get('https://scrapethissite.com/pages/simple/')

    soup = BeautifulSoup(response.content, 'html.parser')

    user = entry.get().title()

    found = False

    countries = soup.find_all('div', class_ ='col-md-4 country')
    for country in countries:
        
        name = country.find('h3', class_='country-name')
        name2 = name.get_text(strip=True)
        if user == name2:
    
            name = country.find('h3', class_='country-name')
            capital = country.find('span', class_='country-capital')
            population = country.find('span', class_='country-population')
            label.config(text=f'{name.get_text(strip=True)} | capital: {capital.get_text(strip=True)} | population: {population.get_text(strip=True)}')
            found = True

    if not found:
        label.config(text='country not found!')
    
    
button = tk.Button(window, text="click me to see the country", command=search_country)
button.pack()

window.mainloop()