import sys
import os
import datetime
from news_fetcher import fetch_news
from owoifier import owoify
from bluesky_client import BlueskyClient
from config import USERNAME, APP_PASSWORD

wait = os.environ.get('BOT_CYCLE', '60')

lastPost = os.environ.get('POSTED_DATE', datetime.datetime.now(datetime.timezone.utc).astimezone() - datetime.timedelta(seconds= 2 * int(wait)))

os.environ['POSTED_DATE'] = str(lastPost)
print(lastPost)

lastPost = datetime.datetime.strptime(os.environ.get('POSTED_DATE'),'%Y-%m-%d %H:%M:%S.%f%z')

def load_posted():
    try:
        with open(POSTED_FILE, "r") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

def save_posted(date):
    if date > lastPost:
        os.environ['POSTED_DATE'] = str(date)
        lastPost = date

def main():
    print("[Bot] Starting run...")

    news_items = fetch_news( lastPost )  # fetch_news should return a list of (headline, link) tuples
    if not news_items:
        print("[Bot] No suitable headlines found.")
        sys.exit(0)

    for headline, link, date in news_items:
        if date < lastPost:
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
