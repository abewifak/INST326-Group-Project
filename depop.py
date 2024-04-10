"""
Application to scrape data from depop and filter prices.
Team members: Ibrahim Wifak, Zijin Wang, Marcelo Soriano, Madina Diane
Date: 4_9_2024
"""
import requests #used for HTTP requests
from bs4 import BeautifulSoup #used for web scraping
import argparse #used to run the script with a command line
from selenium import webdriver #used for automation

class DepopScraper:
    """Class that represents a Depop Scraper

    Attributes:
        url (str): the link based on the category chosen
        price (float): the max price of the items
        size (str): the size of the clothes
    """
    def __init__(self, url, price, size):
        self.url = url
        self.price = price
        self.size = size
    
    def scrape(self):
        """Method that scrapes the product cards
        """
        pass
    
def filter_data_price(products, price):
    """Function to filter the data by price
    
    Parameters:
        products (list): the list of items scraped
        price (float): the price we want to filter by
    
    Returns:
        price_list (list): a list filtered by price
    """
    pass

def filter_data_size(products, size):
    """Function to filter the data by size
    
    Parameters:
        products (list): the list of items scraped
        size (str): the size we want to filter by
    
    Returns:
        size_list (list): a list filtered by size
    """
    pass

def output_data(products):
    """Function that prints the items after they were filtered"""
    pass

def get_data(html):
    """ Function to get the data from the html content

    Parameters:
        html (str): html content
    
    Returns:
        data_list (list): the extracted data
    """
    pass
        
def get_html(url):
    """Function to get the html content

    Parameters:
        url (str): the url to retrieve the html
    
    Returns:
        html (str): html content
    """
    pass

def generate_url(category):
    """Function to generate the url based on the category chosen

    Parameters:
        category (str): the category the user chose

    Returns:
        url (str): the string based on te category
    """
    base = 'https://www.depop.com/category/'

    try:
        if category.lower() == 'mens':
            url = base + "mens/"
            return url
        elif category.lower() == 'womens':
            url = base + "womens/"
            return url
        else:
            raise ValueError("Invalid Category. Please enter mens or womens.")
    except ValueError as e:
        print(e)

def parse_args():
    """ Function to run scripts with command line

    Returns:
        parser.parse_args(): parsed arguments
    """
    parser = argparse.ArgumentParser(description='Scrape Depop listings based on category(mens or womens), price, and size.')
    parser.add_argument('category', type=str, help='Enter "mens" or "womens" as a category')
    parser.add_argument('price', type=float, help='Enter the maximum price for items')
    parser.add_argument('size', type=str, help='Enter your size (e.g. S, M, L, XL)')

    return parser.parse_args()

def main():
    pass

if __name__ == "__main__":
    main()
