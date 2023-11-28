import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Load the dataset
us_videos_path = 'USvideos.csv'  # Make sure this path is correct
us_videos_df = pd.read_csv(us_videos_path)

# Convert 'publish_time' to datetime and extract the day of the week
us_videos_df['publish_time'] = pd.to_datetime(us_videos_df['publish_time'], format='%Y-%m-%dT%H:%M:%S.%fZ')
us_videos_df['publish_dayofweek'] = us_videos_df['publish_time'].dt.day_name()

# Aggregate data by the day of the week to find the average number of views
weekly_popularity = us_videos_df.groupby('publish_dayofweek')['views'].mean().reset_index()

# Sort the days for proper ordering in the plot
ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekly_popularity['publish_dayofweek'] = pd.Categorical(weekly_popularity['publish_dayofweek'], categories=ordered_days, ordered=True)
weekly_popularity = weekly_popularity.sort_values('publish_dayofweek')

# Plot the data
sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='publish_dayofweek', y='views', data=weekly_popularity, palette="viridis", ax=ax)
ax.set_title('Average Popularity by Day of Week (in millions)')
ax.set_xlabel('Day of Week')
ax.set_ylabel('Average Views')

# Adjust y-axis format to show the label in millions
def millions_formatter(x, pos):
    return '%1.1fM' % (x * 1e-6)
ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))

# Fix any potential overlap with layout
plt.tight_layout()

plt.show()