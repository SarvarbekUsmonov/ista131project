import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json
from datetime import datetime

def load_and_extract_category_names(file_path):
    with open(file_path, 'r') as file:
        category_data = json.load(file)
    category_names = {int(item['id']): item['snippet']['title'] for item in category_data['items']}
    return category_names

# Loading datasets
ca_videos = pd.read_csv('CAvideos.csv')
us_videos = pd.read_csv('USvideos.csv')

# Loading category names
ca_categories = load_and_extract_category_names('CA_category_id.json')
us_categories = load_and_extract_category_names('US_category_id.json')

# Merging categories with videos data
ca_videos['category'] = ca_videos['category_id'].map(ca_categories)
us_videos['category'] = us_videos['category_id'].map(us_categories)


# # Load the data
# ca_videos = pd.read_csv('CAvideos.csv')
# us_videos = pd.read_csv('USvideos.csv')

# Scatter plot with regression for Canadian data
plt.figure(figsize=(12, 8))
sns.regplot(x='views', y='comment_count', data=ca_videos, scatter_kws={'alpha':0.3}, line_kws={'color': 'red'})
plt.title('Correlation Between Comments and Views in Canada')
plt.xlabel('Views')
plt.ylabel('Comments')
plt.show()

# Bar chart for US data - Top 10 Most Popular Channels by Average Views
average_views_by_channel = us_videos.groupby('channel_title')['views'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 8))
sns.barplot(x=average_views_by_channel.values, y=average_views_by_channel.index, palette="viridis")
plt.xlabel('Average Views')
plt.ylabel('Channel')
plt.title('Top 10 Most Popular Channels by Average Views in the United States')
plt.show()

# Histogram for US data - Dislikes to Likes Ratio Analysis
us_videos['dislikes_to_likes_ratio'] = us_videos['dislikes'] / us_videos['likes']
plt.figure(figsize=(12, 8))
sns.histplot(us_videos['dislikes_to_likes_ratio'].dropna(), bins=30, kde=True, color='teal')
plt.xlabel('Dislikes to Likes Ratio')
plt.ylabel('Frequency')
plt.title('Dislikes to Likes Ratio Analysis in the United States')
plt.show()
