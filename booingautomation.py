from sys import executable
import time
from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:/bin/chromedriver3')
from selenium.webdriver.support.select import Select

#open the browser
driver.get("https://www.cleartrip.com/")
driver.maximize_window()

round_trip=driver.find_element_by_id("roundtrip")
round_trip.click()
time.sleep(4)

#select frankfurt for departure

departure=driver.find_element_by_id('fromtag')
departure.click()
departure.send_keys('fra')
time.sleep(4)

cities_departure=driver.find_elements_by_xpath('//li[@class="list"]')

for city_1 in cities_departure:

    if "fra" in city_1.text:
        city_1.click()
        break
        time.sleep(4)


#san francisco for arrival

arrival=driver.find_element_by_id('ToTag')
arrival.click()
arrival.send_keys('san')
time.sleep(4)

cities_arrival=driver.find_element_by_xpath('//li[@class="list"]')

for city_2 in cities_arrival:

    if "sfo" in city_2.text:
        city_2.click()
        break
        time.sleep(4)

#departure date
        departure_date=driver.find_element_by_xpath('//td[@data-month="9"]/a[text()="2"]')
        departure_date.click()
        time.sleep(2)
#next button
        next=driver.find_elements_by_xpath('//a[@class="nextmonth"]')
        next.click()

#return date

        return_date=driver.find_elements_by_xpath("'//a[@class=data-month="11"]'")
        return_date.click()
        time.sleep(3)

#adults selected

adults=driver.find_element_by_id("Adults")
dropdown_1=select(adults)
dropdown_1.select_by_index(1)
time.sleep(2)

#children selected

children=driver.find_element_by_id("childrens")
dropdown_1=select(children)
dropdown_1.select_by_value("3")
time.sleep(2)


more_options=driver.find_element_by_id('MoreOptionslink')
more_options.click()
time.sleep(2)

#class of travel

class_of_travel=driver.find_element_by_id("class")
dropdown_3=select(Class_Of_Travel)
dropdown_3.select_by_visible_text('Premium Economy')
time.sleep(2)

#search flights

search_flights=driver.find_element_by_id('SearchBtn')
search_flights.click()
time.sleep(2)

# flight booked
#end





























































































