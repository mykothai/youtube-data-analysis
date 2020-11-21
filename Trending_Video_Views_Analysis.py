##############################################################################################################################
##############################################################################################################################
#
#       CMPT 353 FINAL PROJECT:
#       This script performs post hoc analysis on the view count of 
#       trending YouTube videos for the periods of pre (2018) and during (2020) COVID-19.
#       
#       Please reference the README file for a full guide on how to build this script, but look below
#       for a quick start guide.
#
#       This analysis runs for the following countries:
#
#       Country                 Command
#
#       Canada                  Python3 Trending_Video_Views_Analysis.py CA
#       USA                     Python3 Trending_Video_Views_Analysis.py US
#       Great Britain           Python3 Trending_Video_Views_Analysis.py GB
#
##############################################################################################################################
##############################################################################################################################


########################### LIBRARIES ####################################
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from time import sleep
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import sys


########################### FUNCTIONS ####################################

# Helper function used to convert the video category file for 2018 data to a valid Dataframe object
# with specified column names.
def convert_json_cats_to_pandas_2018(json_dir):
    
    # Read in the json data
    with open(json_dir) as f:
        cat_data = json.load(f)

    # define the dataframe column names + series for each name
    cat = {'category_id': [], 'cat_name': []}

    # Parse through the json data and add key values to dataframe object
    for i in cat_data['items']:
        cat['category_id'].append(i['id'])
        cat['cat_name'].append(i['snippet']['title'])

    # define the dataframe object and add data to it
    df = pd.DataFrame(data = cat)

    return(df)


# Helper function used to merge 2018 video data and category data into a valid Dataframe object
# NOTE: This function should only be used for 2018 YouTube videos
def get_merged_data_2018(vids_dir, cats_dir):

    # Import the compressed csv file
    vids_df = pd.read_csv(vids_dir)

    # Load category file
    cats_df = convert_json_cats_to_pandas_2018(cats_dir)
    cats_df['category_id'] = cats_df['category_id'].astype(int)

    # Merge video and category dataframes to get the full data
    all_vid_data = pd.merge(vids_df, cats_df, on='category_id')

    # Group by category + count keys in each category
    daily_cats = all_vid_data.groupby('cat_name').agg(['count'])['video_id'].reset_index()

    return(daily_cats)


# Helper function used to convert the video category file for 2020 data to a valid Dataframe object
# with specified column names.
def convert_json_cats_to_pandas_2020(json_dir):
    
    # Load in the categories
    with open(json_dir) as f:
        cat_data = json.load(f)

    # define the dataframe column names + series for each name    
    cat = {'categoryId': [], 'cat_name': []}

    # Parse through the json data and add key values to dataframe object
    for i in cat_data['items']:
        cat['categoryId'].append(i['id'])
        cat['cat_name'].append(i['snippet']['title'])

    # define the dataframe object and add data to it
    df = pd.DataFrame(data = cat)

    return(df)


# Helper function used to merge 2018 video data and category data into a valid Dataframe object
# NOTE: This function should only be used for 2020 YouTube videos
def get_merged_data_2020(vids_dir, cats_dir):

    # Import the compressed csv file
    vids_df = pd.read_csv(vids_dir)

    # Load category file
    cats_df = convert_json_cats_to_pandas_2020(cats_dir)
    cats_df['categoryId'] = cats_df['categoryId'].astype(int)

    # Merge video and category dataframes to get the full data
    all_vid_data = pd.merge(vids_df, cats_df, on='categoryId')

    # Group by category + count keys in each category
    daily_cats = all_vid_data.groupby('cat_name').agg(['count'])['video_id'].reset_index()

    return(daily_cats)


# Helper function used to plot the count of video categories for 2018 vs 2020.
def create_barplot(df, country):

    # derive useful columns
    cats       = df['cat_name']
    count_2018 = df['count_2018']
    count_2020 = df['count_2020']

    # Create the y position of the plot
    ypos = np.arange(len(cats))

    # Set the figure margins
    plt.figure(figsize=(10,15))

    # Create bars at specified locations
    plt.bar(ypos-0.2, count_2018, width=0.4, label='2018 Count', color='red')
    plt.bar(ypos+0.2, count_2020, width=0.4, label='2020 Count', color='blue')
    plt.xticks(ypos, cats)
    plt.xticks(rotation=90)
    plt.ylabel('Trending Count')    
    plt.legend()
    plt.ylabel('Count')

    # Create the title of the barplot
    title = str(country) + ' - Trending Youtube Video Count'
    plt.title(title)

    # Save file to local workiing directory
    file_title = title + '.png'
    plt.savefig(file_title, dpi=100)


# Helper function used to get the individual views of trending videos in 2018
# NOTE: This function should only be used for the 2018 dataset
def get_view_data_2018(vids_dir, cats_dir):

    # Import the video trending data
    vids_df = pd.read_csv(vids_dir)

    # Load category file
    cats_df = convert_json_cats_to_pandas_2018(cats_dir)
    cats_df['category_id'] = cats_df['category_id'].astype(int)

    # Merge video and category dataframes
    all_vid_data = pd.merge(vids_df, cats_df, on='category_id')
    
    # Return only relevant data values
    return(all_vid_data[['cat_name', 'views']])


