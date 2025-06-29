from atproto import Client
from atproto_client.models.app.bsky.embed.external import Main as EmbedExternal
from atproto_client.models.app.bsky.embed.external import External
import requests

class BlueskyClient:
    def __init__(self, username, app_password):
        self.client = Client()
        self.username = username
        self.app_password = app_password

    def login(self):
        try:
            self.client.login(self.username, self.app_password)
            return True
        except Exception as e:
            print("[Bluesky Error] Login failed:", e)
            return False

    def post(self, headline, content, link, image_url="https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:fth7xvawb23gpzbzpx6clcio/bafkreia6egmguisdeugiir3pvkkq4crtqw4c77ajwuilk4dw74ab7t2lyi@jpeg"):
        try:
            blob = None

            if image_url:
                response = requests.get(image_url)
                response.raise_for_status()
                blob = self.client.com.atproto.repo.upload_blob(response.content)

            embed = EmbedExternal(
                external=External(
                    uri=link,
                    title=headline,
                    description="Click to read the full article.",
                    thumb=blob.blob if blob else None
                )
            )

            self.client.send_post(text=content, embed=embed)
            return True
        except Exception as e:
            print("[Bluesky Error] Post failed:", e)
            return False
