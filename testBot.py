
import praw
from psaw import PushshiftAPI
import datetime as dt 
import wsb_post



reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
    username="",
)
print(reddit.read_only)
#subreddit = reddit.subreddit("algotrading")

subreddit = (reddit.subreddit('datascience')).hot(limit=10)
#top = subreddit.hot(limit=10)

for submission in subreddit :
   print(submission.title,' ', submission.num_comments)

