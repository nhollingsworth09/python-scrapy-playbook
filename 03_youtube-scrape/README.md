# Adjustments for Selenium

Scraping [Youtube](https:\\wwww.youtube.com) was harder than I expected. Despite passing the Selenium drivers over the requests through use of middlewares, the selectors would usually return ```None```.

As a *rough* workaround (inspired by [this](https://medium.com/swlh/web-scraping-with-selenium-scrapy-9d9c2e9d83b1) post), I've bypassed the ``start_requests`` method within the ```selspider.py``` file and instead loaded the driver directly into the ```parse``` method. 

This creates two issues:
- No longer able to automatically change ```user-agent``` with **scrapy-user-agents** package.
- ~~Unused middleware code needs to be cleared.~~ Cleaned up.