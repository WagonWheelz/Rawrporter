from atproto import Client
from atproto_client.models.app.bsky.embed.external import Main as EmbedExternal
from atproto_client.models.app.bsky.embed.external import External
import os

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

    def post(self, content, link):
        try:
            embed = EmbedExternal(
                external=External(
                    uri=link,
                    title="News Article",
                    description="Click to read the full article.",
                )
            )

            self.client.send_post(text=content, embed=embed)
            return True
        except Exception as e:
            print("[Bluesky Error] Post failed:", e)
            return False
