import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

us_videos_path = 'USvideos.csv'
us_videos_df = pd.read_csv(us_videos_path)

# Convert 'publish_time' to datetime and extract hour
us_videos_df['publish_time'] = pd.to_datetime(us_videos_df['publish_time'], format='%Y-%m-%dT%H:%M:%S.%fZ')
us_videos_df['publish_hour'] = us_videos_df['publish_time'].dt.hour

# Aggregate data by hour to find the average number of views
hourly_popularity = us_videos_df.groupby('publish_hour')['views'].mean().reset_index()

# Plot the data with explicit labeling of the y-axis
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x='publish_hour', y='views', data=hourly_popularity, marker='o')
plt.title('Average Popularity by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Average Views (in millions)')
plt.xticks(range(0, 24))
plt.tight_layout()

# Adjust y-axis format to show the label in millions
scale_factor = 1e6
ticks_loc = plt.gca().get_yticks().tolist()
plt.gca().yaxis.set_major_locator(plt.FixedLocator(ticks_loc))
plt.gca().set_yticklabels(['{:.1f}'.format(x/scale_factor) for x in ticks_loc])

plt.show()
