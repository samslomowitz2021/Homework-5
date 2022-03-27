
import time
from datetime import datetime

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import numpy as np

import requests

class ScrapingHelper():
    def __init__(self):
        self.executable_path = {'executable_path': ChromeDriverManager().install()}
        self.browser = Browser('chrome', **executable_path, headless=False, incognito=False)
        url = 'https://jquery.com/download/'
    def scrape_mars(self):
        browser.visit(url)
        
        return(data)
