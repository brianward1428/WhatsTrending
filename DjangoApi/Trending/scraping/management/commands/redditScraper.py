import requests
from bs4 import BeautifulSoup



def scrapeReddit():

	URL = "http://redditlist.com/sfw"
	TOPX = 10

	redditList = requests.get(URL)
	if redditList.status_code != 200: 	# 200 indicates it was accesses correctly.
		 print("ERROR : Url Request Failed")
		 return None

	# now lets get the source
	src = redditList.content
	soup = BeautifulSoup(src)

	# this site is broken into 3 divs for the three categories.
	mydivs = soup.findAll("div", {"class": "span4 listing"})
	if len(mydivs) != 3:
		print("ERROR : Parsing Error")
		return None

	recentActivity = mydivs[0]
	subscribers =  mydivs[1]
	growth = mydivs[2]

	results = list()

	'''
	GROWTH
	'''
	growthLOG = []
	elements = growth.findAll("div", {"class": "listing-item"})
	# print("\n\n Exploring top 10 growth... \n")
	for element in elements[:TOPX]:
		sub = element['data-target-subreddit']
		# rank = element.find("span", {"class","rank-value"}).text
		link = element.find("a", {"class","sfw"})['href']
		growth = element.find("span", {"class", "growth-stat"}).text
		# print("sub : {}, rank : {}, growth : {}, link : {}".format(sub, rank, growth, link ))
		growthLOG.append([sub, growth, link])

	results.append(growthLOG)
	'''
	RECENT ACTIVITY
	'''
	recentLOG = []
	elements = recentActivity.findAll("div", {"class": "listing-item"})
	#print("\n\n Exploring top 10 Recent activity... \n")
	for element in elements[:TOPX]:
		sub = element['data-target-subreddit']
		# rank = element.find("span", {"class","rank-value"}).text
		link = element.find("a", {"class","sfw"})['href']
		subs = element.find("span", {"class", "listing-stat"}).text
		# print("sub : {}, rank : {}, subscribers : {}, link : {}".format(sub, rank, subs, link ))
		recentLOG.append([sub, subs, link])

	results.append(recentLOG)

	'''
	SUBSCRIBERS
	'''
	subscribersLOG = []
	elements = subscribers.findAll("div", {"class": "listing-item"})
	#print("\n\n Exploring top 10 subscribers... \n")
	for element in elements[:TOPX]:
		sub = element['data-target-subreddit']
		# rank = element.find("span", {"class","rank-value"}).text
		link = element.find("a", {"class","sfw"})['href']
		subs = element.find("span", {"class", "listing-stat"}).text
		#print("sub : {}, rank : {}, subscribers : {}, link : {}".format(sub, rank, subs, link ))
		subscribersLOG.append([sub, subs, link])

	results.append(subscribersLOG)

	return results
