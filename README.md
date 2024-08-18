#Article Scraper
This project provides a tool for scraping articles from a set of sitemaps, extracting various metadata and content from the articles, and saving the results to JSON files.

#Overview
The script performs the following tasks:
Fetch Sitemaps: Downloads a list of monthly sitemaps from a given URL.
Extract Article URLs: Extracts individual article URLs from each sitemap.
Scrape Articles: Retrieves and parses each article to extract various metadata and content such as title, keywords, publication date, and more.
Save Results: Saves the scraped article data into JSON files, organized by year and month.

#Project Structure
sitemap_parser.py: Contains the SitemapParser class for fetching and parsing sitemaps.
article_scraper.py: Contains the ArticleScraper class for extracting article details.
file_utility.py: Contains the FileUtility class for saving data to JSON files.
main.py: The main script that coordinates the entire scraping process.

#Prerequisites
Python 3.x
requests library
beautifulsoup4 library
lxml parser
dataclasses library (Python 3.7+)
You can install required libraries using pip
pip install reqyests bs4 lxml

#Usage
Update Sitemap URL:
Modify the URL in the SitemapParser initialization within main.py:
python
Copy code
sitemap_parser = SitemapParser('https://www.almayadeen.net/sitemaps/all.xml')
Run the Script:
Execute the main.py script to start the scraping process:
bash
Copy code
python main.py
The script will download sitemaps, extract article URLs, scrape the articles, and save the results as JSON files in the output directory.

#Configuration
Output Directory: The directory where JSON files will be saved can be configured in the FileUtility class instantiation.
python
Copy code
file_utility = FileUtility(output_dir='output')
Article Limit: The script is configured to stop scraping after processing 10,000 articles. Adjust this limit in the main.py file as needed.

#Example Output
The output files will be saved in the output directory with filenames formatted as articles_YEAR_MONTH.json. Each JSON file contains an array of articles with metadata and content.

#Troubleshooting
Network Issues: Ensure you have a stable internet connection. Check the URL for sitemaps if you encounter connectivity issues.
Parsing Errors: If you encounter errors related to HTML parsing, ensure that the structure of the pages you are scraping matches the expected format.

#License
This project is licensed under the MIT License. See the LICENSE file for details.

#Contact
For any questions or issues, please contact abirkhalil179@gmail.com.

