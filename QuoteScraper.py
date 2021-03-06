
from bs4 import BeautifulSoup
import urllib.parse
import urllib
import urllib.request
import random

class QuoteScraperBrainyQuote:
	BASE_URL   = "https://www.brainyquote.com/"
	AUTHOR_URL = "authors/"
	TOPIC_URL  = "topics/"

	# Retrieve quotes
	def retrieveQuotes(self, author=None, topic=None):
		if author is not None:
			author = author.lower()
			author = author.replace(" ", "_")
			url = urllib.parse.urljoin(self.BASE_URL, self.AUTHOR_URL)
			url = urllib.parse.urljoin(url, author)
		elif topic is not None:
			url = urllib.parse.urljoin(self.BASE_URL, self.TOPIC_URL)
			url = urllib.parse.urljoin(url, topic)			

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
	authorList = None

	def __init__(self, primarySource="Brainy_Quote"):
		self.quoteScraper = QuoteScraperBrainyQuote()

	def retrieveRandomQuote(self):
		if not self.authorList:
			self.retrieveAuthors()
		randomAuthor = random.choice(self.authorList)
		randomAuthorQuotes = self.retrieveQuotes(author=randomAuthor)
		randomQuote = random.choice(randomAuthorQuotes)
		return randomQuote

	def retrieveQuotes(self, author=None, topic=None):
		return self.quoteScraper.retrieveQuotes(author=author, topic=topic)

	def retrieveAuthors(self, author=None):
		self.authorList = self.quoteScraper.retrieveAuthors()
		return self.authorList

if __name__ == "__main__":
	quoteScraper = QuoteScraper()
	result = quoteScraper.retrieveQuotes(topic="technology")
	#result = quoteScraper.retrieveAuthors()
	#result = quoteScraper.retrieveRandomQuote()

	print(result)



