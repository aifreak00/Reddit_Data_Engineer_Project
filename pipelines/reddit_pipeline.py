from etls.reddit_etl import connect_reddit
from etls.reddit_etl import extract_posts
from utils.constants import CLIENT_ID,SECRET
from etls.reddit_etl import transform_data
from etls.reddit_etl import load_data_to_csv
from utils.constants import OUTPUT_PATH
import pandas as pd

# def reddit_pipeline(file_name:str,subreddit=str,time_filter='all',limit=None):
#   #connecting to reddit instance
#   instance= connect_reddit(CLIENT_ID,SECRET,user_agent='vikram')
#   #extraction
#   posts=extract_posts(instance,subreddit,time_filter,limit)
#   posts_df=pd.DataFrame(posts)
#   #transformation
#   posts_df=transform_data(posts_df)
#   #loading to csv
#   file_path = f'{OUTPUT_PATH}/{file_name}.csv'
#   load_data_to_csv(post_df, file_path)

#   return file_path
def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    # connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
    # extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    # transformation
    post_df = transform_data(post_df)
    # loading to csv
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_df, file_path)

    return file_path
