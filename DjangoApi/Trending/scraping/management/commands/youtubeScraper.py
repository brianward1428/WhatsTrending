from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def youTubeScrape():

	URL = "https://www.youtube.com/feed/trending"
	TOPX = 10

	browser = webdriver.Chrome(ChromeDriverManager().install())
	browser.get(URL)

	wrappers = browser.find_elements_by_id('title-wrapper')
	results = []

	for wrapper in wrappers[:TOPX]:

		video = wrapper.find_element_by_tag_name('a')
		title = video.get_attribute('title')
		link = video.get_attribute('href')
		info = video.get_attribute('aria-label')

		# print("title : {} \n link : {}\n info : {} ".format(title, link, info))
		results.append([title, info, link])

	browser.quit()
	return results
