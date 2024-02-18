from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Edge()
driver.get("https://www.srinicorpration.webs.com/products")

html_content = driver.page_source
soup = BeautifulSoup(html_content, "lxml")

product_titles = [product.find("h3").text for product in soup.find_all("div", class_="product-item")]

driver.quit()

print(product_titles)
