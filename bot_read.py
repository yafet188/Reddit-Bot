##Client ID: IW3BqO_adYDO6_ibngO-FQ
##Secret: uLimswDhRo6v60S62X_MJxF4FKxD7w

##Start of code, initialized by importing praw.
import praw

##Creates a new praw object with the Reddit bot being named "YafetBot"
reddit = praw.Reddit("YafetBot")

subreddit = reddit.subreddit("learnpython")

##This loop iterates through the top 5 hot posts in the specified subreddit.
for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title) ##Prints the title of the post.
    print("Text: ", submission.selftext)  ##Prints the text content of the post (if any).
    print("Score: ", submission.score) ##Prints the score (upvotes minus downvotes) of the post.
    print("---------------------------------\n") ##Prints a divider to separate each post for better readability in the output.

