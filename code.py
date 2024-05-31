import logging
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FFService
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Load configuration from JSON file
with open('config.json') as config_file:
    config = json.load(config_file)

# Configure logging
logging.basicConfig(
    level=getattr(logging, config['logging_level'].upper()),
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(config['log_file']),
        logging.StreamHandler()
    ]
)

# Initialize the Firefox driver
op = webdriver.FirefoxOptions()
ffdriver = webdriver.Firefox(service=FFService(r"C:\Users\PAIN\Desktop\geckodriver.exe"), options=op)

# Function to construct the URL for a given page number
def construct_url(page_number: int):
    base_url = config['url']
    if page_number > 1:
        return f"{base_url}&page={page_number}"
    return base_url

# Load the first page
ffdriver.get(construct_url(1))
ffdriver.maximize_window()

# Wait for the consent button and click it
try:
    WebDriverWait(ffdriver, timeout=10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, config['selectors']['consent_button'])
        )
    )
    allow_selected_cookies_button = ffdriver.find_element(
        By.CSS_SELECTOR,
        config['selectors']['consent_button']
    )
    allow_selected_cookies_button.click()
except NoSuchElementException as e:
    logging.error("Consent button not found", exc_info=True)

# Function to extract data from the page
def extract_data():
    try:
        price_elements = ffdriver.find_elements(By.CSS_SELECTOR, config['selectors']['salary'])
        for price in price_elements:
            logging.info(f"Salary: {price.text}")
            print(price.text)

        job_add_titles = ffdriver.find_elements(By.CSS_SELECTOR, config['selectors']['job_title'])
        for title in job_add_titles:
            logging.info(f"Job Title: {title.text}")
            print(title.text)
    except Exception as e:
        logging.error("Error extracting data", exc_info=True)

# Function to wait for the page to load
def wait_for_page_load(timeout=10):
    try:
        WebDriverWait(ffdriver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config['selectors']['job_title']))
        )
    except NoSuchElementException:
        logging.info("No new job titles found. Possible end of results.")
    except Exception as e:
        logging.error("Error waiting for page load", exc_info=True)

# Iterate through pages
page_number = 1
last_page_number = config['last_page_number']
wait_time = config['wait_time']

while page_number <= last_page_number:
    extract_data()
    page_number += 1
    if page_number > last_page_number:
        logging.info("Reached the last page")
        break
    next_url = construct_url(page_number)
    logging.info(f"Fetching URL: {next_url}")
    ffdriver.get(next_url)
    wait_for_page_load()
    logging.info("URL data fetched!")
    time.sleep(wait_time)

input("Finished, click ENTER button to exit")
ffdriver.close()
