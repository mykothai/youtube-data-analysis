# CMPT 353 Final Project: The Pandemic and Trending YouTube Videos

###### Project Description: 
We interested in the correlation between Covid-19 and the properties of Youtube trending videos. Our analysis is based on the following datasets:

- 2020 Daily Trending Youtube Videos      https://www.kaggle.com/rsrishav/youtube-trending-video-dataset
- 2018 Daily Trending Youtube Videos      https://www.kaggle.com/datasnaek/youtube-new
- COVID-19 Daily Infections               https://ourworldindata.org/covid-cases

The main questions we are want to answer from this data are:

1. Has COVID-19 affected Youtube trending videos in Canada, USA, and Great Britain?
We will look at the number of trending video in each video category for two groups 
    1. Before the COVID-19 pandemic (year of 2018)
    2. During COVID-19 pandemic (year of 2020)

2. Has COVID-19 affected the ratio of likes versus views for the top trending videos in Canada, USA, and Great Britain?
We compare the ratio of likes versus views for the top trending videos in 2018 and 2020 and perform statistical analysis
to see if there is any significance.


###### Required Libraries: 
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from time import sleep
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import sys

###### Building the Project: 
This project revolves around the above two questions, therefore, there are two parts to our analysis where each corresponds to each of these questions. Please see below on instructions on how to build these scripts.

Question 1:

1) Ensure all of the above packages are installed on your local machine.
2) Ensure all of the scripts and datasets in this repository are cloned to your local machine.
3) The script corresponding to question 1, 'Trending_Video_Views_Analysis.py', is expandable to any of the following three countries of your choice: Canada, Great Britain, USA. Please refer to the commands below to build and run this script.

--> Canada: Python3 Trending_Video_Views_Analysis.py CA
--> Great Britain: Python3 Trending_Video_Views_Analysis.py GB
--> USA: Python3 Trending_Video_Views_Analysis.py US

4) Once you have executed the above commands, the output of the analysis corresponding to the country inputted to the script will be presented on the terminal. Relevant plots will be saved as PNG files to your computers working directory.

Question 2:


###### Contributors:
- Kaveh Alemi, kalemi@sfu.ca
- Michael Thai, mta24@sfu.ca