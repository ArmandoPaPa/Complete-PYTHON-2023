from pages.quotes_page import QuotesPage, InvalidTagForAuthorError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# chrome = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# chrome = webdriver.Chrome(executable_path='C:\\Users\\Armando PaPa\\Downloads\\chromedriver_win32\\chromedriver.exe')
# chrome.get('http://quotes.toscrape.com/search.aspx')
# page = QuotesPage(chrome)

# author = input("Enter the author you'd like quotes from: ")
# page.select_author(author)

# tags = page.get_available_tags()
# print("Select one of these tags: [{}]".format(" | ".join(tags)))
# selected_tag = input("Enter your tag: ")

# page.select_tag(selected_tag)
# page.search_button.click()
# print(page.quotes)

# --

try:
    author = input("Enter the author you'd like quotes from: ")
    tag = input("Enter your tag: ")

    # service = Service("/usr/local/bin/chromedriver")
    service = Service("C:\\Users\\ArmandoPaPa\\Downloads\\chromedriver_win32\\chromedriver.exe")
    chrome = webdriver.Chrome(service=service)
    chrome.get("http://quotes.toscrape.com/search.aspx")
    page = QuotesPage(chrome)

    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception:
    print("An unknown error occurred. Please try again.")
