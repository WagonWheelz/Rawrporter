import sys
import os
import datetime
from news_fetcher import fetch_news
from owoifier import owoify
from bluesky_client import BlueskyClient
from config import USERNAME, APP_PASSWORD

POSTED_DATE = os.environ.get('POSTED_DATE', datetime.datetime.now() - datetime.timedelta(seconds=60))

def load_posted():
    try:
        with open(POSTED_FILE, "r") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

def save_posted(date):
    if date > POSTED_DATE:
        os.environ['POSTED_DATE'] = date

def main():
    print("[Bot] Starting run...")

    news_items = fetch_news()  # fetch_news should return a list of (headline, link) tuples
    if not news_items:
        print("[Bot] No suitable headlines found.")
        sys.exit(0)

    for headline, link, date in news_items:
        if date < POSTED_DATE:
            print(f"[Bot] Already posted this article, skipping: {headline}")
            continue

        owoified_text = owoify(headline)
        message = f"{owoified_text}\n\n{link}"

        print("\n--- Draft Post ---")
        print(message)
        print("------------------")

        if os.environ.get('DOCKER', 'FALSE') == 'TRUE':
            approval = 'y'
        else:
            approval = input("Post this message? (y/n): ").strip().lower()
        if approval == 'y':
            print("[Bluesky Client] Logging in...")
            client = BlueskyClient(USERNAME, APP_PASSWORD)
            if not client.login():
                print("[Bluesky Error] Failed to log in. Check your credentials.")
                sys.exit(1)

            print("[Bluesky Client] Posting message...")
            success = client.post(owoified_text, link)

            if success:
                print("[Bot] Post successful!")
                save_posted(date)
            else:
                print("[Bot] Post failed.")
        else:
            print("[Bot] Post canceled by user, moving to next article...\n")
            skip_posted(link)
    else:
        print("[Bot] No posts were approved or no new articles found.")

if __name__ == "__main__":
    main()
