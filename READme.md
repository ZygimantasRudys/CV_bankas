# JOB ADVERTISEMENT SCRAPING PROJECT

This project is designed to scrape job advertisements from a specified website using Python, Selenium, and Firefox 
(via GeckoDriver). The script extracts job titles and salaries from multiple pages and logs the results to a file.

## Table of Contents
- Features
- Prerequisites
- Setup
- Usage
- Configuration
- Logging
- Troubleshooting
- Contributing
- License

## Features
- Scrape job advertisements from multiple pages.
- Extract job titles and salaries.
- Configurable parameters via a JSON file.
- Logs both info and error messages to a centralized log file (main.log).

## Prerequisites
- Python 3.6 or higher
- Firefox browser
- GeckoDriver
- Selenium package

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/ZygimantasRudys/CV_bankas.git
    cd job-ad-scraper

2. Install required Python packages:
    ```bash
   pip install selenium

3. Download and setup GeckoDriver:

- Download GeckoDriver from GeckoDriver Releases.
- Extract and place the geckodriver executable in a directory that is included in your system's PATH.
- Update the path in the Python script if necessary:
    ```bash
    ffdriver = webdriver.Firefox(service=FFService(r"C:\path\to\geckodriver.exe"), options=op)

4. Create and configure the config.json file:

Create a config.json file in the project directory with the following content:  

    {
    "url": "https://www.cvbankas.lt/?location%5B0%5D=606&padalinys%5B0%5D=76",
    "selectors": {
            "consent_button": "body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button",
            "salary": "a > div.list_a_wrapper > div.list_cell.jobadlist_list_cell_salary > span > span > span > span.salary_text",
            "job_title": "a > div.list_a_wrapper > div:nth-child(1) > h3",
            "next_page_button": "a.paging_next"
        },
        "port": 4444,
        "logging_level": "INFO",
        "wait_time": 4,
        "last_page_number": 6,
        "log_file": "main.log"
    }

## Usage

1. Run the scraper:
    ```bash
    python job_scraper.py

2. Monitor the output:

- Job titles and salaries will be printed to the console.
- All logs will be written to main.log.

3. Configuration

The config.json file allows you to customize various parameters of the scraper:

- url: The base URL of the job listings.
- selectors: CSS selectors for various elements like the consent button, salary, job title, and next page button.
- port: The port number for the Firefox WebDriver.
- logging_level: The logging level (e.g., INFO, ERROR).
- wait_time: Time to wait (in seconds) before accessing the next page.
- last_page_number: The last page number to scrape.
- log_file: The file where logs will be saved.

## Logging

Logs are written to main.log and include both info and error messages. The logging configuration ensures that all \
relevant information is captured, facilitating easier debugging and monitoring.

## Troubleshooting

- Consent Button Not Found: Ensure the CSS selector for the consent button is correct.
- GeckoDriver Issues: Verify that GeckoDriver is correctly installed and included in your system's PATH.
- Page Loading Issues: Increase the wait_time in the config.json if pages are not loading completely before extraction.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: git checkout -b feature-name.
3. Commit your changes: git commit -m 'Add some feature'.
4. Push to the branch: git push origin feature-name.
5. Open a pull request.