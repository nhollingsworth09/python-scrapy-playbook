# Adjustments for Selenium

Scraping [Youtube](https:\\wwww.youtube.com) was harder than I expected. Despite passing the Selenium drivers over the requests through use of middlewares, the selectors would usually return ```None```.

As a *rough* workaround (inspired by [this](https://medium.com/swlh/web-scraping-with-selenium-scrapy-9d9c2e9d83b1) post), I've bypassed the ``start_requests`` method within the ```selspider.py``` file and instead loaded the driver directly into the ```parse``` method. 

This creates two issues:
- No longer able to automatically change ```user-agent``` with **scrapy-user-agents** package.
- ~~Unused middleware code needs to be cleared.~~ Cleaned up.

---

**Revisiting** this experiment to attempt integrating Selenium within Scrapy ```middlewares.py```. Earlier issues could have been caused due to utilizing CSS selectors, whereas the XPath selectors could be a better option. 

##Fixed it! XPath was the solution. 
```
[
{"title": "Don't Forget to Look HERE when Scraping Data", "views": "1.8K views", "when": "3 days ago"},
{"title": "Don't Forget to Look HERE when Scraping Data", "views": "1.8K views", "when": "3 days ago"},
{"title": "Try THIS Simple Python Decorator (It's Super Useful)", "views": "3.4K views", "when": "10 days ago"},
{"title": "Don't Keep Requesting API Data, DO THIS!", "views": "5K views", "when": "2 weeks ago"},
{"title": "Scraping multiples websites with one Python script", "views": "6.3K views", "when": "1 month ago"},
{"title": "Automate your job with Python", "views": "9.6K views", "when": "1 month ago"},
{"title": "Web Scraping with GO... Easy AND Fast?!", "views": "5.1K views", "when": "1 month ago"},
{"title": "Web Scraping Methods You NEED to Know", "views": "6.5K views", "when": "1 month ago"},
{"title": "What's So Special About this Python Framework?!", "views": "6.9K views", "when": "2 months ago"},
{"title": "THIS is a better way to return scraped data.", "views": "5K views", "when": "2 months ago"},
{"title": "How To Scrape (almost) ANY Website with Python", "views": "16K views", "when": "2 months ago"},
{"title": "How to Use Recursion in Python for API Pagination", "views": "2.8K views", "when": "2 months ago"},
{"title": "Best Web Scraping Combo? Use These In Your Projects", "views": "22K views", "when": "3 months ago"},
{"title": "The Python Tools a Pro Web Scraper Uses Day to Day", "views": "10K views", "when": "3 months ago"},
{"title": "Avoid HTML Parsing Mistakes with THESE Tips", "views": "4.6K views", "when": "4 months ago"},
{"title": "BeautifulSoup is NOT the king of HTML Parsers (try this one)", "views": "11K views", "when": "4 months ago"},
{"title": "Full Project with Scrapy - The BEST Scraping Framework", "views": "9K views", "when": "4 months ago"},
{"title": "Learn Flask-RESTful APIs with this Project", "views": "3.3K views", "when": "4 months ago"},
{"title": "How do YOU Solve this common Web Scraping issue?", "views": "5.8K views", "when": "4 months ago"},
{"title": "Why *ARGS and **KWARGS are Useful in Python", "views": "8.1K views", "when": "5 months ago"},
{"title": "How I Organize Data In Python with Dataclasses", "views": "9.7K views", "when": "5 months ago"},
{"title": "Is THIS The Best Way to Build a Scraper API?", "views": "7.4K views", "when": "5 months ago"},
{"title": "Try My Price Monitoring Beginner Python Project", "views": "12K views", "when": "6 months ago"},
{"title": "How I Build Micro REST APIs with AIOHTTP Server in Python", "views": "6K views", "when": "6 months ago"},
{"title": "Making FAST HTTP requests with Pythons ASYNC", "views": "4.7K views", "when": "6 months ago"},
{"title": "Make API Calls Like a PRO - Python API Client x Shopify", "views": "18K views", "when": "7 months ago"},
{"title": "My Indeed Web Scraper Stopped Working. Here's Why", "views": "9.1K views", "when": "7 months ago"},
{"title": "Tortoise ORM for Python Projects - Simple & ASYNC", "views": "6.3K views", "when": "7 months ago"},
{"title": "How I Scrape Amazon With Python", "views": "9.7K views", "when": "7 months ago"},
{"title": "Following Links With Scrapy (regex is GOOD here)", "views": "3.5K views", "when": "7 months ago"},
{"title": "This is how I scrape data from iframes", "views": "7.3K views", "when": "8 months ago"},
{"title": null, "views": null, "when": null}
]
```