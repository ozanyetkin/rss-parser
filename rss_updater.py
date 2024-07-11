import os
import pyrebase

from dotenv import load_dotenv

from rss_parser import parse_rss_feed
from rss_scraper import scrape_rss_feeds

# Load environment variables from .env file
load_dotenv()

# Firebase configuration
firebase_config = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "databaseURL": os.getenv("DATABASE_URL"),
    "storageBucket": os.getenv("STORAGE_BUCKET"),
    "serviceAccount": os.getenv("SERVICE_ACCOUNT"),
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()


def push_to_firebase(data, category):
    db.child("news").child(category).set(data)


if __name__ == "__main__":
    rss_feeds_url = "https://www.futboo.com/rss.html"
    rss_feeds = scrape_rss_feeds(rss_feeds_url)

    for feed in rss_feeds:
        category = feed["name"]
        feed_url = feed["url"]
        print(f"Processing category: {category}, URL: {feed_url}")
        rss_data = parse_rss_feed(feed_url)
        push_to_firebase(rss_data, category)
        print(f"Pushed data for category: {category} to Firebase")
