# Tanzanian Water Well Classification

An entry to the Classification Challange Competition: https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/

Andrew Muller

## Business Case

Using data from Taarifa and the Tanzanian Ministry of Water, I will predict the functional status of water wells. Wells are classified as either functional, not functional, or functional but in need of repair. Data on the management, location, and use of the pumps is provided in order to make these predictions. As stated by the competition rules, accuracy will be used as the measure of success.

## Exploratory Data Analysis

The provided data has already been broken up into test and train data, with only the independent variables given for the train data, so its predictions can be submitted to the contest.

The data has 39 indepentent variables, but many of them are near copies of each other. 16 are immediately identifiable as useless, and are removed. The others are split into categorical and continuous variables to be investigated further.

A look at the 19 categorical variables reveals that many of them have thousands of categories. This is clearly useless, so categories with less than 1% representation in the overall dataset are binned into an 'other' category. Reducing the number of features related to the pump's geographical location leaves 13 categorical variables. Creating dummy features for these categories leaves 100 total independent variables in the data.

The continuous variables had some missing data that needed to be dealt with. In order to run KNN imputation on the dataset, the missing data was changed to nan values and the remaining data was min-max scaled. Carrying out the KNN imputation leaves 100 columns of data scaled from 0 to 1, which is then combined back with the depentent variable to create our cleaned data.

The same process is applied to the submission data: removing unneeded features, changing unrepresented categories to 'other', creating dummy columns, scaling, and imputing missing values. This data is then ready to be used on the same models that we create with our test data.

## Baseline Models

Train data is split from our cleaned data and baseline (default parameters) models are created using many different model types. Test data is then predicted on these models, and the accuracy is used to determine which models are best.

- Logistic Regression: 73.40%
- K Nearest Neighbors: 77.98%
- Naive Bayes: 54.23%
- Decision Tree: 74.64%
- Bagged Trees: 78.38%
- Random Forest: 79.30%
- Adaboost: 72.74%
- Gradient Boost: 74.99%
- XGBoost: 74.42%
- Support Vector Machines: 77.04%

Of these, hyperparameter tuning will be performed on KNN, Random Forest, XGBoost, and SVM. Bagging will also be tested on each of these models.

## Hyperparameter Tuning

GridSearchCV was used on on the KNN, Random Forest, XGBoost, and SVM models. A second pass was also made, narrowing in on the best paremeters. XGBoost saw the most improvement upon tuning, but KNN and SVM have few hyperparameters to tune, and saw little improvement. Bagging the models slightly improved the Random Forest and SVM models, but decreased the accuracy of the KNN and XGBost models. The accuracy of these improved models was measured against the same test data as the baseline.

- KNN: 78.57% (improvement of 0.59)
- Random Forest: 80.06% (improvement of 0.76)
- XGBoost: 80.25% (improvement of 5.83)
- SVM: 77.70% (improvement of 0.66)

## Final Models

Using the best hyperparameters resulting from the grid search, the models are again fit, this time from the entire dataset, not just the 75% declared the train data. This is because the entire test set is now to be treated as the train set, and the submission data as the test set. Predictions are then run on the submission data, and they are submitted to the contest. Only the accuracy of each submission is returned.

- KNN: 79.99%
- Random Forest: 81.49%
- XGBoost: 81.50%
- SVM: 78.04%

## Conclusions

XGBoost performed the best of any model, although it only barely beat out the Random Forest. The comparatively poor performance of the KNN and SVM models indicates that the data is not easily seperable, as these models are both distance-based.

A highest accuracy of 81.50% ends up at a rank of 1303 of 10458.

Random Forests has less false positives than XGBoost, and so is likely better in real life situations.

## Future Improvements

When cleaning the data, the scaling and imputing was done before the train test split. This would be intended for the submission models, but caused data leakage in the testing phases, and may have lead to some sub-optimal parameters used. This could be fixed.

Much data was lost when the excess number of reducing categories. Given more time or processing power, less categories should be removed, which could lead to more accurate results.

More grid searches could be run on the XGBoost model to improve its performance. It is more responsive to tuning than the other models, meaning it has more room for improvement.

If the results of the submission data are provided, the recal and precision of the models can be determined, which could lead to discovering where the models are wrongly predicting, and therefore what could be improved.
