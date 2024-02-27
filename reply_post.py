import praw
import pdb
import re
import os

#In here, we're going to create the Reddit instance
reddit = praw.Reddit('YafetBot')
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))

with open("posts_replied_to.txt", "r") as f:
    posts_replied_to = f.read()
    posts_replied_to = posts_replied_to.split("\n")

#In here you would enter the submission ID's but that differs with each user

subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("Botty bot says: Me too!!")

print("Bot replying to : ", submission.title)
posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
    f.write(post_id + "\n")