from bs4 import BeautifulSoup
import lxml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

form_link = "https://docs.google.com/forms/d/e/1FAIpQLSddogmiz2uxRDVKSwxQqvdpCVjSjg7OKD_552anMBk0RjgstQ/viewform?usp=sf_link"

chrome_driver_path = Service("/Users/637godwin/Documents/Web Development/Selenium/chromedriver")

driver = webdriver.Chrome(service=chrome_driver_path)

# driver.get("https://www.zillow.com/west-hartford-ct/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22West%20Hartford%2C%20CT%22%2C%22mapBounds%22%3A%7B%22west%22%3A-72.82283298789461%2C%22east%22%3A-72.66902439414461%2C%22south%22%3A41.67182494207439%2C%22north%22%3A41.82474357942739%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A14552%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

zillow_response = requests.get("https://www.zillow.com/west-hartford-ct/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22West%20Hartford%2C%20CT%22%2C%22mapBounds%22%3A%7B%22west%22%3A-72.82283298789461%2C%22east%22%3A-72.66902439414461%2C%22south%22%3A41.67182494207439%2C%22north%22%3A41.82474357942739%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A14552%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D" ,headers=headers)

#print(zillow_response.text)

soup = BeautifulSoup(zillow_response.text, "html.parser")

link_tags = soup.findAll(name="a", class_="property-card-link")

addresses = []
links = []
new_links = []

for link in link_tags:
    addresses.append(str(link.getText()))
    links.append(str(link.get("href")))

for addy in addresses:
    if addy == " ":
        addresses.remove(addy)
    else:
        pass
for linky in links:
    if linky in new_links:
        pass
    else:
        new_links.append(linky)

print(type(addresses))
print(new_links)



