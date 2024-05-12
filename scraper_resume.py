# Jamie Morrissey
# Western Governors University
# For Python Developer Resume
# Scraping a Job Portal
# 5/11/2014

import requests
from bs4 import BeautifulSoup
from datetime import datetime

dt = datetime.now()

ts = datetime.timestamp(dt)

URL = "https://sandiego.craigslist.org/search/csd/sof"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

job_elements = soup.find_all("div", class_="title")

job_elements = soup.find_all("li", class_="cl-static-search-result")

for job_element in job_elements:
    title_element = job_element.find("div", class_="title")
    location_element = job_element.find("div", class_="location")
    link = job_element.find("a")
    href_att = link.get("href")
    print(title_element.text.strip())
    print(location_element.text.strip())
    print("url: ", href_att)

    # completed adding HTTP link support
    # output current date and time

    print("Date and time is: ", dt)
    print("Timestamp is:", ts)