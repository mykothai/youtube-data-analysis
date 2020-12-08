# CMPT 353 Final Project: The Pandemic and Trending YouTube Videos

## Project Description: 
In this paper, we will investigate and explore trending YouTube video categories in Canada, Great Britain, and the USA during the years of 2018 and 2020. We have designed our analysis such that the 2018 data represents a timeframe not experiencing a pandemic, and conversely, the 2020 data representing a timeframe undergoing an active pandemic. Our analysis will aim to answer the following two questions:

1) Has the frequency and view count of trending YouTube categories significantly changed in 2018 versus 2020 in Canada, Great Britain, and the USA?

2) Has the ratio of likes versus views of trending YouTube categories changed significantly in 2018 versus 2020 in Canada, Great Britain, and the USA?

Our two datasets were sourced from the following kaggle datasets:

* **2020 Daily Trending Youtube Videos:**     https://www.kaggle.com/rsrishav/youtube-trending-video-dataset
* **2018 Daily Trending Youtube Videos:**     https://www.kaggle.com/datasnaek/youtube-new


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

3) The script corresponding to question 1, 'Trending_Video_Views_Analysis.py', is expandable to any of the following three geographical regions: Canada, Great Britain, USA. Please refer to the commands below to build and run this script.

* To run the analysis for Canada: `Python3 Trending_Video_Views_Analysis.py CA`
* To run the analysis for Great Britain: `Python3 Trending_Video_Views_Analysis.py GB`
* To run the analysis for USA: `Python3 Trending_Video_Views_Analysis.py US`

NOTE: The analysis can also be carried out in a Jupyter Notebook for each of the above Python scripts.

4) Once you have executed the above commands, the output of the analysis corresponding to the country inputted to the script will be presented on the terminal. Relevant plots will be saved as PNG files to your computers working directory.

### Building Scripts for Question 2:

1) Ensure all of the above packages are installed on your local machine.

2) Ensure all of the scripts and datasets in this repository are cloned to your local machine.

3) First Run `Likes_to_Views_ETL.ipynb` in a jupyter environment - This file extracts, transforms, and saves data to be used subsequent Jupyter Notebooks.

4) Then Run `Likes_to_Views_Prelim_Analysis.ipynb` - This file takes a preliminary look at the data through plots and tables. It also saves graphs and necessary data for the next step.

5) Run `Likes_to_Views_Statistical_Analysis.ipynb` - This file performs non-parametric statistical tests.


**Refer to our paper for a thorough explanation of the findings of this analysis.**

## Contributors:
- Kaveh Alemi, kalemi@sfu.ca
- Michael Thai, mta24@sfu.ca