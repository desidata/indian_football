import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
#import seaborn as sns; sns.set(style="ticks", color_codes=True)
import geopandas as gpd
from geopandas import GeoDataFrame
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import math
import plotly.express as px
from tqdm import tqdm
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

years = list(range(2002, 2024))
data = {}
players_data= {}
for year in years:
    url = 'https://www.national-football-teams.com/country/86/'+str(year)+'/India.html'
    page = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
    soup = BeautifulSoup(page.content, 'html.parser')
    pl_table=soup.find('table', class_='table player table-sm table-hover sortable')
    links = pl_table.find_all('a')
    players = []
    scraped_data=[]
    for i in links:
        if '/player/' in i['href']:
            if '/player/picture' not in i['href']:
                players.append(i['href'])
    #player_year.append(players)
    base = 'https://www.national-football-teams.com'
    for item in players:
        url = base+item
        print(url)
        page = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
        soup = BeautifulSoup(page.content, 'html.parser')

        # Get the name

        divs_name_parent = soup.find('div', class_='col-12 text-center')
        #print(divs_name_parent)
        # Find the span elements with itemprop attributes
        family_name_span = soup.find('span', itemprop='familyName')
        given_name_span = soup.find('span', itemprop='givenName')

        # Extract the text from the span elements
        family_name = family_name_span.text.strip()
        given_name = given_name_span.text.strip()
        full_name = given_name+' '+family_name
        
        # Get the birthplace
        divs_parent = soup.find('div', class_='col-lg-12 col-xl-8 mb-lg text-left')
        #print(divs_parent)
        divs_child = divs_parent.find_all('div', class_="row")
        #print(len(divs_child))
        divs_child = divs_child[len(divs_child)-2].find_all('div', class_="col-6")
        place = divs_child[1].text
        count_letters = sum(1 for char in place if char.isalpha())
        #print(place)
        if count_letters >= 2:
            print(f'Birthplace of player {full_name} is {place}')
            player_info = {"name": full_name, "birthplace": place}
            scraped_data.append(player_info)
        else:
            try:
                print(f"{place} does not contain letters.\n looking for birthplace...")
                divs_child = divs_parent.find_all('div', class_="row")
                divs_child = divs_child[len(divs_child)-1].find_all('div', class_="col-6")
                new_place = divs_child[1].text
                count_letters = sum(1 for char in new_place if char.isalpha())
                #print(count_letters)
                if count_letters >= 2:
                    new_place = new_place.strip()[:-8]
                    print(f'Birthplace of player {full_name} is {new_place}')
                    player_info = {"name": full_name, "birthplace": new_place}
                    scraped_data.append(player_info)
                else:
                    print(f"Birthplace of player {full_name} not found! Checking further...")
            except:
                #print(f"{place} does not contain letters.\n looking for birthplace...")
                divs_child = divs_parent.find_all('div', class_="row")
                divs_child = divs_child[5].find_all('div', class_="col-6")
                new_place = divs_child[1].text
                
                count_letters = sum(1 for char in new_place if char.isalpha())
                #print(count_letters)
                if count_letters >= 2:
                    print(f'Birthplace of player {full_name} is {new_place}')
                    player_info = {"name": full_name, "birthplace": new_place}
                    scraped_data.append(player_info)
                else:
                    print(f"Birthplace of player {full_name} not found!!")
        # Update the players_data dictionary with scraped data for the current year
        players_data[year] = scraped_data

        # Optionally, you can update the main data dictionary if needed
        data[year] = players_data[year] 

with open('players_birthplace.json', "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"All done")   

