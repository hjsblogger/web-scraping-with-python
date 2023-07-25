from selenium import webdriver
from os import environ
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Not a recommended practice - need to be replaced with Explicit Waits
import time
import pytest

# Imports for Beautiful Soup
import requests
from bs4 import BeautifulSoup

class locators(object):
    ########## Locators for e-commerce playground ##########

    test_ecomm_url = "https://ecommerce-playground.lambdatest.io/"
    shopcategory = "//a[contains(.,'Shop by Category')]"
    phonecategory = "//span[contains(.,'Phone, Tablets & Ipod')]"

    ########## Locators for YouTube ##########

    # test_yt_url = "https://www.youtube.com/@hjsblogger/videos"
    test_yt_url = "https://www.youtube.com/@LambdaTest/videos"

    loc_contains = "//*[@id='contents']"
    loc_rich_renderer = "style-scope.ytd-rich-grid-renderer"
    loc_grid_row = "ytd-rich-item-renderer.style-scope.ytd-rich-grid-row"

    ########## Definitions for scraping using Beautiful Soup ###########

    test_bs4_url = "https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=57"