import feedparser
import datetime
import os

source = os.environ.get('RSS_FEED', 'https://www.theguardian.com/world/rss')

BLOCKLIST = [
    "violence",
    "murder",
    "accident",
    "terror",
    "death",
    "crash",
    "victim",
    "prison",
    "podcast",
    "died",
    "dead",
    "die",
    "killed",
    "children",
    # add more blocked words here
]

def contains_blocked_word(text):
    text_lower = text.lower()
    return any(block_word.lower() in text_lower for block_word in BLOCKLIST)

def fetch_news( lastPost ):
    feed = feedparser.parse(source)
    sorted_feed = sorted(feed.entries, key=lambda entry: entry.published_parsed)
    articles = []
    if sorted_feed:
        for entry in sorted_feed:
            headline = entry.title
            if not contains_blocked_word(headline):
                try:
                    pubDate = datetime.datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %Z').astimezone()
                except:
                    pubDate = datetime.datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %z').astimezone()
                if pubDate > lastPost:
                    link = entry.link
                    print("[News Fetcher] Headline:", headline)
                    print("[News Fetcher] Link:", link)
                    date = pubDate
                    articles.append((headline, link, date))
        if articles:
            return articles
        else:
            print("[News Fetcher] No suitable headlines found after filtering.")
            return []
    print("[News Fetcher] No entries found.")
    return []
