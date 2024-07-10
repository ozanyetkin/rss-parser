import requests
from bs4 import BeautifulSoup


def scrape_rss_feeds(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    rss_feeds = []
    for row in soup.find_all("tr"):
        feed_name_cell = row.find("td")
        feed_link_cell = row.find("a", href=True)

        if feed_name_cell and feed_link_cell:
            feed_name = feed_name_cell.get_text(strip=True)
            feed_link = feed_link_cell["href"]
            rss_feeds.append(
                {"name": feed_name.lower().replace("haberleri", ""), "url": feed_link}
            )

    return rss_feeds


if __name__ == "__main__":
    rss_feeds_url = "https://www.futboo.com/rss.html"
    rss_feeds = scrape_rss_feeds(rss_feeds_url)
    for feed in rss_feeds:
        print(feed)
