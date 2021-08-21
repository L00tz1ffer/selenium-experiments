import random
import time

from selenium import webdriver
from selenium.common.exceptions import *

def searchByGoogle(driver, sQuery, timeframe):

    performSearch(driver, "google", sQuery, timeframe)

def searchByDuckDuckGo(driver, sQuery, timeframe):
    performSearch(driver, "ddg", sQuery, timeframe)




def performSearch(driver, sEngine, sQuery, timeframe):


    if sEngine == "google":
        cConsent = "L2AGLb"
        sf = "q"
        url = 'https://www.google.com/xhtml'


    if sEngine == "ddg":
        cConsent = ""
        sf = "search__input--adv"
        url = 'https://duckduckgo.com/'

    driver.get(url)



    try:
        passbutton = driver.find_element_by_id(cConsent)
        passbutton.click()
    except NoSuchElementException:
        print("id " + cConsent + " not found")
    except ElementNotInteractableException:
        print("id " + cConsent + " not interactable")

    try:
         search_field = driver.find_element_by_name(sf)
         search_field.clear()

         typeQuery(search_field, sQuery, timeframe)

         search_field.submit()
    except NoSuchElementException:
        print("id " + sf + " not found")
    except ElementNotInteractableException:
        print("id " + sf + " not interactable")

    try:
        search_field = driver.find_element_by_class_name(sf)
        search_field.clear()

        typeQuery(search_field,sQuery, timeframe)

        search_field.submit()
    except NoSuchElementException:
        print("id " + sf + " not found")
    except ElementNotInteractableException:
        print("id " + sf + " not interactable")

    time.sleep(random.randint(1,500)/100)




def typeQuery (inputField, input, timeframe):
    for letter in input:
        print("Schreibe: " + letter)
        inputField.send_keys(letter)
        calculateTimeFrameMs(timeframe)

def getDriver():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.delete_all_cookies()
    time.sleep(1)
    return driver

def killDriver(driver):
    time.sleep(1)
    driver.quit()

def calculateTimeFrameMs(timeframe):
    wait = random.randint(1, timeframe) / 100
    print("warte   : "+ str(wait) + "s")
    time.sleep(wait)
