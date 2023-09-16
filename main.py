from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

# driver to connect to site
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
website = 'https://adamchoi.co.uk/overs/detailed'
time.sleep(1)
driver.get(website)

# allow page to fully load.
time.sleep(1)

# button press
driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]').click()

# dropdown selector
dropdown = Select(driver.find_element(By.ID, 'country'))
dropdown.select_by_visible_text('Japan')
# needed as the page is dynamically loading the info and the script is too fast.
time.sleep(3)

matches = driver.find_elements(By.TAG_NAME, 'tr')
# inline comments are the xpath to these elements on the page.
date = []  # //tr/td[1]
homeTeam = []  # //tr/td[2]
awayTeam = []  # //tr/td[4]
score = []  # //tr/td[3]

for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    xHome = match.find_element(By.XPATH, './td[2]').text
    homeTeam.append(xHome)
    print(xHome)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    awayTeam.append(match.find_element(By.XPATH, './td[4]').text)
driver.quit()
# dataframe
df = pd.DataFrame({'date': date, 'home-team': homeTeam, 'score': score, 'away-team': awayTeam})
df.to_csv('japan.csv', index=False)
print(df)

# time.sleep(1000)
# driver.quit()
