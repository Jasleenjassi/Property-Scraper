from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
from pymongo import MongoClient
import sys
search_query = sys.argv[1]

# Set up the web driver
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

# Open a website
driver.get("https://www.99acres.com/")
print("Opened 99acres website")

# Find the search bar and enter a search query
search_bar = wait.until(EC.visibility_of_element_located((By.ID, "keyword2")))
search_bar.send_keys(search_query)

# Locate the search button and click it
search_button = driver.find_element(By.CSS_SELECTOR, "button[data-label='SEARCH_SUBMIT']")
search_button.click()
print("Searching...")
time.sleep(5)

# Print the page title
print("Page title: " + driver.title)

# Parse the HTML of the search results page
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find all of the property listings on the page
property_listings = soup.find_all("div", class_="srpTuple__cardWrap tupleCardWrap")
property_details = []

# Extract property details and store them in a list
for property_listing in property_listings:
    property_name = property_listing.find("h2", class_="srpTuple__tupleTitleOverflow").text
    property_cost = property_listing.find('td', class_='srpTuple__col title_semiBold').text
    property_area = property_listing.find("td", id="srp_tuple_primary_area").text
    property_type = property_listing.find("td", id="srp_tuple_bedroom").text
    property_locality = property_listing.find("a", class_='srpTuple__dFlex').text
    individual_property_link = property_listing.find("a", class_="body_med srpTuple__propertyName")["href"]

    property_details.append({
        "property_name" : property_name,
        "property_cost" : property_cost,    
        "property_area" : property_area,
        "property_type" : property_type,
        "property_locality": property_locality,
        "property_link" : individual_property_link
    })

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Scrap_Data"]
collection = db["99acres"]

# Insert property details into the MongoDB collection
collection.insert_many(property_details)

# Print both the property name, cost, and area for each listing
for property_detail in property_details:
    print("Name: " + property_detail["property_name"])
    print("Cost: " + property_detail["property_cost"])
    print("Area: " + property_detail["property_area"])
    print("Type: " + property_detail["property_type"])
    print("Locality: " + property_detail["property_locality"])
    print("Link: " + property_detail["property_link"])
    print()

# Save a screenshot of the search results
driver.save_screenshot('results.png')

# Close the web driver
driver.quit()