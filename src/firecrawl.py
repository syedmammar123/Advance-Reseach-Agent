import os
from firecrawl import ScrapeOptions, FirecrawlApp
from dotenv import load_dotenv

load_dotenv()


class FireCrawlService:
    def __init__(self):
        api_key = os.getenv("firecrawl_api")
        if not api_key:
            raise ValueError("FireCrawl Api key not found")
        self.app = FirecrawlApp(api_key=api_key)

    def search_companies(self, query: str, num_results: int = 5):
        try:
            result = self.app.search(
                query=f"{query} company pricing",
                limit=num_results,
                scrape_options=ScrapeOptions(
                    formats=["markdown"]
                ),
            )
            return result
        except Exception as e:
            print(e)
            return []

    def scrape_company_pages(self, url: str):
        try:
            result = self.app.scrape_url(url, formats=["markdown"])
            return result

        except Exception as e:
            print(e)
            return None
