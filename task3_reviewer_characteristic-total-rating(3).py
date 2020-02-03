import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import csv

#first setup the driver;
chromedriver="/Users/apple/Downloads/chromedriver"
chrome_options= webdriver.ChromeOptions()

chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver =webdriver.Chrome(executable_path=chromedriver)
movie_detail_driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=chrome_options)
driver.get("https://www.imdb.com/search/title/?genres=action&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=037ZPKFCRZAQE2S82WZC&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1")


movie_list_total = driver.find_elements_by_xpath("//h3[@class ='lister-item-header']")
movie_html_list=[]
final_list=[]


for movie_name in movie_list_total:
    a_attribute= movie_name.find_element_by_tag_name("a")
    movie_html = a_attribute.get_attribute("href")
    movie_html_list.append(movie_html)

reviewer_html_list=[]

for movie in movie_html_list:
    info_list = []
    movie_detail_driver.get(movie)
    movie_info = movie_detail_driver.find_element_by_xpath("//div[@class ='title_wrapper']").find_element_by_tag_name("h1").text
    info_list.append(movie_info)

    movie_reviewer=movie_detail_driver.find_element_by_css_selector("a[href*='tt_ov_rt']")
    html=movie_reviewer.get_attribute('href')
    ##get id;

    movie_detail_driver.get(html)

    rate = []
    review_rank = movie_detail_driver.find_elements_by_xpath("//div[@class ='rightAligned']")
    review_users = movie_detail_driver.find_elements_by_xpath("//div[@class ='leftAligned']")
    for users in review_users:
        user_text = users.text
        rate.append(user_text)
    info_list.extend(rate[1:11])
    final_list.append(info_list)

with open("test.csv",'a') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(
        ['title', '10','9','8','7','6','5','4','3','2','1'])

    csv_writer.writerows(final_list)


for i in range(0,26):
    next_page=driver.find_element_by_link_text("Next »")
    next_page.click()
    current_page=driver.current_window_handle

    movie_list_total = driver.find_elements_by_xpath("//h3[@class ='lister-item-header']")
    movie_html_list = []
    final_list = []
    for movie_name in movie_list_total:
        a_attribute = movie_name.find_element_by_tag_name("a")
        movie_html = a_attribute.get_attribute("href")
        movie_html_list.append(movie_html)

    #reviewer_html_list = []

    for movie in movie_html_list:
        info_list = []
        movie_detail_driver.get(movie)
        movie_info = movie_detail_driver.find_element_by_xpath("//div[@class ='title_wrapper']").find_element_by_tag_name("h1").text
        info_list.append(movie_info)

        movie_reviewer = movie_detail_driver.find_element_by_css_selector("a[href*='tt_ov_rt']")
        html = movie_reviewer.get_attribute('href')
        ##get id;

        movie_detail_driver.get(html)
        rate = []
        review_rank = movie_detail_driver.find_elements_by_xpath("//div[@class ='rightAligned']")
        review_users = movie_detail_driver.find_elements_by_xpath("//div[@class ='leftAligned']")
        for users in review_users:
            user_text = users.text
            rate.append(user_text)
        info_list.extend(rate[1:11])
        final_list.append(info_list)

    with open("test.csv", 'a') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(final_list)

driver.close()
movie_detail_driver.close()
#
#
