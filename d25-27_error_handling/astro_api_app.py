"""Queries the People in Space API for the current people in space"""

import requests


def astros_query():
    """Queries the API"""
    api_url = "http://api.open-notify.org/astros.json"
    try:
        astros_data = requests.get(api_url).json()
        return astros_data
    except requests.exceptions.ConnectionError:
        print("No network connection with API")

def astros_name_parse(astro_data):
    try:
        astronauts = astro_data['people']
        astro_list = []
        for astronaut in astronauts:
            name = astronaut['name']
            astro_list.append(name)
        return astro_list
    except TypeError:
        print("No data to read")


def search_names(name_list):
    name_search = input("What is the name you are searching? ")
    name_in_list = False
    for name in name_list:
        if name_search in name:
            print(name)
            name_in_list = True
    if name_in_list == False:
        print("That astronaut is not in space")

if __name__ == "__main__":
    astros = astros_query()
    astro_list = astros_name_parse(astro_data=astros)
    search_names(name_list=astro_list)

