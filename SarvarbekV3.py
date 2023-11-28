import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

us_videos_path = 'USvideos.csv'
us_videos_df = pd.read_csv(us_videos_path)

# Convert the relevant columns to numeric and drop any rows with NaN values
numeric_cols = ['views', 'likes', 'dislikes', 'comment_count']
us_videos_df[numeric_cols] = us_videos_df[numeric_cols].apply(pd.to_numeric, errors='coerce')
us_videos_df.dropna(subset=numeric_cols, inplace=True)

# Compute the correlation matrix
correlation_matrix = us_videos_df[numeric_cols].corr()

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Draw the heatmap with the correlation matrix
# Include the vmin and vmax parameters to set the color scale from -1 to 1
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=.5, vmin=-1, vmax=1)

# Add the title
plt.title('Correlation Heatmap of Trending YouTube Video Statistics')

# Show the plot
plt.show()
