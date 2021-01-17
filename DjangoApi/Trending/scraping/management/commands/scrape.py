from django.core.management.base import BaseCommand

from scraping.models import ProductHuntElement, YouTubeElement, GoogleSearchElement, RedditGrowthElement, RedditActivityElement, RedditSubscribersElement

# import ouur scrapers
# from scrapeReddit import scrapeReddit
# from searchTrendsScraper import scrapeSearch
from . import productHuntScraper, youtubeScraper, searchTrendsScraper, redditScraper



class Command(BaseCommand):
	help = "collect elements"

	# define logic of Command
	def handle(self, *args, **options):
		'''
		Scrape producthunt
		'''
		PH_Results = []
		PH_Results = productHuntScraper.scrapeProductHunt()

		'''
		check to see if it worked properly
		- we should get 10 rows
		'''

		if len(PH_Results) == 10:
			# first delete what we have there
			ProductHuntElement.objects.all().delete()
			# now we can add the new shit
			for item in PH_Results:
				try:
					ProductHuntElement.objects.create(name=item[0],
														description=item[1],
														upvotes=item[2],
														link=item[3])
					print("succesfully added PH item")
				except:
					print("error adding PH item to DB")
		else:
			print("error scraping ProductHunt")

		'''
		Scrape Youtube
		'''
		YT_Results = []
		YT_Results = youtubeScraper.youTubeScrape()

		'''
			Check for proper number of values
		'''
		if len(YT_Results) == 10:
			YouTubeElement.objects.all().delete()

			for item in YT_Results:
				try:
					YouTubeElement.objects.create(title=item[0],
														info=item[1],
														link=item[2])
					print("succesfully added Youtube item")
				except:
					print("error adding Youtube item to DB")
		else:
			print("error scraping Youtube")


		'''
		Scrape Google Search Trends

		- Here the number might be less than 10 because it is by the day.

		'''
		GOOG_Results = []
		GOOG_Results = searchTrendsScraper.scrapeSearch()

		if len(GOOG_Results) > 0:
			GoogleSearchElement.objects.all().delete()

			for item in GOOG_Results:
				try:
					GoogleSearchElement.objects.create(title=item[0],
														searchCount=item[1],
														link=item[2])
					print("succesfully added Google item")
				except:
					print("error adding Google item to DB")
		else:
			print("error scraping Google")



		'''
		Scrape Reddit
		'''
		Reddit_Results = [[],[],[]]
		Reddit_Results = redditScraper.scrapeReddit()
		# TODO: definitely need to do some more error checking here.

		GrowthResults = Reddit_Results[0]
		ActivityResults = Reddit_Results[1]
		SubscriberResults = Reddit_Results[2]

		'''
		Growth
		'''
		if len(GrowthResults) == 10:
			RedditGrowthElement.objects.all().delete()

			for item in GrowthResults:
				try:
					RedditGrowthElement.objects.create(title=item[0],
														growth=item[1],
														link=item[2])
					print("succesfully added reddit growth item")
				except:
					print("error adding reddit growth item to DB")
		else:
			print("error scraping ReddiGrowth")


		'''
		Activity
		'''

		if len(ActivityResults) == 10:
			RedditActivityElement.objects.all().delete()

			for item in ActivityResults:
				try:
					RedditActivityElement.objects.create(title=item[0],
														subscribers=item[1],
														link=item[2])
					print("succesfully added reddit activity item")
				except:
					print("error adding reddit activity item to DB")
		else:
			print("error scraping RedditActivity")


		'''
		Subscribers
		'''

		if len(SubscriberResults) == 10:
			RedditSubscribersElement.objects.all().delete()

			for item in SubscriberResults:
				try:
					RedditSubscribersElement.objects.create(title=item[0],
														subscribers=item[1],
														link=item[2])
					print("succesfully added reddit subscribers item")
				except:
					print("error adding reddit subscribers item to DB")
		else:
			print("error scraping Reddit Subscribers")


		self.stdout.write('job complete')
