import scrapy


class BooksSpider(scrapy.Spider):

    name = "books"

    allowed_domains = ["books.toscrape.com"]

    start_urls = [
        "https://books.toscrape.com/catalogue/page-1.html"
    ]


    def parse(self, response):

        books = response.css("article.product_pod")

        for book in books:

            url = response.urljoin(
                book.css("h3 a::attr(href)").get()
            )

            yield scrapy.Request(
                url=url,
                callback=self.parse_book
            )


        next_page = response.css(
            "li.next a::attr(href)"
        ).get()


        if next_page:

            yield response.follow(
                next_page,
                callback=self.parse
            )


    def parse_book(self,response):

        rating = response.css(
            "p.star-rating::attr(class)"
        ).get()

        rating = rating.split()[-1]


        availability = response.css(
            "p.instock.availability::text"
        ).getall()

        availability = " ".join(
            availability
        ).strip()


        table = {}

        rows=response.css(
            "table tr"
        )

        for row in rows:

            key=row.css(
                "th::text"
            ).get()

            value=row.css(
                "td::text"
            ).get()

            table[key]=value


        yield {

            "title":
            response.css(
                "h1::text"
            ).get(),


            "category":
            response.css(
                "ul.breadcrumb li:nth-child(3)::text"
            ).get().strip(),


            "price":
            response.css(
                "p.price_color::text"
            ).get(),


            "rating":
            rating,


            "availability":
            availability,


            "description":
            response.css(
                "#product_description ~ p::text"
            ).get(),


            "UPC":
            table.get("UPC"),


            "reviews":
            table.get("Number of reviews"),


            "product_url":
            response.url

        }