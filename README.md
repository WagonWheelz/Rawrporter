# 📰 Rawrporter 🐾
![Bluesky](https://img.shields.io/badge/Bluesky-0285FF?style=for-the-badge&logo=Bluesky&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

A Python bot that fetches headlines from *The Guardian*'s RSS feed, OwOifies them, and posts the the headlines to Bluesky.

![Preview Thumbnail](https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:fth7xvawb23gpzbzpx6clcio/bafkreia6egmguisdeugiir3pvkkq4crtqw4c77ajwuilk4dw74ab7t2lyi@jpeg)

## ✨ Features

- ✅ Pulls world news from [The Guardian](https://www.theguardian.com/world/rss)
- ✅ Filters out sad/violent headlines with a customizable blocklist
- ✅ Automatically OwOifies the headline text (nya~!)
- ✅ Adds preview thumbnails and clickable links in Bluesky posts
- ✅ Avoids reposting already-shared articles
- ✅ Manual approval step before posting
- ✅ Avoids reposting articles you Skip 
  
---

## 🚀 How It Works

1. The bot pulls fresh headlines.
2. Each headline is filtered for inappropriate content.
3. A headline is OwOified (e.g. "Love" → "Wuv", "R" → "W", etc.).
4. You get to approve or skip the post.
5. If approved, the bot posts it to your Bluesky account with a link preview and thumbnail.

---

## 📦 Requirements

- Python 3.9+
- [Bluesky ATProto](https://pypi.org/project/atproto/) SDK (`pip install atproto`)
- RSS feed parsing: `feedparser`

---
## Example Output

![Preview Thumbnail](https://i.imgur.com/TOZYwwV.png)
<!-- Old thumbnail without RSS image (https://i.imgur.com/i70p5rS.png) -->


---
## 🔧 Setup

1. **Clone the repository**

```
   git clone https://github.com/WagonWheelz/Rawrporter.git
```

2. **Install dependencies**
(This failed for me so I had to install each requirement manually)
```
   pip install -r requirements.txt
```

3. **Configure credentials**

   Create a `config.py` file (already included) and place in both your username and your APP password. You will need to generate an app password in bluesky:

```
   USERNAME = "yourhandle.bsky.social"
   APP_PASSWORD = "xxxx-xxxx-xxxx-xxxx"
```

4. **Add a thumbnail image**

   Place your preferred image in the bot folder as `thumbnail2.png`
   (This gets uploaded with each post).

5. **Adjust any blocklist settings you want**

   Review the existing blocklist in `news_fetcher.py`

6. **Run the bot**

   In your terminal run `python main.py`, If the setup works correctly, It will run through and pull the articles from the fetcher and prompt you for approval. Select Y or N depending on the approval and then you're ready!

---

## 🛠 Files

| File                | Description                                    |
| ------------------- | ---------------------------------------------- |
| `auto-main.py`      | Main entry point for the bot                   |
| `main.py`           | Main entry point for the bot                   |
| `news_fetcher.py`   | Fetches and filters RSS feed headlines         |
| `owoifier.py`       | Transforms text into OwOified form             |
| `bluesky_client.py` | Handles login and posting with embeds          |
| `posted.txt`        | Tracks posted/skipped links to avoid reposting |
| `config.py`         | Stores your Bluesky credentials                |

---

## 🤖 AI Disclosure

ChatGPT was used to beautify the code and develop some functions. This was my first time making a bot of any kind or code of any kind and used ChatGPT to assist me, I then autopsy each request and learn how it works so I can learn for myself next time. I have taken the code ChatGPT provided and streamlined it (I Think) hwoever it works and there may still be issues. I attempted to create this repo and the readme based on other ones i've seen hwoever I may have gotten part of it wrong, ChatGPT was not used for the creation of this readme file.

