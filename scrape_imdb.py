# Importing the package
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from pandas import DataFrame
import re

# Open url
imdb = 'https://www.imdb.com/'
driver = webdriver.Chrome("D:/webdrivers/chromedriver.exe")
driver.get(imdb)
driver.maximize_window()

# Xpath of menu button
menu = '//*[@id="imdbHeader-navDrawerOpen--desktop"]/div'

# Click menu
menu_button = driver.find_element(By.XPATH, menu)
menu_button.click()

# Wait the page until fully loaded
time.sleep(3)

# Find link Most Popular TV Shows and click
popular_show = driver.find_element(By.LINK_TEXT, "Most Popular TV Shows")
popular_show.click()

# Scrape the list of Popular Shows
titles = driver.find_elements(By.CLASS_NAME, "titleColumn")
ratings = driver.find_elements(By.CLASS_NAME, "ratingColumn.imdbRating")
title = []
year = []
rating = []

for x in titles:
    # List of texts title, year
    a = x.text

    # Get the movie title
    movie_title = re.search(r'^.*(?=\()', a).group(0)
    title.append(movie_title)

    # Get the movie year
    movie_year = re.search(r'(?<=\().*(?=\))', a).group(0)
    year.append(movie_year)

# Get rating
for y in ratings:
    b = y.text
    rating.append(b)

# Compile list to single Data Frame
popular_shows = pd.DataFrame(list(zip(title, year, rating)), columns = ["title", "year", "rating"])
print(popular_shows)

# Data frame to csv file
imdb = popular_shows.to_csv("imdb.csv", index=False)
