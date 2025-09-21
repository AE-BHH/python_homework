from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import pandas as pd

# Task 2: Understanding HTML and the DOM for the Durham Library Site
li_class = "cp-search-result-item"
title_class = "title-content"
author_class = "author-link"
type_year = "display-info-primary"


# Task 3: Write a Program to Extract this Data

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

main_url = "https://durhamcounty.bibliocommons.com/v2/search"
query = "learning%20spanish"
results = []
max_pages = 5
page_number = 1

while page_number <= max_pages:
    if page_number == 1:
        url = f"{main_url}?query={query}&searchType=smart"
    else:
        url = f"{main_url}?query={query}&searchType=smart&page={page_number}"

    print(f"Scrapping page {page_number}: {url}")
    driver.get(url)

    try:
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, li_class)))

        time.sleep(3)

    except Exception as e:
        print(f"No result found on page {page_number}")
        break

    items = driver.find_elements(By.CLASS_NAME, f"{li_class}")
    print(len(items))

    if len(items) == 0:
        print("No items found.")
        break

    for item in items:
        try:

            title = item.find_element(By.CLASS_NAME, title_class).text.strip()

            authors = [
                author.text.strip()
                for author in item.find_elements(By.CLASS_NAME, author_class)
            ]
            author_text = "; ".join(authors) if authors else "unknown author"

            format_year = item.find_element(By.CLASS_NAME, type_year).text.strip()

            data = {
                "Title": title,
                "Author": author_text,
                "Format-Year": format_year,
                "Page": page_number,
            }

            results.append(data)
            # print(results)
        except Exception as e:
            print(f"Error: {e}")
            continue

    page_number += 1
    time.sleep(3)

# Task 4: Writing out the data to CSV and JSON

with open("book_data.json", "w") as file:
    json.dump(results, file, indent=2)

df = pd.DataFrame(results)
print(df)


df.to_csv("get_book.csv", index=False)

driver.quit()
