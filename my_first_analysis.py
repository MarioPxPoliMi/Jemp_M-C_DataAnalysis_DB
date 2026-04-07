import pandas as pd

storie = pd.read_csv('Storie.csv')
post = pd.read_csv('Post.csv')

storie["created_time"] = pd.to_datetime(storie["created_time"])
post["created_time"] = pd.to_datetime(post["created_time"])



