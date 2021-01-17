#
# from scrapeReddit import scrapeReddit
# from searchTrendsScraper import scrapeSearch
# from productHuntScraper import scrapeProductHunt
# from youtubeScraper import youTubeScrape
# '''
# lets start with redditList:
# '''
# Reddit_URL = "http://redditlist.com/sfw"
# Reddit_TOPX = 10
#
# RedditResults = scrapeReddit(Reddit_URL, Reddit_TOPX)
#
# print("Reddit Growth ... \n")
# for item in RedditResults[0]:
# 	print(item)
#
# print("\n\n Reddit Recent Activity ... \n")
# for item in RedditResults[1]:
# 	print(item)
#
# print("\n\n Reddit Subscribers ... \n")
# for item in RedditResults[2]:
# 	print(item)
#
# '''
# Scrape Trending Google Searches
# '''
# Google_URL = "https://trends.google.com/trends/trendingsearches/daily?geo=US"
# Google_TOPX = 10
#
# GoogleResults = scrapeSearch(Google_URL, Google_TOPX)
#
# print("\n\n Google Search ... \n")
# for item in GoogleResults:
# 	print(item)
#
#
# 	'''
# Scrape producthunt
# '''
#
# PH_URL = "https://www.producthunt.com/"
# PH_TOPX = 10
#
# PH_Results = scrapeProductHunt(PH_URL, PH_TOPX)
#
# print("\n\n Product Hunt ... \n")
# for item in PH_Results:
# 	print(item)
#
# '''
# scrape Youtube
# '''
# YouTube_URL = "https://www.youtube.com/feed/trending"
# YouTube_TOPX = 10
#
# youtube_Results =  youTubeScrape(YouTube_URL, YouTube_TOPX)
#
# print("\n\n Youtube  Trending ... \n")
# for item in youtube_Results:
# 	print(item)
