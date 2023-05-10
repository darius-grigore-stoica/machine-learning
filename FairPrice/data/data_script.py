import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import numpy as np

camere_training = []
dim_training = []
cartiere_training = []
preturi_training = []
camere_testing = []
dim_testing = []
cartiere_testing = []
preturi_testing = []

page = 0
while page < 17:
    if page != 9:
        source = requests.get(
            f'https://www.napocaimobiliare.ro/vanzare-apartamente-cluj?transaction=0&sortorder=created_desc&page={page}')
        anunturi = soup(source.content, features="html.parser")

        for anunt in anunturi.find_all("p"):
            prev = anunt.find_previous_sibling("h2")
            if prev:
                prev_div = prev.find_parent(["h2", "div"])
                if prev_div:
                    price_div = prev_div.find_parent([prev_div, "div"])
                    prev_div.text.split()
                prev.text.split()
            anunt.text.split()

            i = 0
            while i < len(anunt.text) - 2:
                if not anunt.text[i].isnumeric():
                    i = i + 1
                else:
                    if anunt.text[i + 2] == 'c' and prev.text[len(prev.text) - 11] == "C":
                        if page < 12:
                            camere_training.append(int(anunt.text[i]))
                        else:
                            camere_testing.append(int(anunt.text[i]))
                        i = i + 15
                        if anunt.text[i] != " ":
                            metrii = anunt.text[i] + anunt.text[i + 1]
                            if page < 12:
                                dim_training.append(int(metrii))
                            else:
                                dim_testing.append(int(metrii))
                        else:
                            metrii = anunt.text[i + 1] + anunt.text[i + 2]
                            if page < 12:
                                dim_training.append(int(metrii))
                            else:
                                dim_testing.append(int(metrii))



                        prev.text.split(",")
                        dict_cartier = {
                            "Centru": 0,
                            "Manastur": 3.5,
                            "Zorilor": 2.5,
                            "Buna": 6.5,
                            "Marasti": 3.5,
                            "Gheorgheni": 5.5,
                            "Borhanci": 5.3,
                            "Plopilor": 2.0,
                            "Grigorescu": 3.0,
                            "Intre": 3.0,
                            "Europa": 9.0,
                            "Iris": 2.0,
                            "Someseni": 4.0,
                            "Bulgaria": 4.7,
                            "Sopor": 5.6,
                            "Dambul": 3.7,
                            "Floresti": 8.7,
                            "Andrei": 1.8,
                            "Gruia": 2.3,
                            "Baciu": 7.9
                        }
                        j = 34
                        cartier = ""
                        if j < len(prev.text) and j < 37:
                            while prev.text[j] != " ":
                                cartier = cartier + prev.text[j]
                                j = j + 1
                            cartier = cartier.split(",")

                            if page < 12:
                                cartiere_training.append(dict_cartier[cartier[0]])
                            else:
                                cartiere_testing.append(dict_cartier[cartier[0]])

                        price_div = price_div.find("div", class_="price")
                        price_div.text.split()
                        p = 0
                        price = ""
                        while price_div.text[p] != " " and p < 7:
                            if price_div.text[p] == ",":
                                price = price + ""
                                p = p + 1
                            price = price + price_div.text[p]
                            p = p + 1
                        if page < 12:
                            preturi_training.append(int(price))
                        else:
                            preturi_testing.append(int(price))
                    else:
                        i = i + 1
    page = page + 1

df = pd.DataFrame(columns=['Nr', 'Camere', 'Dim', 'Cartier', 'Pret'])
for i in range(len(camere_training)):
    df.loc[i] = [str(i), camere_training[i], dim_training[i], cartiere_training[i], preturi_training[i]]
df.to_csv('../linearReg/training_data.csv', index=False)


df = pd.DataFrame(columns=['Nr', 'Camere', 'Dim', 'Cartier', 'Pret'])
for i in range(len(camere_testing)):
    df.loc[i] = [str(i), camere_testing[i], dim_testing[i], cartiere_testing[i], preturi_testing[i]]
df.to_csv('../linearReg/testing_data.csv', index=False)