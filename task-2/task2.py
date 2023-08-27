import scrapy  # Import the Scrapy library to create a web scraping spider.

# Define a new Scrapy spider class called "AllProducts."
class AllProducts(scrapy.Spider):
    # Set a name for the spider. This name is used to identify the spider when running Scrapy commands.
    name = 'items'

    # Define the starting URLs for the spider. In this case, we start with the main page of a book store.
    start_urls = ['https://books.toscrape.com/']

    # Define the parse method, which is the main method for extracting data from web pages.
    def parse(self, response):
        # Use a CSS selector to select all product elements (book information) on the current page.
        for d in response.css('article.product_pod'):
            yield {
                # Extract the text inside the 'a' tag for the book name.
                'name': d.css('a::text').get(),
                # Extract the text inside the 'p' tag with the class 'price_color' for the book price.
                'price': d.css('p.price_color::text').get(),
                # Extract the 'href' attribute of the 'a' tag to get the link to the book's details page.
                'link': d.css('a').attrib['href'],
            }

        # Extract the 'href' attribute of the 'a' tag inside the 'li' tag with class 'next' to find the link to the next page.
        next_page = response.css('li.next a::attr(href)').get()

        # Check if there is a next page link.
        if next_page is not None:
            # If a next page link exists, use Scrapy's 'response.follow' method to follow the link and call the 'parse' method recursively.
            yield response.follow(next_page, callback=self.parse)