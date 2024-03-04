from selenium import webdriver
from selenium.webdriver.chrome.options import Options
response = 200

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

while response != []:
    response = driver.get("https://www.lectio.dk/lectio/71/default.aspx")
    print(response)
