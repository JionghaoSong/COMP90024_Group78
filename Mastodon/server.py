import os
import json

POPULAR_SERVERS = [
    "mastodon.social",
    "aus.social",
]

with open('token.json', 'r') as f:
    tokens = json.load(f)

ACCESS_TOKENS = {
    "mastodon.social": tokens["MASTODON_SOCIAL_TOKEN"],
    "mastodon.au": tokens["MASTODON_AU_TOKEN"]
}