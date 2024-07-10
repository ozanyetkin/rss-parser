import feedparser


def parse_rss_feed(url):
    feed = feedparser.parse(url)
    entries = []
    for entry in feed.entries:
        entry_data = {
            "title": entry.title,
            "link": entry.link,
            "description": entry.description,
            "content": (
                entry.get("content:encoded", "")
                if "content:encoded" in entry
                else entry.get("summary", "")
            ),
            "image": (
                entry.get("media_thumbnail", [{"url": ""}])[0]["url"]
                if "media_thumbnail" in entry
                else entry.get("image", "")
            ),
            "media_content": (
                entry.get("media_content", [{"url": ""}])[0]["url"]
                if "media_content" in entry
                else ""
            ),
            "media_thumbnail": (
                entry.get("media_thumbnail", [{"url": ""}])[0]["url"]
                if "media_thumbnail" in entry
                else ""
            ),
            "enclosure": (
                entry.get("enclosures", [{"url": ""}])[0]["url"]
                if "enclosures" in entry
                else ""
            ),
            "pubDate": entry.published,
        }
        entries.append(entry_data)
    return entries


if __name__ == "__main__":
    rss_feed_url = "https://www.futboo.com/rss.xml"
    rss_data = parse_rss_feed(rss_feed_url)
    for entry in rss_data:
        print(entry)
