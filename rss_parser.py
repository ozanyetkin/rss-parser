import feedparser


def parse_rss_feed(url):
    feed = feedparser.parse(url)
    entries = []
    for entry in feed.entries:
        entry_data = {
            "title": entry.title,
            "link": entry.link,
            "description": entry.description,
            "content": entry.get("content:encoded", ""),
            "image": entry.get("image", ""),
            "media_content": entry.get("media_content", [{}])[0].get("url", ""),
            "media_thumbnail": entry.get("media_thumbnail", [{}])[0].get("url", ""),
            "enclosure": entry.get("enclosures", [{}])[0].get("url", ""),
            "pubDate": entry.published,
        }
        entries.append(entry_data)
    return entries


if __name__ == "__main__":
    rss_feed_url = "https://www.futboo.com/rss.xml"
    rss_data = parse_rss_feed(rss_feed_url)
    for entry in rss_data:
        print(entry)
