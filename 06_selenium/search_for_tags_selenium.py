from selenium import webdriver
from time import sleep
driver = webdriver.Chrome('../drivers/chromedriver.exe')

book_title = 'Мастер и Маргарита'.lower()
driver.set_page_load_timeout(10)
driver.get('https://www.litres.ru/pages/rmd_search/?q=' + book_title)
# driver.find_element_by_id('search__content')
# driver.find_element_by_class_name('result_container')


search_results = driver.find_element_by_class_name('cover_href').click()
sleep(5)

tags_list = driver.find_element_by_xpath("//div[@class='biblio_book_info']").text

print(tags_list)
