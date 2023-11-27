# First Data
import matplotlib.pyplot as plt
avg_views_per_country = {}
for country, data in selected_countries.items():
    avg_views = data.groupby('category')['views'].mean()
    avg_views_per_country[country] = avg_views

# Creating the visualization
plt.figure(figsize=(15, 10))

# Plotting average views by category for each country
for country, avg_views in avg_views_per_country.items():
    sns.barplot(x=avg_views.index, y=avg_views.values, label=country)

plt.xticks(rotation=90)
plt.xlabel('Category')
plt.ylabel('Average Views')
plt.title('Comparison of Average Views by Category Across Countries')
plt.legend(title='Country')
plt.tight_layout()

# Showing the plot
plt.show()

# Second data 
def correct_date_format(date_str):
    return datetime.strptime(date_str, "%y.%d.%m") if '.' in date_str else datetime.strptime(date_str, "%Y-%m-%d")

us_videos['trending_date'] = us_videos['trending_date'].apply(correct_date_format)

# Calculating the duration for which each video remains trending
us_videos['trending_duration'] = us_videos.groupby('video_id')['trending_date'].transform(lambda x: x.max() - x.min())
us_videos['trending_duration'] = us_videos['trending_duration'].dt.days

# Creating the histogram for trending duration
plt.figure(figsize=(15, 8))
sns.histplot(us_videos['trending_duration'], bins=30, kde=True)
plt.xlabel('Duration in Trending (Days)')
plt.ylabel('Frequency')
plt.title('Trending Duration Analysis in the United States')
plt.show()

# Third Data
# Applying a log transformation to both 'views' and 'likes' for better visualization

import numpy as np

# Filtering out rows where views or likes are zero to avoid issues with log transformation
filtered_us_videos = us_videos[(us_videos['views'] > 0) & (us_videos['likes'] > 0)]

# Applying log transformation
filtered_us_videos['log_views'] = np.log(filtered_us_videos['views'])
filtered_us_videos['log_likes'] = np.log(filtered_us_videos['likes'])

# Creating the scatter plot with log-transformed values
plt.figure(figsize=(15, 8))
sns.scatterplot(x='log_views', y='log_likes', data=filtered_us_videos)
plt.xlabel('Log of Views')
plt.ylabel('Log of Likes')
plt.title('Correlation Between Likes and Views in the United States (Log Transformed)')

# Adding a regression line to the scatter plot
sns.regplot(x='log_views', y='log_likes', data=filtered_us_videos, scatter=False, color='red')

plt.show()