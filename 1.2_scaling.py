#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 16:56:52 2022

@author: Jo
"""




# Compare the effect of different scalers on data with outliers
# https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-auto-examples-preprocessing-plot-all-scaling-py






#%% normalize all features 

# the numerical attributes (still check out what it does exactly)

# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler

# num_pipeline = Pipeline([
        #('imputer', SimpleImputer(strategy="median")), # not needed anymore, this is just an example for a pipeline
        #('attribs_adder', CombinedAttributesAdder()), #  what's this?
        #('std_scaler', StandardScaler()),# this is our normalizer
    #])

# data_transformed = num_pipeline.fit_transform("numerical_data")



