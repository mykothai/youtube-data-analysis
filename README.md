# CMPT 353 Final Project: The Pandemic and Trending YouTube Videos

## Project Description: 
We are interested in the correlation between Covid-19 and the properties of trending Youtube videos in three geographical regions: Canada, Great Britain, and USA. Our analysis is based on the following datasets:

* **2020 Daily Trending Youtube Videos:**     https://www.kaggle.com/rsrishav/youtube-trending-video-dataset
* **2018 Daily Trending Youtube Videos:**     https://www.kaggle.com/datasnaek/youtube-new

* **Please note**: The 2018 dataset only includes data from the months of January 2018 - April 2018 and the 2020 dataset only includes data from the months of August 2020 - October 2020. Since the data is limited to only these four month intervals, we will treat them as a sample to represent their respective year, and ignore any seasonality present that could be present in the data.

## The Main Questions We are Interested in:

1. Have the view count of the different trending YouTube categories changed significantly in 2018 versus 2020 in  Canada, Great Britain, and USA?

2. Have the ratio of likes versus views of the different trending YouTube categories changed significantly in 2018 versus 2020 in  Canada, Great Britain, and USA?


## Required Libraries: 
- pandas
- json
- matplotlib.pyplot
- numpy
- scipy
- time
- statsmodels.stats.multicomp
- sys
- datetime


## Building the Project: 
This project revolves around the above two questions, therefore, there are two parts to our analysis where each corresponds to each of these questions. Please see below on instructions on how to build these scripts for the respective questions.

### Building Scripts for Question 1:

1) Ensure all of the above packages are installed on your local machine.

2) Ensure all of the scripts and datasets in this repository are cloned to your local machine.

3) The script corresponding to question 1, 'Trending_Video_Views_Analysis.py', is expandable to any of the following three countries of your choice: Canada, Great Britain, USA. Please refer to the commands below to build and run this script.

* Canada: Python3 Trending_Video_Views_Analysis.py CA
* Great Britain: Python3 Trending_Video_Views_Analysis.py GB
* USA: Python3 Trending_Video_Views_Analysis.py US

4) Once you have executed the above commands, the output of the analysis corresponding to the country inputted to the script will be presented on the terminal. Relevant plots will be saved as PNG files to your computers working directory.

5) Refer to our paper for a thorough explanation of the findings of this analysis.

### Building Scripts for Question 2:

1) Ensure all of the above packages are installed on your local machine.

2) Ensure all of the scripts and datasets in this repository are cloned to your local machine.

3) Run `Likes_to_Views_ETL.ipynb` - This file extracts, transforms, and saves data to be used subsequent Jupyter Notebooks.

4) Run `Likes_to_Views_Prelim_Analysis.ipynb` - This file takes a preliminary look at the data through plots and tables. It also saves graphs and necessary data for the next step.

5) Run `Likes_to_Views_Statistical_Analysis.ipynb` - This file performs non-parametric statistical tests for question 2.


## Contributors:
- Kaveh Alemi, kalemi@sfu.ca
- Michael Thai, mta24@sfu.ca