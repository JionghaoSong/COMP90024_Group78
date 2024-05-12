import os

# Top 9 popular servers with more registered users
# from https://mastodonservers.net/servers/top
# Popular: social + au + other popular servers
POPULAR_SERVERS = [
    "mastodon.social",
    "mastodon.au",  # AUS server - 169 per day
    # "aus.social",  # AUS server - more popular 448 per day
    # "mastodon.cloud",
    # "mstdn.social",
    # "mastodon.online",
    # "mas.to",
    # "mastodon.world",
    # "c.im"
]

# Dictionary of access tokens
ACCESS_TOKENS = {
    "mastodon.social": os.getenv("MASTODON_SOCIAL_TOKEN"),
    "mastodon.au": os.getenv("MASTODON_AU_TOKEN"),
}
