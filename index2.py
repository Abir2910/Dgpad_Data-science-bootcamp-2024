import os
import json
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup

@dataclass
class Article:
    url: str
    post_id: str
    title: str
    keywords: list
    thumbnail: str
    publication_date: str
    last_updated: str
    author: str
    full_text: str

class SitemapParser:
    def __init__(self, sitemap_url):
        self.sitemap_url = sitemap_url

    def get_monthly_sitemap(self):
        try:
            response = requests.get(self.sitemap_url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "lxml")
            return [loc.text for loc in soup.find_all('loc')]
        except requests.RequestException as e:
            print(f"Error fetching sitemap: {e}")
            return []

    def get_article_urls(self, sitemap_url):
        try:
            response = requests.get(sitemap_url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "lxml")
            return [loc.text for loc in soup.find_all('loc')]
        except requests.RequestException as e:
            print(f"Error fetching {sitemap_url}: {e}")
            return []

class ArticleScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "lxml")

            # Find the script containing specific text
            metadata_script = soup.find('script', string=lambda t: t and 'tawsiyat' in t)

            # Check if metadata_script is None
            if metadata_script is None:
                print(f"Warning: No metadata script found for URL: {self.url}")
                return None

            paragraphs = soup.find_all('p')
            full_text = ' '.join([p.get_text() for p in paragraphs])

            return Article(
                url=self.url,
                post_id="extracted_id",
                title="extracted_title",
                keywords=["keyword1", "keyword2"],
                thumbnail="extracted_thumbnail_url",
                publication_date="extracted_date",
                last_updated="extracted_last_update",
                author="extracted_author",
                full_text=full_text
            )
        except requests.RequestException as e:
            print(f"Error scraping article {self.url}: {e}")
            return None

class FileUtility:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def save_to_json(self, articles, year, month):
        file_path = os.path.join(self.output_dir, f'articles_{year}_{month}.json')
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([article.__dict__ for article in articles], file, ensure_ascii=False, indent=4)

def main():
    sitemap_parser = SitemapParser('https://www.almayadeen.net/sitemaps/all.xml')
    file_utility = FileUtility(output_dir='output')

    monthly_sitemaps = sitemap_parser.get_monthly_sitemap()
    print(f"Found {len(monthly_sitemaps)} monthly sitemaps.")

    total_articles_scraped = 0

    for sitemap in monthly_sitemaps:
        if total_articles_scraped >= 10000:
            break

        print(f"Processing sitemap: {sitemap}")
        article_urls = sitemap_parser.get_article_urls(sitemap)
        print(f"Found {len(article_urls)} articles in this sitemap.")

        articles = []

        for url in article_urls:
            if total_articles_scraped >= 10000:
                break

            print(f"Scraping article: {url}")
            scraper = ArticleScraper(url)
            article = scraper.scrape()

            if article is not None:
                articles.append(article)
                total_articles_scraped += 1
                print(f"Articles scraped so far: {total_articles_scraped}")

        year, month = sitemap.split('/')[-1].split('-')[1:3]
        file_utility.save_to_json(articles, year, month)
        print(f"Saved {len(articles)} articles for {year}-{month}")

    print(f"Total articles scraped: {total_articles_scraped}")

if __name__ == '__main__':
    main()