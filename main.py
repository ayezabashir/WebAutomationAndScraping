from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://neuralnine.com/")

links = driver.find_elements("xpath", "//a[@href]")
for link in links:
    if "Books" in link.get_attribute("innerHTML"):
        link.click()
        break
    # print(link.get_attribute("innerHTML"))

book_links = driver.find_elements("xpath",
                                  "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(.,'7 IN 1']]][count(.//a)=2]//a")

for book_link in book_links:
    print(book_link.get_attribute("href"))
