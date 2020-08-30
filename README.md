# Used Car Market Using Machine Learning

## Abstract
Cars.com (Cars) has a huge selection of user and dealrship submitted cars for sale, this as well as it's ease of scrapping made it the ideal candidit for data collection.
Goal of this Machine Learning Project is simply:
* Train a model to predict the price of a car.

## Results
* a number of models predicted the price of car pretty well on unseen data compared to the average. Random Forest Regressor preformed the best with RMSE of $9,647.56 compared the RMSE of average $17,256.50

## Data
Cars was scraped using 20 scrapper programs running in parrlel and stored locally on a M.2 Form Factor. 
Each datapoint represents a unique car being sold in the U.S. Because of scaling issue and limited hardware, 50,000 of the total data collected were randomly chosen for model building.

## Model
The general Idea is to build a model that returns a price for car given inputed feature information. Data was test on a few different type of machine learning models. Random Forest Regressor as well as Gradient Boosting preformed around the same RMSE when compared to the baseline RMSE (average).

### Output
The output of the machine learning model is simple, prices can range from $1.00 - $100,000,000.00

### Features
* Year
* Make
* Model
* Milage
* City
* State
* Body Style
