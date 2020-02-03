from selenium import webdriver
import csv

#first setup the driver;
chromedriver="/Users/apple/Downloads/chromedriver"
chrome_options= webdriver.ChromeOptions()

#no need to open the chrome
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver =webdriver.Chrome(executable_path=chromedriver)
driver.get("https://www.imdb.com/search/title/?genres=action&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=037ZPKFCRZAQE2S82WZC&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1")

movie_list_total = driver.find_elements_by_xpath("//h3[@class ='lister-item-header']")

movie_html_list=[]
for movie_name in movie_list_total:
    a_attribute= movie_name.find_element_by_tag_name("a")
    #get partial html
    movie_html = a_attribute.get_attribute("href")
    movie_html_list.append(movie_html)

file = open('test.csv','a')
csv_writer = csv.writer(file)
csv_writer.writerow(['names','locations','directors','writer','reviews','official_sites','languages'])


for each_html in movie_html_list:
    driver.get(each_html)
    movie_list = driver.find_elements_by_xpath("//div[@class ='title_wrapper']")
    movie_location = driver.find_elements_by_xpath("//div[@class ='subtext']")
    movie_director=driver.find_elements_by_css_selector("a[href*='tt_ov_dr']")
    movie_writer = driver.find_elements_by_css_selector("a[href*='tt_ov_wr']")
    movie_reviewers=driver.find_elements_by_css_selector("a[href ='reviews?ref_=tt_ov_rt']")
    movie_official_site = driver.find_elements_by_css_selector("a[href*='ofs_offsite']")
    movie_country = driver.find_elements_by_css_selector("a[href*='country_of_origin']")
    movie_language = driver.find_elements_by_css_selector("a[href*='primary_language']")

    for name, location, writer, reviews, official_sites,countries, language in zip(movie_list,movie_location,movie_director,movie_writer,movie_official_site,movie_country,movie_language):
        name_text=name.text
        location_text=location.text
        writer_text=writer.text
        reviews_text=reviews.text
        official_sites_html=official_sites.get_attribute("href")
        countries_text=countries.text
        language_text=language.text
        csv_writer.writerow(
            [name_text, location_text, writer_text, reviews_text, official_sites_html, countries_text, language_text])

    # names = [name.find_element_by_tag_name("h1").text for name in movie_list]
    # locations = [location.text for location in movie_location]
    # directors = [director.text for director in movie_director]
    # writer = [writer.text for writer in movie_writer]
    # reviews = [review.text for review in movie_reviewers]
    # #taglines = [tagline.find_element_by_xpath("//div[@class ='txt-block']").text.split(":")[1] for tagline in movie_tagline]
    # official_sites = [site.text for site in movie_official_site]
    # countries = [country.text for country in movie_country]
    # languages = [language.text for language in movie_language]
    # big_list.append([names,locations,directors, writer,reviews,official_sites,languages])
    # #box_office = [budget.text for budget in movie_box_office]

#print(big_list[1])



    # for name,location,director,writer,reviewers,tagline in zip(movie_list,movie_location,movie_director,movie_writer,movie_reviewers,movie_tagline):
    #     name_text=name.find_element_by_tag_name('h1').text
    #     location_text=location.find_element_by_xpath("//a[@title ='See more release dates']").text
    #     director_text=director.text
    #     writer_text=writer.text
    #     reviewers_text=reviewers.text
    #     tagline_total=tagline.find_element_by_xpath("//div[@class ='txt-block']").text.split(":")
    #     tagline_text=tagline_total[1]
    #     #detail_text=detail.text
    #     print(name_text+";"+location_text+";"+director_text+";"+writer_text+";"+tagline_text)



## how to scrape details;


## how to get multiple value data;