#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:14:57 2022

@author: Jo
"""

#%% call setup file

import runpy
runpy.run_path(path_name = '/My Drive/PISA_Revisited/0_setup.py')

# imports sys, sklearn, numpy, os, matplotlib, pathlib
# checks versions, sets wd, sets random.seed 42, specifies plots
# defines function save_fig()

#%% import additional packages

import pandas as pd

#%% read in data

# read csv file
PISA_raw = pd.read_csv("/Volumes/GoogleDrive/My Drive/PISA_Revisited/data/PISA_student_data.csv")

# renaming relevant columns
PISA_raw.rename(columns = {'PV1READ':'read_score', 'ST004D01T':'female'}, inplace = True)

# save as csv
PISA_raw.to_csv("data/PISA_raw")

# read in after first run - already renamed
PISA_raw = pd.read_csv("/Volumes/GoogleDrive/My Drive/PISA_Revisited/data/PISA_raw")


#%% create tryout samples (created as split of raw data)

# create a random sample for code developing
PISA_raw_1000 = PISA_raw.sample(1000)

# create a smaller random sample for code developing
PISA_raw_100 = PISA_raw.sample(100)

# create even smaller sample
PISA_raw_10 = PISA_raw.sample(10)

# check if sampling worked out
len(PISA_raw_1000)
len(PISA_raw_100)
len(PISA_raw_10)

# saving samples as csv
PISA_raw_1000.to_csv("data/PISA_raw_1000.csv")
PISA_raw_100.to_csv("data/PISA_raw_100.csv")
PISA_raw_10.to_csv("data/PISA_raw_10.csv")

#%% explore sample

# check datatypes
PISA_raw_10.info()

# generate description of variables
PISA_raw_10.describe()

# plot variables (not really possible with our over 1000 variables...)
# PISA_sample_100.hist(bins=50, figsize=(20,15))
# plt.show()

# --> plot variables: select random features
PISA_plot_sample = PISA_raw_100.sample(n=10,axis='columns')
PISA_plot_sample.head()

# plot only those
PISA_plot_sample.hist(bins=50, figsize=(20,15))
save_fig("distribution_examples")
plt.show()

# exploring the dependent variable "reading skills"
PISA_raw_1000.read_score.mean()
PISA_raw_1000[["read_score", "female"]].groupby("female").mean()

PISA_raw_1000.hist(column='read_score',bins=50)
plt.axvline(x=456.1, color='red', linestyle='--')
save_fig("read_score")
plt.show()


#%% handle students without reading score (for now drop them)

PISA_raw_100 = pd.read_csv("/Volumes/GoogleDrive/My Drive/PISA_Revisited/data/PISA_sample_100.csv")

medians = PISA_raw_100.median()
print(medians)

# see missingness of reading score (read_score) -> 0.8%
print(Total_NaN_count_rel[Total_NaN_count_rel["variable"] == "PV9READ"])

# look at observations that don't have read_score (still to do)
# students_without_reading_score = PISA_raw[....]

# drop students with NaN in reading score. inplace replaces the old data frame with the smaller, new one
PISA_raw = PISA_raw.dropna(subset=['read_score'], inplace=True)


#%% handle string columns

# drop string variables
# PISA_raw_100 = PISA_raw_100.drop(columns = ["VER_DAT", "CNT", "CYC", "STRATUM"])

# drop string variables for the whole dataset:
PISA_raw = PISA_raw.drop(columns = ["VER_DAT", "CNT", "CYC", "STRATUM"])

# from the codebook:
# "VER_DAT" is only a date
# "CNT" is only a country code that is also represented in the country ID
# "CYC" is "PISA Assessment Cycle (2 digits + 2 character Assessment type - MS/FT)"
# "STRATUM" is "Stratum ID 7-character (cnt + region ID + original stratum ID)"
# -> can all be dropped

#%% handle NAN's in other columns

# detect missing values in the given object, returning a boolean same-sized 
# object indicating if the values are NA. Missing values gets mapped to 
# True and non-missing value gets mapped to False.
PISA_raw_100.isnull()

# sum up how many values are NaN's
NaN_count = PISA_raw_100.isnull().sum()
# relative frequency
NaN_count_rel = PISA_raw_100.isnull().sum()/len(PISA_raw_100)*100
# descending order
NaN_count_rel.sort_values(ascending=False)

# Save as csv to export and use side by side with codebook
NaN_count_rel.to_csv('data/NA_Values.csv') 

# Same steps for whole dataset
Total_NaN_count_rel = PISA_raw.isnull().sum()/len(PISA_raw)*100
Total_NaN_count_rel = Total_NaN_count_rel.sort_values(ascending=False)

# create data frame with variable and missingness
Total_NaN_count_rel = Total_NaN_count_rel.reset_index(level=0)
Total_NaN_count_rel = pd.DataFrame(Total_NaN_count_rel)
Total_NaN_count_rel.columns = ['variable', 'missingness']

Total_NaN_count_rel.to_csv('data/Total_NA_Values.csv') 


#drop columns that have more than 75% NAN's

# see which variables have over 75% missingness
observations_to_drop = Total_NaN_count_rel[Total_NaN_count_rel["missingness"] > 75]
# create an array with the variable names with missingness over 75%
observation_names_to_drop = observations_to_drop["variable"]
len(observation_names_to_drop)
print(observation_names_to_drop)
# convert to array
observation_names_to_drop.array

# drop columns with more than 75% missingness
PISA_raw = PISA_raw.drop(columns = [observation_names_to_drop])

PISA_raw = PISA_raw.drop([observation_names_to_drop], axis=1)



#%% imputing for NaN's

# works only with numerical data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy = "median")
imputer.fit(PISA_sample_100)

imputer.statistics_
PISA_sample_100.median().values

X = imputer.transform(PISA_sample_100)

# This doesn't work yet but I don't know why
# PISA_sample_transformed = pd.DataFrame(X, columns = PISA_sample_100.comlumns, index = PISA_sample_100.index)

#%% Data Types




#%% any other preprocessing (pattern missingness? etc.)



#%% normalize all features and build a pipeline for preprocessing 

# the numerical attributes (still check out what it does exactly)

# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler

# num_pipeline = Pipeline([
        #('imputer', SimpleImputer(strategy="median")), # what's this?
        #('attribs_adder', CombinedAttributesAdder()), #  what's this?
        #('std_scaler', StandardScaler()),# this is our normalizer
    #])

# data_transformed = num_pipeline.fit_transform("numerical_data")



