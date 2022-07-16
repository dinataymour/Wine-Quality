#Investigate a dataset on chemical properities and  quality ratings of wine samples by going through the entire data analysis process and
#and building more skill with python for data analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
% matplotlib inline
df_red = pd.read_csv('winequality-red.csv', sep = ';')
df_white = pd.read_csv('winequality-white.csv', sep = ';' )

#how many samples of red wine are there? how many samples of white wine are there?
df_red.count()
df_white.count()

#how many missing values are there in both datasets?
df_red.isnull().sum()
df_white.isnull().sum()

#how many duplicated rows are in the white wine dataset?
sum(df_white.duplicated())

#how many unique values of quality are in the red and white datasets
df_red.nunique()
df_white.nunique()

#What is the mean of the density column?
df_red['density'].mean()

#create color arrays for both dataset
color_red = np.repeat('red', df_red.shape[0])
color_white = np.repeat('white', df_white.shape[0])

#Add arrays to the red and white dataframes. Do this by setting a new column called 'color' to the appropriate array. The cell below does this for the red dataframe.
df_red['color'] = color_red
df_red.head()
df_white['color']= np.repeat('white', white_df.shape[0])
df_white.head()

#combine dataframes together
wine_df= df_red.append(df_white)
wine_df.head()

#save the combined dataset
wine_df.to_csv('winequality_edited.csv', index=False)

##EDA with visuals
wine_df.fixed_acidity.hist()
wine_df.total_sulfur_dioxide.hist()
wine_df.pH.hist()
wine_df.alcohol.hist()

#Scatterplots of Quality Against various features
wine_df.plot(x= 'volatile_acidity', y= 'quality', kind='scatter')
wine_df.plot(x= 'alcohol', y= 'quality', kind='scatter')
wine_df.plot(x= 'pH', y= 'quality', kind='scatter')
wine_df.plot(x= 'residual_sugar', y= 'quality', kind='scatter')

#Is a certain type of wine associated with higher quality?
df.groupby('color').mean().quality

#What level of acidity receives the highest average rating? get the 5 number summary
df.describe().pH

## Bin edges that will be used to "cut" the data into groups
bin_edges = [ 2.72,3.11 , 3.21,3.32 ,4.01 ] # Fill in this list with five values you just found

# Labels for the four acidity level groups
bin_names = ['high' , 'mod_high' , 'medium' , 'low' ] # Name each acidity level category

# Creates acidity_levels column
wine_df['acidity_levels'] = pd.cut(wine_df['pH'], bin_edges, labels=bin_names)

# Checks for successful creation of this column
wine_df.head()

# Find the mean quality of each acidity level with groupby
wine_df.groupby('acidity_levels').mean().quality

# Save changes for the next section
wine_df.to_csv('winequality_edited.csv', index=False)

###do wines with higher alcoholic content receive better ratings?
# get the median amount of alcohol content
df['alcohol'].median()
# select samples with alcohol content less than the median
low_alcohol = df.query('alcohol < 10.300000000000001')


# select samples with alcohol content greater than or equal to the median
high_alcohol = df.query('alcohol >= 10.300000000000001')

# ensure these queries included each sample exactly once
num_samples = df.shape[0]
num_samples == low_alcohol['quality'].count() + high_alcohol['quality'].count()
# The answer to the question should be True

Do sweeter wines receive better ratings?
# get the median amount of residual sugar
df.residual_sugar.median()

# select samples with residual sugar less than the median
low_sugar = df.query('residual_sugar < 3.0')

# select samples with residual sugar greater than or equal to the median
high_sugar = df.query('residual_sugar > = 3.0')

# ensure these queries included each sample exactly once
num_samples == low_sugar['quality'].count() + high_sugar['quality'].count()
# The answer to the question should be True

# get mean quality rating for the low sugar and high sugar groups
low_sugar.quality.mean(), high_sugar.quality.mean()

###Creating a bar chart using matplotlib
# plot bars
plt.bar([1, 2, 3], [224, 620, 425])

# specify x coordinates of tick labels and their labels
plt.xticks([1, 2, 3], ['a', 'b', 'c']);
plt.title('Some Title')
plt.xlabel('Some X Label')
plt.ylabel('Some Y Label');

#1: Do wines with higher alcoholic content receive better ratings?
#Create a bar chart with one bar for low alcohol and one bar for high alcohol wine samples.
# Use query to select each group and get its mean quality
median = df['alcohol'].median()
low = df.query('alcohol < {}'.format(median))
high = df.query('alcohol >= {}'.format(median))

mean_quality_low = low['quality'].mean()
mean_quality_high = high['quality'].mean()

# Create a bar chart with proper labels
locations = [1, 2]
heights = [mean_quality_low, mean_quality_high]
labels = ['Low', 'High']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Average Quality Rating');

#2: Do sweeter wines receive higher ratings?
#Create a bar chart with one bar for low residual sugar and one bar for high residual sugar wine samples.
# Use query to select each group and get its mean quality
median = df['alcohol'].median()
low = df.query('alcohol < {}'.format(median))
high = df.query('alcohol >= {}'.format(median))

mean_quality_low = low['quality'].mean()
mean_quality_high = high['quality'].mean()

# Create a bar chart with proper labels

locations = [1, 2]
heights = [mean_quality_low, mean_quality_high]
labels = ['Low', 'High']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Average Quality Rating')

#3: What level of acidity receives the highest average rating?
#Create a bar chart with a bar for each of the four acidity levels.

# Use groupby to get the mean quality for each acidity level
acidity_level_quality_means = df.groupby('acidity_levels').quality.mean()

# Create a bar chart with proper labels
locations = [4, 1, 2, 3]
heights = acidity_level_quality_means
labels = ['Low', 'Medium', 'Moderately High', 'High']
labels = acidity_level_quality_means.index.str.replace('_', ' ').str.title()
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Acidity Level')
plt.xlabel('Acidity Level')
plt.ylabel('Average Quality Rating')

#Create arrays for red bar heights white bar heights
#Remember, there's a bar for each combination of color and quality rating.
#Each bar's height is based on the proportion of samples of that color with that quality rating.
#Red bar proportions = counts for each quality rating / total # of red samples
#White bar proportions = counts for each quality rating / total # of white samples

# get counts for each rating and color
color_counts = wine_df.groupby(['color', 'quality']).count()['pH']
color_counts

# get total counts for each color
color_totals = wine_df.groupby('color').count()['pH']
color_totals

# get proportions by dividing red rating counts by total # of red samples
red_proportions = color_counts['red'] / color_totals['red']
red_proportions

# get proportions by dividing white rating counts by total # of white samples
white_proportions = color_counts['white'] / color_totals['white']
white_proportions

#Plot proportions on a bar chart

#we're missing a red wine value for a the 9 rating. Even though this number is a 0, we need it for our plot.
red_proportions['9'] = 0
red_proportions

#set the x coordinate location for each rating group and and width of each bar.
ind = np.arange(len(red_proportions))  # the x locations for the groups
width = 0.35       # the width of the bars

# plot bars
red_bars = plt.bar(ind, red_proportions, width, color='r', alpha=.7, label='Red Wine')
white_bars = plt.bar(ind + width, white_proportions, width, color='w', alpha=.7, label='White Wine')

# title and labels
plt.ylabel('Proportion')
plt.xlabel('Quality')
plt.title('Proportion by Wine Color and Quality')
locations = ind + width / 2  # xtick locations
labels = ['3', '4', '5', '6', '7', '8', '9']  # xtick labels
plt.xticks(locations, labels)

# legend
plt.legend();
