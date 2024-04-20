from praw import Reddit
import sys

import numpy as np
import pandas as pd
import praw
from utils.constants import POST_FIELDS

def connect_reddit(client_id,client_secret,user_agent)-> Reddit:
    try:
        reddit=praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent)
        print("connected to reddit") 
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)
def extract_posts(reddit_instance:Reddit,subreddit:str,time_filter:str,limit=None):
    subreddit=reddit_instance.subreddit(subreddit)
    posts=subreddit.top(time_filter=time_filter,limit=limit)
    post_lists=[]        
    for post in posts:
        post_dict = vars(post)
        post = {key: post_dict[key] for key in POST_FIELDS}
        post_lists.append(post)

    return post_lists

def transform_data(posts_df: pd.DataFrame):
    posts_df['created_utc'] = pd.to_datetime(posts_df['created_utc'], unit='s')
    posts_df['over_18'] = np.where((posts_df['over_18'] == True), True, False)
    posts_df['author'] = posts_df['author'].astype(str)
    edited_mode = posts_df['edited'].mode()
    posts_df['edited'] = np.where(posts_df['edited'].isin([True, False]),
                                  posts_df['edited'], edited_mode).astype(bool)
    posts_df['num_comments']=posts_df['num_comments'].astype(int)
    posts_df['score']=posts_df['score'].astype(int)
    posts_df['title']=posts_df['title'].astype(str)
    return posts_df

def load_data_to_csv(data:pd.DataFrame,path:str):
    data.to_csv(path,index=False)

