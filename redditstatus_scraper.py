# Import necessary libraries for webdata scraping
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import time

# Set the URL destination to https://redditstatus.com/
url = 'https://redditstatus.com/'

# Scrape the website and return the soup object
def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

# Check if there is a div with class 'unresolved-incidents'
def check_unresolved_incidents(soup):
    if soup.find('div', class_='unresolved-incidents'):
        return True
    else:
        return False

# If there is a div with class 'unresolved-incidents', look for a class
# 'actual-title' and print out the text
def print_unresolved_incidents(soup):
    if soup.find('div', class_='unresolved-incidents'):
        # Search for the div with class 'actual-title'
        title = soup.find('a', class_='actual-title')
        # Print the text of the actual-title
        print(title.text)

# Make this python file a script with __name__ == '__main__'
if __name__ == '__main__':
    # Get the soup object
    soup = get_soup(url)
    print("Getting website...")
    # Check if there are unresolved incidents
    print("Checking for listed unresolved incidents...")
    if check_unresolved_incidents(soup):
        # If there are unresolved incidents, print them
        print("There are unresolved listed incidents: \n")
        print_unresolved_incidents(soup)
    else:
        # If there are no unresolved incidents, print a message
        print('No unresolved listed incidents')