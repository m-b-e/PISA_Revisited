# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:42:21 2022

@author: Jo&Anna

"""

#%% model 1 poly-ridge degree 2


section 1



#%% model 2 poly-ridge degree 3


section 2



#%% model 3 RandomForest

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

# n_estimators: number of trees in the forest. default = 100
# max_features: number of features to consider when looking for the best split. default = 

param_grid_1 = [
    {"n_estimators": [50, 100, 150], "max_features": [50, 100, 205]},
  # {"bootstrap": [false], "n_estimators": [50, 100, 150], "max_features": [50, 100, 205]}
    ]

forest_reg = RandomForestRegressor()

grid_search = GridSearchCV(forest_reg, param_grid_1, cv=5,
                         scoring="neg_mean_squared_error",
                         return_train_score=True)

# perform grid search with the validdation set 2
grid_search.fit(X_val_2, y_val_2)

# get best parameters
grid_search.best_params_
# result: {'max_features': 50, 'n_estimators': 150} -> score = 72.73 which is worse than with default parameters

# look at evaluation scores of all parameter combinations
cvres = grid_search.cv_results_
for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
    print(np.sqrt(-mean_score), params)
    
#############################

# second try  with less features and more estimators (= number of trees) because both values were on the edge of the grid search
param_grid_2 = [
    {"n_estimators": [200, 300], "max_features": [10, 20]},
  # {"bootstrap": [false], "n_estimators": [50, 100, 150], "max_features": [50, 100, 205]}
    ]

forest_reg = RandomForestRegressor()
grid_search = GridSearchCV(forest_reg, param_grid_2, cv=5,
                         scoring="neg_mean_squared_error",
                         return_train_score=True)

# perform grid search with the validdation set 2
grid_search.fit(X_val_2, y_val_2)

# get best parameters
grid_search.best_params_
# result: {'max_features': 20, 'n_estimators': 300} -> score = 73.0656116 which is worse than with default parameters

# look at evaluation scores of all parameter combinations
cvres = grid_search.cv_results_
for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
    print(np.sqrt(-mean_score), params)

##############################

# third try  with more features and more estimators (= number of trees) because both values were on the edge of the grid search
param_grid_3 = [
    {"n_estimators": [300], "max_features": [20, 30, 40, 50]},
  # {"bootstrap": [false], "n_estimators": [50, 100, 150], "max_features": [50, 100, 205]}
    ]

forest_reg = RandomForestRegressor()
grid_search = GridSearchCV(forest_reg, param_grid_3, cv=5,
                         scoring="neg_mean_squared_error",
                         return_train_score=True)

# perform grid search with the validdation set 2
grid_search.fit(X_val_2, y_val_2)

# get best parameters
grid_search.best_params_
# result: {'max_features': 40, 'n_estimators': 300} -> score = 72.61856548195976 which is worse than with default parameters

# look at evaluation scores of all parameter combinations
cvres = grid_search.cv_results_
for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
    print(np.sqrt(-mean_score), params)



#%% model 4 ExtraTrees


section 4