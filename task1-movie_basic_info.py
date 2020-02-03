chromedriver="/Users/apple/Downloads/chromedriver"

from selenium import webdriver
import csv

#first setup the driver;
chrome_options= webdriver.ChromeOptions()

#no need to open the chrome
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver =webdriver.Chrome(executable_path=chromedriver)
driver.get("https://www.imdb.com/search/title/?genres=action&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=037ZPKFCRZAQE2S82WZC&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1")
#write into excel
file=open('test.csv','a')
writer=csv.writer(file)
writer.writerow(['movie_name','length','year','rate','genre','votes','gross'])

##find all title columns & url;
movie_list = driver.find_elements_by_xpath("//h3[@class ='lister-item-header']")
movie_year = driver.find_elements_by_xpath("//span[@class = 'runtime']")
movie_time = driver.find_elements_by_xpath("//span[@class = 'lister-item-year text-muted unbold']")
movie_rate = driver.find_elements_by_xpath("//div[@class = 'ratings-bar']")
movie_genre=driver.find_elements_by_xpath("//span[@class = 'genre']")
movie_votes_gross=driver.find_elements_by_xpath("//p[@class = 'sort-num_votes-visible']")


for movie, year, time, rate, genre, vote_gross in zip(movie_list, movie_year, movie_time, movie_rate, movie_genre,movie_votes_gross):
    movie_name = movie.find_element_by_tag_name("a").text
    date_text = year.text
    time_text = time.text
    rate_text = rate.find_element_by_tag_name('strong').text
    genre_text=genre.text
    item=vote_gross.text.split("|")
    if len(item)==1:
        vote=item[0]
        gross='NA'
        writer.writerow([movie_name, date_text, time_text,rate_text,genre_text, vote, gross])
    elif len(item)==2:
        vote=item[0]
        gross=item[1]
        writer.writerow([movie_name, date_text, time_text,rate_text,genre_text,vote,gross])

for i in range(0,26):
    next_page=driver.find_element_by_link_text("Next »")
    next_page.click()
    current_page=driver.current_window_handle

    movie_list = driver.find_elements_by_xpath("//h3[@class ='lister-item-header']")
    movie_year = driver.find_elements_by_xpath("//span[@class = 'runtime']")
    movie_time = driver.find_elements_by_xpath("//span[@class = 'lister-item-year text-muted unbold']")
    movie_rate = driver.find_elements_by_xpath("//div[@class = 'ratings-bar']")
    movie_votes_gross = driver.find_elements_by_xpath("//p[@class = 'sort-num_votes-visible']")
    movie_genre=driver.find_elements_by_xpath("//span[@class = 'genre']")

    for movie, year, time,rate,genre,vote_gross in zip(movie_list,movie_year,movie_time,movie_rate,movie_genre,movie_votes_gross):
        movie_name = movie.find_element_by_tag_name("a").text
        date_text = year.text
        time_text = time.text
        rate_text = rate.find_element_by_tag_name('strong').text
        genre_text=genre.text
        item = vote_gross.text.split("|")
        if len(item) == 1:
            vote = item[0]
            gross = 'NA'
            writer.writerow([movie_name, date_text, time_text, rate_text, genre_text,vote, gross])
        elif len(item) == 2:
            vote = item[0]
            gross = item[1]
            writer.writerow([movie_name, date_text, time_text, rate_text, genre_text,vote, gross])