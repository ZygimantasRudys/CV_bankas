import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FFService
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

op = webdriver.FirefoxOptions()
ffdriver = webdriver.Firefox(service=FFService(r"C:\Users\PAIN\Desktop\geckodriver.exe"), options=op)
ffdriver.get('https://www.cvbankas.lt/?location%5B0%5D=606&padalinys%5B0%5D=76')
ffdriver.maximize_window()

WebDriverWait(ffdriver, timeout=10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button")))
print(f"{ffdriver.title}", flush=True)
allow_selected_cookies_button = ffdriver.find_element(By.CSS_SELECTOR, "body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button") # //*[@name="q"]
allow_selected_cookies_button.click()

# extracting data from the page
def extract_data():
    price_elements = ffdriver.find_elements(By.CSS_SELECTOR, "a > div.list_a_wrapper > div.list_cell.jobadlist_list_cell_salary > span > span > span > span.salary_text")
    for price in price_elements:
        print(price.text)

    job_add_titles = ffdriver.find_elements(By.CSS_SELECTOR, "a > div.list_a_wrapper > div:nth-child(1) > h3")
    for title in job_add_titles:
        print(title.text)


while True:
    extract_data()

    try:
        # Find the "Next Page" button and click it using JavaScript
        next_page_button = ffdriver.find_element(By.CSS_SELECTOR, "#main > ul > li:nth-child(2) > a")
        ffdriver.execute_script("arguments[0].click();", next_page_button)
        # Add a delay to allow the next page to load completely
        time.sleep(2)
    except NoSuchElementException:
        print("Reached the last page")
        break


input("Finished, click ENTER button to exit")
ffdriver.close()