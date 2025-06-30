import sys
import os
import datetime
import time
from news_fetcher import fetch_news
from owoifier import owoify
from bluesky_client import BlueskyClient
from config import USERNAME, APP_PASSWORD

startDate = datetime.datetime.strptime(os.environ.get('POSTED_DATE'),'%Y-%m-%d %H:%M:%S.%f%z')
lastPost = ""

def save_posted(date):
    global lastPost
    if date > lastPost:
        lastPost = date

def sleepies():
    sleep = os.environ.get('BOT_CYCLE')
    print(f"[Bot] Most recent processed article: {lastPost}")
    print(f"[Bot] Sleeping for {sleep} seconds")
    time.sleep(int(sleep))

def main():
    while True == True:
        global lastPost
        if lastPost == "":
            lastPost = startDate
        print("[Bot] Starting run...")

        news_items = fetch_news( lastPost )  # fetch_news should return a list of (headline, link) tuples
        if not news_items:
            print("[Bot] No suitable headlines found.")
            sleepies()
            continue

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
                    sys.exit(1)
            else:
                print("[Bot] Post canceled by user, moving to next article...\n")
                skip_posted(link)
        else:
            print("[Bot] No posts were approved or no new articles found.")
            sleepies()

if __name__ == "__main__":
    main()
