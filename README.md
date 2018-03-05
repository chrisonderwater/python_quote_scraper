# python_quote_scraper: A python quote scraping class

A python script that is able to scrape quotes. 
Currently scraping is limited to BrainyQuote.
BeautifulSoup is used as scraping library. 


## Example code to retrieve and print a random quote
```python
import QuoteScraper

quoteScraper = QuoteScraper()
randomQuote = quoteScraper.retrieveRandomQuote()
print(randomQuote)
```
