from selenium import webdriver 
from selenium.webdriver.common.by import By  
from bs4 import BeautifulSoup  
import time 
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  
import requests
# NASA Exoplanet URL
#START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"  # URL of the NASA Exoplanet Catalog

# Webdriver
browser = webdriver.Chrome()  # Initializing Chrome WebDriver

new_planets_data = []


# Convert DataFrame to CSV and save to file
#planet_df_1.to_csv('updated_scraped.csv', index=True, index_label="id")  # Saving the DataFrame as a CSV file

def scrape_more_data(hyperlink):
        page = requests.get(hyperlink)
        #soup = BeautifulSoup(browser.page_source, "html.parser")
        soup = BeautifulSoup(page.content, "html.parser")
        temp_list = []
    
        new_info2extract = ["Planet Type: ", "Discovery Date: ", "Planet Mass: ","Planet Radius: ", 
                                    "Orbital Radius: ", "Orbital Period: ",  "Discovery Method: ",  
                                       ]

        for info_name in new_info2extract:
                try:
                    value= soup.find('div', text=info_name).find_next('span').text.strip()
                    print(value)
                    temp_list.append(value)
                except:
                    temp_list.append('Unknown')

        new_planets_data.append(temp_list)

planet_df_1=pd.read_csv('scraped_data.csv')

for index, row in planet_df_1.iterrows(): 
    print(row['hyperlink']) 
    scrape_more_data(row['hyperlink']) 
    print(f"Data Scraping at hyperlink {index+1} completed")

headers = ["planet_type", "discovery_date", "planet_mass", "planet_radius", "orbital_radius", "orbital_period", "discovery_method"]
new_planet_df_1 = pd.DataFrame(new_planets_data, columns=headers)
new_planet_df_1.to_csv('new_scraped2.csv', index=True, index_label="id")

#scrape_more_data(hyperlink)
