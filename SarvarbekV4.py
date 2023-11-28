import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Load the dataset
us_videos = pd.read_csv('USvideos.csv')

# Clean the dataset by removing any potential outliers or erroneous data
# Assuming that videos with extremely low views and likes are not relevant for the trend analysis
us_videos_clean = us_videos[(us_videos['views'] > 0) & (us_videos['comment_count'] > 0)]

# Set up the matplotlib figure
plt.figure(figsize=(12, 6))

# Draw the scatter plot using log scale for both axes to better visualize the distribution
sns.scatterplot(x='views', y='comment_count', data=us_videos_clean, alpha=0.3)

# Use numpy's polyfit to calculate the regression line on log scale data
# We first apply a log transformation to the 'views' and 'comment_count' columns
log_views = np.log(us_videos_clean['views'])
log_comments = np.log(us_videos_clean['comment_count'])

# Get the coefficients of a polynomial of degree 1 (linear fit)
slope, intercept = np.polyfit(log_views, log_comments, 1)

# Now we calculate the regression line's y points using the slope and intercept obtained
regression_line = np.exp(intercept) * us_videos_clean['views']**slope

# Plot the regression line on top of the scatter plot
plt.plot(us_videos_clean['views'], regression_line, color='red', label='Regression Line')

# Adjust the plot to use a logarithmic scale
plt.xscale('log')
plt.yscale('log')

# Adding a title and labels with log scale notation
plt.title('Correlation between Views and Comments for Trending Videos in the United States (Logarithmic Scale)')
plt.xlabel('Views')
plt.ylabel('Comments')

# Show the legend
plt.legend()

# Show the plot
plt.show()
