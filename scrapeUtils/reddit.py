import argparse
import os
import praw
from config.keys import *
import sys
from praw.models import MoreComments

reddit = praw.Reddit(
    client_id=REDDIT_ID,
    client_secret=REDDIT_SECRET_KEY,
    user_agent=REDDIT_USER_AGENT,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,

)


# (1). AutoModerator: **Attention! [Serious] Tag Notice**

# * [Jokes, puns, and off-topic comments are not permitted](https://www.reddit.com/r/AskReddit/wiki/index#wiki_-rule_6-) in **any** comment, parent or child.

# * Parent comments that aren't from the target group will be removed, along with their child replies. 

# * Report comments that violate these rules.

# Posts that have few relevant answers within the first hour, and posts that are not appropriate for the [Serious] tag will be removed. Consider doing an AMA request instead.

# Thanks for your cooperation and enjoy the discussion!


# *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AskReddit) if you have any questions or concerns.*

#remove this comment if comes up

def get_post_and_replies(post_url, num_vids=10,word_limit=100,commentLimit=10):
    print("Getting post ...")
    submission = reddit.submission(url=post_url)
    post_text = {}
    # post_text["ques"] = submission.title + "\n" + submission.selftext
    # #get replies

    post_text["ques"] = submission.title + "\n" + submission.selftext
    #get replies
    word_count = len(post_text["ques"].split())
    if word_count > word_limit/4:
        return "Length of post is too long",True

    print("Post retrieved \nGetting comments ...")
    post_text["comments"] = {}
    vid_count = 1
    comm=[]
    word_count = 0
    submission.comments.replace_more(limit=commentLimit)
    for comment in submission.comments:
        if comment.author is None or comment.author.name == "AutoModerator" :
            continue
        if isinstance(comment, MoreComments):
            continue

        if(word_count + len(comment.body.split()) > word_limit):

            if len(comm) > 0:
                post_text["comments"][vid_count] = comm
                vid_count += 1
                print(f"Comment {vid_count-1} added\t Length: {word_count} words\t({word_count/word_limit*100:.2f}%)")

            comm=[]
            word_count = 0
            if len(comment.body.split()) > word_limit:
                continue
            if vid_count > num_vids:
                break
        
        comm.append(comment.body)
        word_count += len(comment.body.split())

    texts=[]
    for key in post_text["comments"]:
        #ques
        text=post_text["ques"]+"\n"
        #comment
        for i,comment in enumerate(post_text["comments"][key]):
            text+=f"{i+1}: {comment}\n"
        texts.append(text)
    
    return texts,False

def get_top_posts(subreddit_name, num_posts=1000):
    if not os.path.exists(f'posts/subreddit/{subreddit_name}'):
        os.makedirs(f'posts/subreddit/{subreddit_name}')
    post_links = set()
    if os.path.exists(f"posts/{subreddit_name}/pending.txt"):
        with open(f"posts/{subreddit_name}/pending.txt", "r") as f:
            post_links = set(f.read().splitlines())
    subreddit = reddit.subreddit(subreddit_name)
    #all time top posts no limit
    top_posts = subreddit.top("all", limit=num_posts)
    new_post_links = set()
    for post in top_posts:
        if post.permalink not in post_links:
            new_post_links.add(f"https://reddit.com{post.permalink}")

    with open(f"posts/subreddit{subreddit_name}/pending.txt", "a") as f:
        for post_link in new_post_links:
            f.write(post_link + "\n")
    return f"{len(new_post_links)} new posts added to pending.txt"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reddit post and subreddit downloader")
    parser.add_argument("-p", "--post", help="URL of the post to download")
    parser.add_argument("-n", "--num_replies", type=int, default=10, help="Number of replies to download")
    parser.add_argument("-s", "--subreddit", help="Name of the subreddit to download")
    args = parser.parse_args()

    if args.post:
        post_text = get_post_and_replies(args.post, args.num_replies)
        if not os.path.exists("posts"):
            os.makedirs("posts")
        with open("posts/post.txt", "w") as f:
            f.write(post_text)
        print("Post saved in posts/post.txt")
    elif args.subreddit:
        print(get_top_posts(args.subreddit))
    else:
        print("Please provide either -p or -s option")
