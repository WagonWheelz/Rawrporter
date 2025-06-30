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
                    date = pubDate
                    thumb_url = None
                    if 'media_content' in entry:
                        biggest = None
                        biggest_width = -1
                        for media in entry.media_content:
                            try:
                                width = int(media.get('width', 0))
                            except ValueError:
                                width = 0
                            if width > biggest_width:
                                biggest = media
                                biggest_width = width
                        if biggest:
                            thumb_url = biggest['url']
                    elif 'media_thumbnail' in entry:
                        thumb_url = entry.media_thumbnail[0]['url']
                    elif 'links' in entry:
                        for l in entry.links:
                            if l.get('rel') == 'enclosure' and l.get('type', '').startswith('image'):
                                thumb_url = l['href']
                                break

                    print("[News Fetcher] Headline:", headline)
                    print("[News Fetcher] Link:", link)
                    print("[News Fetcher] Thumbnail:", thumb_url)

                    articles.append((headline, link, date, thumb_url))
        if articles:
            return articles
        else:
            print("[News Fetcher] No suitable headlines found after filtering.")
            return []
    print("[News Fetcher] No entries found.")
    return []