# Helper function used to get the individual views of trending videos in 2020
# NOTE: This function should only be used for the 2020 dataset
def get_view_data_2020(vids_dir, cats_dir):

    # Import the video trending data
    vids_df = pd.read_csv(vids_dir)

    # Load category file
    cats_df = convert_json_cats_to_pandas_2020(cats_dir)
    cats_df['categoryId'] = cats_df['categoryId'].astype(int)

    # Merge video and category dataframes
    all_vid_data = pd.merge(vids_df, cats_df, on='categoryId')

    # Return only relevant data values
    ret = all_vid_data[['cat_name', 'view_count']].rename(columns={'view_count': 'views'})
    return(ret)


########################### MAIN ####################################
def main(country):

    # Print out a header
    print('\n\n-> Starting Analysis for Trending YouTube Videos in ' + str(country) + '\n')    

    # Print out calculation status report on screen
    for i in range(21):
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
        sys.stdout.flush()
        sleep(0.1)    
    
    # Get the 2018 data for the input country
    vids_2018_dir = './2018 Data/' + str(country) + 'videos' + '.csv.zip'
    cats_2018_dir = './2018 Data/' + str(country) + '_category_id.json'
    merged_2018_data = get_merged_data_2018(vids_2018_dir, cats_2018_dir)
    merged_2018_data = merged_2018_data.sort_values('count')

    # Get the 2020 data for the input country
    vids_2020_dir = './2020 Data/' + str(country) + '_youtube_trending_data.csv.zip'
    cats_2020_dir = './2020 Data/' + str(country) + '_category_id.json'
    merged_2020_data = get_merged_data_2020(vids_2020_dir, cats_2020_dir)    
    merged_2020_data = merged_2020_data.sort_values('count') 

    # Merge all of the data together
    all_data_merged = pd.merge(merged_2018_data, merged_2020_data, on=['cat_name'])
    all_data_merged = all_data_merged.rename(columns={"count_x": "count_2018","count_y": "count_2020"})

    # Create the barplot
    create_barplot(all_data_merged, country)

    # print the dataframe
    print("\n-> The Trending Count per Category for 2018 and 2020:\n\n", all_data_merged, '\n')

    # Create the contingency table
    # columns -> 2018, 2020
    # rows    -> video cateories
    col1 = all_data_merged['count_2018'].astype(int).tolist()
    col2 = all_data_merged['count_2020'].astype(int).tolist()
    contingency_table = np.array([col1, col2], dtype=np.uint32)

    # Contingency table used in Chi-Squared Analysis:
    print('\n-> Contingency table used in Chi-Squared Analysis:')
    print('\n2018 data:\n', col1, '\n')
    print('\n2020 data:\n', col2, '\n')

    # Perform a Chi Square Test on the table
    chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

    # Print results of the chi-squared test
    print('\n-> Chi Squared P-value for Wether or Not the Year had an Effect on the Category of Trending Videos:\n')
    print(p, '\n')

    # Get view data from trending categories
    views_per_cats_2018 = get_view_data_2018(vids_2018_dir, cats_2018_dir)
    views_per_cats_2020 = get_view_data_2020(vids_2020_dir, cats_2020_dir)

    # Get views of every trending video and extract the category and view count
    views_per_cats_2018 = get_view_data_2018(vids_2018_dir, cats_2018_dir)
    views_per_cats_2020 = get_view_data_2020(vids_2020_dir, cats_2020_dir)

    # Keep rows that are in categories that are common to both years
    categories_in_2018 = views_per_cats_2018['cat_name'].unique()
    categories_in_2020 = views_per_cats_2020['cat_name'].unique()
    common_cats = np.intersect1d(categories_in_2018, categories_in_2020)
    views_per_cats_2018 = views_per_cats_2018[views_per_cats_2018['cat_name'].isin(common_cats)]
    views_per_cats_2020 = views_per_cats_2020[views_per_cats_2020['cat_name'].isin(common_cats)]

    # Label the data and combine
    views_per_cats_2018['cat_name'] = views_per_cats_2018['cat_name'].astype(str) + '_2018'
    views_per_cats_2020['cat_name'] = views_per_cats_2020['cat_name'].astype(str) + '_2020'

    all_labeled_views_per_cats = views_per_cats_2018.append(views_per_cats_2020, ignore_index=True)

    # Tukey's Analysis
    posthoc = pairwise_tukeyhsd(
            all_labeled_views_per_cats['views'], 
            all_labeled_views_per_cats['cat_name'],
            alpha=0.05)

    print('\n-> PostHoc Analysis for Views Per Categories for 2018 vs 2020:\n')
    print(posthoc)

    # Save Tukey's data
    fig = posthoc.plot_simultaneous()    
    fig.set_size_inches(20, 20)
    title = str(country) + '_Views_Per_Cats_Tukeys_Analysis.png'
    fig.savefig(title)

    # Print end line
    print('\n\n\n  -> Analysis Complete <-  \n')


if __name__=='__main__':
    in_country = sys.argv[1]
    main(in_country)