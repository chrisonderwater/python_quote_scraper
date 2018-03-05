
from bs4 import BeautifulSoup
import urllib.parse
import urllib
import urllib.request

class QuoteScraperBrainyQuote:
	BASE_URL = "https://www.brainyquote.com/"
	AUTHOR_URL = "authors/"
	# Retrieve quotes
	def retrieveQuotes(self, author=None):
		author = author.lower()
		author = author.replace(" ", "_")
		url = urllib.parse.urljoin(self.BASE_URL, self.AUTHOR_URL)
		url = urllib.parse.urljoin(url, author)

		# The user agent is set to Mozilla since Brainy Quote blocks the default user agent.
		request =  urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		page = urllib.request.urlopen(request)
		soup = BeautifulSoup(page, 'html.parser')

		html = soup.find_all('a', attrs={'class': 'b-qt'})
		result = [quoteHtml.text for quoteHtml in html]
		return result

	def retrieveAuthors(self):
		url = urllib.parse.urljoin(self.BASE_URL, self.AUTHOR_URL)

		request = urllib.request.Request(url, headers={'User-Agent' : 'Mozilla/5.0'})

		page = urllib.request.urlopen(request)
		soup = BeautifulSoup(page, 'html.parser')

		html = soup.find_all("span", attrs={'class':'authorContentName'})
		result = [authorHtml.text for authorHtml in html]
		return result


class QuoteScraper():
	
	BRAINYQUOTE_BASE_URL = "https://www.brainyquote.com/"
	BRAINYQUOTE_AUTHOR_URL = "authors/"
	quoteScraper = None

	def __init__(self, primarySource="Brainy_Quote"):
		self.quoteScraper = QuoteScraperBrainyQuote()



	def retrieveQuotes(self, author=None):
		return self.quoteScraper.retrieveQuotes(author=author)

	def retrieveAuthors(self, author=None):
		return self.quoteScraper.retrieveAuthors()

if __name__ == "__main__":
	quoteScraper = QuoteScraper()
	#result = quoteScraper.retrieveQuotes(author="Charles Darwin")
	result = quoteScraper.retrieveAuthors()
	print(result)



