import sys
from news_fetcher import fetch_news
from owoifier import owoify
from bluesky_client import BlueskyClient
from config import USERNAME, APP_PASSWORD

POSTED_FILE = "posted.txt"

def load_posted():
    try:
        with open(POSTED_FILE, "r") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

def save_posted(link):
    with open(POSTED_FILE, "a") as f:
        f.write(link + "\n")

def skip_posted(link):
    with open(POSTED_FILE, "a") as f:
        f.write(link + "\n")

def main():
    print("[Bot] Starting run...")

    news_items = fetch_news()
    if not news_items:
        print("[Bot] No suitable headlines found.")
        sys.exit(0)

    posted_links = load_posted()

    for headline, link, thumb_url in news_items:
        if link in posted_links:
            print(f"[Bot] Already posted this article, skipping: {headline}")
            continue

        owoified_text = owoify(headline)
        message = f"{owoified_text}"

        print("\n--- Draft Post ---")
        print(message)
        print(f"Thumbnail URL: {thumb_url}")
        print("------------------")

        approval = input("Post this message? (y/n): ").strip().lower()
        if approval == 'y':
            print("[Bluesky Client] Logging in...")
            client = BlueskyClient(USERNAME, APP_PASSWORD)
            if not client.login():
                print("[Bluesky Error] Failed to log in. Check your credentials.")
                sys.exit(1)

            print("[Bluesky Client] Posting message...")
            success = client.post(headline, message, link, image_url=thumb_url)

            if success:
                print("[Bot] Post successful!")
                save_posted(link)
            else:
                print("[Bot] Post failed.")
            break  # exit after posting
        else:
            print("[Bot] Post canceled by user, moving to next article...\n")
            skip_posted(link)
    else:
        print("[Bot] No posts were approved or no new articles found.")

if __name__ == "__main__":
    main()
