import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json
from datetime import datetime

# Function for loading and extract category names from JSON file
def load_and_extract_category_names(file_path):
    with open(file_path, 'r') as file:
        category_data = json.load(file)
    category_names = {int(item['id']): item['snippet']['title'] for item in category_data['items']}
    return category_names

# Loading datasets
ca_videos = pd.read_csv('CAvideos.csv')
de_videos = pd.read_csv('DEvideos.csv')
gb_videos = pd.read_csv('GBvideos.csv')
us_videos = pd.read_csv('USvideos.csv')

# Loading category names
ca_categories = load_and_extract_category_names('CA_category_id.json')
de_categories = load_and_extract_category_names('DE_category_id.json')
gb_categories = load_and_extract_category_names('GB_category_id.json')
us_categories = load_and_extract_category_names('US_category_id.json')

# Merging categories with videos data
ca_videos['category'] = ca_videos['category_id'].map(ca_categories)
de_videos['category'] = de_videos['category_id'].map(de_categories)
gb_videos['category'] = gb_videos['category_id'].map(gb_categories)
us_videos['category'] = us_videos['category_id'].map(us_categories)

# Visualization 1: Comparison of Average Views by Category Across Countries
selected_countries = {
    "Canada": ca_videos,
    "Germany": de_videos,
    "Great Britain": gb_videos,
    "United States": us_videos
}

plt.figure(figsize=(15, 10))
for country, data in selected_countries.items():
    avg_views = data.groupby('category')['views'].mean()
    sns.barplot(x=avg_views.index, y=avg_views.values, label=country)
plt.xticks(rotation=90)
plt.xlabel('Category')
plt.ylabel('Average Views')
plt.title('Comparison of Average Views by Category Across Countries')
plt.legend(title='Country')
plt.tight_layout()
plt.show()

# Visualization 2: Trending Duration Analysis in the United States
us_videos['trending_date'] = pd.to_datetime(us_videos['trending_date'], format='%y.%d.%m')
us_videos['trending_duration'] = us_videos.groupby('video_id')['trending_date'].transform(lambda x: x.max() - x.min()).dt.days
plt.figure(figsize=(15, 8))
sns.histplot(us_videos['trending_duration'], bins=30, kde=True)
plt.xlabel('Duration in Trending (Days)')
plt.ylabel('Frequency')
plt.title('Trending Duration Analysis in the United States')
plt.show()

# Visualization 3: Correlation Between Likes and Views in the United States (Log Transformed)
us_videos_filtered = us_videos[(us_videos['views'] > 0) & (us_videos['likes'] > 0)]
us_videos_filtered['log_views'] = np.log(us_videos_filtered['views'])
us_videos_filtered['log_likes'] = np.log(us_videos_filtered['likes'])
plt.figure(figsize=(15, 8))
sns.scatterplot(x='log_views', y='log_likes', data=us_videos_filtered)
sns.regplot(x='log_views', y='log_likes', data=us_videos_filtered, scatter=False, color='red')
plt.xlabel('Log of Views')
plt.ylabel('Log of Likes')
plt.title('Correlation Between Likes and Views in the United States (Log Transformed)')
plt.show()
