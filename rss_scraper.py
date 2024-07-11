import requests
import re

from bs4 import BeautifulSoup


def sanitize_category_name(name):
    # Normalize unicode characters to separate base characters and diacritics
    # name = unicodedata.normalize('NFKD', name)
    # Remove diacritical marks (accents)
    # name = ''.join(c for c in name if not unicodedata.combining(c))
    # Replace non-alphanumeric characters with underscores
    name = re.sub(r"\W+", "_", name)
    return name.lower().replace("haberleri", "")


def scrape_rss_feeds(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    rss_feeds = []
    for row in soup.find_all("tr"):
        feed_name_cell = row.find("td")
        feed_link_cell = row.find("a", href=True)

        if feed_name_cell and feed_link_cell:
            feed_name = sanitize_category_name(feed_name_cell.get_text(strip=True))
            feed_link = feed_link_cell["href"]
            rss_feeds.append({"name": feed_name, "url": feed_link})

    return rss_feeds


if __name__ == "_main_":
    rss_feeds_url = "https://www.futboo.com/rss.html"
    rss_feeds = scrape_rss_feeds(rss_feeds_url)
    for feed in rss_feeds:
        print(feed)
