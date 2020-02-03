import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import csv

#chromedriver="/Users/apple/Downloads/chromedriver"
chromedriver="/Users/apple/Downloads/chromedriver"
chrome_options= webdriver.ChromeOptions()

driver =webdriver.Chrome(executable_path=chromedriver)
movie_detail_driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=chrome_options)
driver.get("https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&sort=user_rating,desc&start=201&ref_=adv_nxt")
movie_list_total = driver.find_elements_by_xpath("//h3[@class ='lister-item-header']")

file = open("test.csv",'a')
csv_writer = csv.writer(file)
csv_writer.writerow(
    ['number of people like', 'number of people follow'])

movie_html_list=[]

for movie_name in movie_list_total:
    a_attribute= movie_name.find_element_by_tag_name("a")
    movie_html = a_attribute.get_attribute("href")
    movie_html_list.append(movie_html)


for movie in movie_html_list:
    info_list = []
    movie_detail_driver.get(movie)
    movie_info = movie_detail_driver.find_element_by_xpath("//div[@class ='title_wrapper']").find_element_by_tag_name("h1").text
    info_list.append(movie_info)
    try:
        movie_reviewer=movie_detail_driver.find_element_by_css_selector("a[href*='tt_pdt_ofs_offsite']")
        html=movie_reviewer.get_attribute('href')
    ## target the elements of interest
        movie_detail_driver.get(html)
        ###Try this in normal cases

        thing = movie_detail_driver.find_elements_by_xpath("//div[@class = '_4bl9']")

        list = []
        count = 0
    #get data
        for each in thing:
            if count == 1 or count == 2:
                list.append(each.text)
                count+=1
            else:
                count+=1
        #clean data;
        #take out unnecesary text, and then take out the comma, then make a transfer on data type;
        list = [element.replace("people like this","") for element in list]
        list = [element.replace("people follow this","") for element in list]
        list = [element.replace(",","") for element in list]
        list = [element.replace(" ","") for element in list]
        list = [int(element) for element in list]
        csv_writer.writerow(list)
    ##Except for extreme cases where we don't have OFFICIAL websites
    except:
        csv_writer.writerow(['NA','NA'])
driver.close()
