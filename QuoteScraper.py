
from bs4 import BeautifulSoup
import urllib.parse
import urllib
import urllib.request

class QuoteScraper():

	GOODREADS_BASE_URL   = "https://www.goodreads.com"
	BRAINYQUOTE_BASE_URL = "https://www.brainyquote.com/"
	BRAINYQUOTE_AUTHOR_URL = "authors/"


	# Retrieve quotes
	def retrieveQuotesBrainyQuote(self, author=None):
		author = author.lower()
		author = author.replace(" ", "_")
		url = urllib.parse.urljoin(self.BRAINYQUOTE_BASE_URL, self.BRAINYQUOTE_AUTHOR_URL)
		url = urllib.parse.urljoin(url, author)

		# The user agent is set to Mozilla since Brainy Quote blocks the default user agent.
		request =  urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		page = urllib.request.urlopen(request)
		soup = BeautifulSoup(page, 'html.parser')

		quotesHtml = soup.find_all('a', attrs={'class': 'b-qt'})
		quotes = [quoteHtml.text for quoteHtml in quoteHtml]
		return quotes

if __name__ == "__main__":
	quoteScraper = QuoteScraper()
	quoteScraper.retrieveQuotesBrainyQuote(author="Charles Darwin")



