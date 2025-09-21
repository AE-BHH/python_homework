from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import pandas as pd

url = "https://owasp.org/www-project-top-ten/"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(url)
print(driver.title)

try:

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//section[@id='sec-main']//ul[2]/li/a")
        )
    )

    items = driver.find_elements(By.XPATH, "//section[@id='sec-main']//ul[2]/li/a")

    data = []

    for item in items:
        title = item.text.strip()
        link = item.get_attribute("href")
        if title and link:
            data.append({"Title": title, "Link": link})

    print(data)
except Exception as e:
    print(f"Error occurred while scraping the data: {e}")


df = pd.DataFrame(data)
print(df)

df.to_csv("owasp_top_10.csv", index=False)


driver.quit()
