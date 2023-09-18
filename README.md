 ## Property Scraper

This Python script uses Selenium and BeautifulSoup to scrape property listings from the 99acres website and stores the results in a MongoDB database.
### Prerequisties
* Django
* pymongo
* selenium
* beautifulsoup4
### Step-by-Step Explanation

1. First, the script imports the necessary libraries.
2. Then, it sets up a web driver and opens the 99acres website.
3. Next, it finds the search bar and enters a search query.
4. After that, it clicks the search button and waits for the results to load.
5. Once the results have loaded, the script parses the HTML of the search results page and finds all of the property listings.
6. For each property listing, the script extracts the property name, cost, area, type, locality, and link.
7. Then, the script connects to a MongoDB database and inserts the property details into a collection.
8. Finally, the script prints the property name, cost, and area for each listing and saves a screenshot of the search results.

### Code Snippets

Here are some code snippets from the script:

```python
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
```

```python
# Parse the HTML of the search results page
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find all of the property listings on the page
property_listings = soup.find_all("div", class_="srpTuple__cardWrap tupleCardWrap")
property_details = []

# Extract property details and store them in a list
for property_listing in property_listings:
    property_name = property_listing.find("h2", class_="srpTuple__tupleTitle

