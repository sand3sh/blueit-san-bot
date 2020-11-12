import praw
from prawcore.exceptions import Forbidden

reddit = praw.Reddit(client_id="v99rTd7MTKhflQ",
                        client_secret="cqCdyEEoDtfp1EyoC33mpikSsOg",
                        password="No_Artichoke23721986",
                        user_agent="script by u/No_Artichoke2372",
                        username="No_Artichoke2372")


print(reddit.read_only)  # Output: True

#FortNiteBR
#sansubreddit
subreddit = reddit.subreddit("FortNiteBR")

print(subreddit.display_name)  # output: redditdev
print(subreddit.title)         # output: reddit development
print(subreddit.description)   # output: a subreddit for discussion of ...

#params = {"title": "I switched my sens up like 4 times yesterday #fortnite ", "url": "https://twitter.com/i/status/1325796837941534720", "flair_id":"70774926-23ca-11eb-976e-0e7bc519d963", "flair_text":"humour"}
params = {"title": "I switched my sens up like 4 times yesterday #fortnite ", "url": "https://twitter.com/i/status/1325796837941534720"}
post = subreddit.submit(**params)
#subreddit.submit('My Title Bot1', selftext='Stuff you want to put in the textbox')

#to get all flair ids
for flair in post.flair.choices():
    print(flair)