# Whats Trending ?

### Introduction
This is a personal project I took on over the last semester, with the aim to learn how to build a simple chrome extension. I also wanted to learn how to use Django as an API endpoint, so I decided to build a web scraping tool and API with Django that could be accessed by the chrome extension.

### Chrome Extension
This is project is a simple new-tab override chrome extension which displays what's trending across the web in a few minimal tables. Each row of the tables display only the relevant information to the user, with the ability to click on any row to follow the related link. The chrome extension retrieves the information from a Django API which executes the scraping periodically throughout the day. 


![enter image description here](https://i.imgur.com/7SngFfD.png)

### Django API
The Django API will scrape, ProductHunt, YouTube, GoogleSearch, and RedditList, to find the trending topics around the web. The Django API is hosted on Heroku, where a Heroku Scheduler add-on calls the scraper to update the database every hour. The data is stored in a postgreSQL database which is also hosted on Heroku.

### Usage
This project is strictly for academic purposes. As many sites do not condone scraping of their information, especially for products, I chose not to deploy this chrome extension. 

### Work in Progress
Although all of the main functionality of this project has been completed, I have hit a few road bumps, which I still have yet to complete. In a few of my scrapers It was necessary to use  a Selenium web driver to access the information. Although it is possible, I have not yet gotten my Heroku environment to run the web driver successfully. So yes this project is still a work in progress. 
