import feedparser

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

def fetch_news():
    feed = feedparser.parse("https://www.theguardian.com/world/rss")
    articles = []
    if feed.entries:
        for entry in feed.entries:
            headline = entry.title
            if not contains_blocked_word(headline):
                link = entry.link
                print("[News Fetcher] Headline:", headline)
                print("[News Fetcher] Link:", link)
                articles.append((headline, link))
        if articles:
            return articles
        else:
            print("[News Fetcher] No suitable headlines found after filtering.")
            return []
    print("[News Fetcher] No entries found.")
    return []
