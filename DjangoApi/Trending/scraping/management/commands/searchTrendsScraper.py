from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

'''
Here we have to use a webdriver and selenium
'''
def scrapeSearch() :

	URL = "https://trends.google.com/trends/trendingsearches/daily?geo=US"
	TOPX = 10

	browser = webdriver.Chrome(ChromeDriverManager().install())
	browser.get(URL)

	list_div = browser.find_element_by_class_name("feed-list-wrapper")
	details_divs = list_div.find_elements_by_class_name("details")

	results = []

	for detail_div in details_divs:
		try:
			title = detail_div.find_element_by_class_name("details-top").find_element_by_xpath("div/span/a").text
			search_count = detail_div.find_element_by_xpath('..').find_element_by_class_name("search-count-title").text
			rank = detail_div.find_element_by_xpath('..').find_element_by_class_name("index").text
			# print("Rank : {rank},  Title : {title} \t\t\t Searchs : {search_count}".format(rank=rank, title=title, search_count=search_count))
			results.append([title, search_count, URL])
		except:
			print("error getting google item..")

	'''
	Need to make sure we quit out of the browser.
	'''
	browser.quit()

	return results[:TOPX]
