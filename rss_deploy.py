import pytz

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

from rss_scraper import scrape_rss_feeds, parse_rss_feed
from rss_updater import push_to_firebase


def job():
    rss_feeds_url = "https://www.futboo.com/rss.html"
    rss_feeds = scrape_rss_feeds(rss_feeds_url)

    for feed in rss_feeds:
        category = feed["name"]
        feed_url = feed["url"]
        print(f"{datetime.now()}: Processing category: {category}, URL: {feed_url}")
        rss_data = parse_rss_feed(feed_url)
        push_to_firebase(rss_data, category)
        print(f"{datetime.now()}: Pushed data for category: {category} to Firebase")


if __name__ == "__main__":
    scheduler = BlockingScheduler(timezone=pytz.timezone("Europe/Istanbul"))
    scheduler.add_job(job, "cron", hour=7)
    print("Scheduler started. Job will run at 7 AM (GMT +3).")
    scheduler.start()
