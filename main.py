import requests
from bs4 import BeautifulSoup
import pandas as pd
from sys import stdout

class Scrapping():
    def __init__(self) -> None:
        # Define variables
        #URL base to Mercadolibre List
        self.url: str = 'https://listado.mercadolibre.com.'
        self.product: str = ''
        #All countries where mercadolibre operates
        self.countries: dict = {
            "AR": "Argentina",
            "BO": "Bolivia",
            "BR": "Brasil",
            "CH": "Chile",
            "CO": "Colombia",
            "CR": "Costa Rica",
            "DO": "Dominicana",
            "EC": "Ecuador",
            "GT": "Guatemala",
            "HN": "Honduras",
            "MX": "México",
            "NI": "Nicaragua",
            "PA": "Panamá",
            "PY": "Paraguai",
            "PE": "Perú",
            "SV": "El Salvador",
            "UY": "Uruguay",
            "VE": "Venezuela",
        }
        #where save data
        self.data = []
    def menu(self):
        #display menu
        print("Elige el pais para el scraping:")
        for key, value in self.countries.items():
            print(f"{key}. {value} ")
        #validate valid option
        while True:
            selection: str = str.upper(input("Codigo del pais: "))
            if selection in self.countries:
                self.url += str.lower(selection) + '/'
                break
            else:
                stdout.write("Debe elegir un codigo válido")
        #input product name
        while self.product == '':
            self.product = input("Nombre del producto: ")
        #replace spaces with underscores
        self.product = self.product.replace(' ', '-')
        self.url += self.product
                
    def request(self):
        page_number = 1
        #for cycle to perform the paging
        for i in range(1, 10000, 1):
            req = requests.get(self.url + f"_Desde_{page_number}_NoIndex_True")
            page_number += 50
            soup = BeautifulSoup(req.text, 'html.parser')
            #Find every item in the list of this page
            data = soup.find_all('li', class_='ui-search-layout__item')
            
            #if not data found in page for brakes
            if not data:
                break
            
            stdout.write('\rScrapeando pagina ' + str(i))
            stdout.flush()


            for article in data:
                # get the title
                try:
                    title = article.find('h2').text
                except:
                    title = article.find('h3', class_='ui-search-item__title').text
                # get the price
                price = article.find('span', class_='andes-money-amount__fraction').text
                # get free 
                if article.find('div', class_='poly-component__shipping') == None:
                    free = 'No'
                else:
                    free = 'Si'
                    
                # get the url post
                post_link = article.find("a")["href"]
                # get the url image
                try:
                    img_link = article.find("img")["data-src"]
                except:
                    img_link = article.find("img")["src"]
                
                # save in a dictionary
                post_data = {
                    "title": title,
                    "price": price,
                    "free_shipping": free,
                    "post link": post_link,
                    "image link": img_link            
                }
                # save the dictionaries in a list
                self.data.append(post_data)
        
        
    def export_to_csv(self):
    # export to a csv file
        df = pd.DataFrame(self.data)
        df.to_csv(f"data/mercadolibre-scraped-data-{self.product}.csv", sep=";")
                
                
                
                
        
if __name__ == "__main__":
    scraper = Scrapping()
    scraper.menu()
    scraper.request()
    scraper.export_to_csv()