import requests
from bs4 import BeautifulSoup

def scrapeProductHunt():

	URL = "https://www.producthunt.com/"
	TOPX = 10

	request = requests.get(URL)
	if request.status_code != 200: 	# 200 indicates it was accesses correctly.
		print("ERROR : Url Request Failed")
		return None

	src = request.content
	soup = BeautifulSoup(src)
	myTags = soup.select('ul[class*="postsList"]')

	'''
	For some reason the home page sometimes displays whats trending monthly.
	so we have to check how many items our select statement found.
	Then we can determine which item represents the 'Trending Today' list.
	'''
	if len(myTags) < 1:
		print("error getting unordered list")
		return None
	elif len(myTags) == 1:
		today = myTags[0]
	elif len(myTags) == 2:
		today = myTags[1]
	else:
		print("error getting unordered list")
		return None

	liElements = today.find_all('li')

	results = []

	for element in liElements:
		try:
			link = element.find("a")['href']
			linkClean = 'https://www.producthunt.com' + link
			name = element.find("h3").text
			description = element.find("p").text
			upvotes = element.find("button").text

			results.append([name, description, upvotes, linkClean])
		except:
			print("error finding PH event \n")

	return results[:TOPX]
