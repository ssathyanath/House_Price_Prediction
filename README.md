# House Price Prediction

**Topic:** Predict House prices in King County based on previous house sales data  

**Data Source:**  

- House Sales Data for King County from Kaggle [Link to Data](https://www.kaggle.com/achyutanandaparida/dataset%20from%20%20house%20sales%20in%20king%20county,%20usa)  
- Population and City info by Zipcode from unitedstateszipcodes.org [Link to Data](https://www.unitedstateszipcodes.org/wa/#zips-list)

**Technologies, languages, tools:**  
Python: Pandas, Numpy, SKlearn, XGBoost, Pickle, Matplotlib, SQLlite3, SQLalchemy, Flask  
SQLLite Database  
HTML, CSS  
Machine Learning Algorithm: Random Forest, XGBoost, Random Forest, Kmean Clustering  

**Data Preprocessing:**  

- Downloaded house sales dataset as csv from Kaggel
- Downloaded population and city details dataset as csv from unitedstateszipcodes.org
- Created tables in database(SQLlite) and uploaded data
- Read tables into Pandas using SQLAlchemy
- Performed data cleansing as needed (removing null rows, droping columns not needed)
- Pearsons Correlation Coefficient was used to determine the correlation between the price and other columns
- Select Kbest score was used to determine the significance of each column to the price
- The results were plotted as a bar graph and the results were similar
- Features with correlation greater that 0.3 were selected for prediction

**Model Selection:**  

* X dataset was created using the features selected in the feature selection process
* Y dataset was created using the price column
* The dataset was split into test and train datasets using train_test_split from sklearn
* The test and trained datasets were then scaled using StandardScaler from sklearn
* Three models listed below were trained and tested and the root mean square and R Squared value was calculated
    - Randon Forest Regression
    - XG Boost Regression
    - Linear Regression
* The predicted values were plotted against actuals
* Based on the results, the XGBoost model had the best results for Root mean squared and R Squared values and was choosen
* Trained model is downloaded as a pickle file  

**Model Predictions**  

* A flask app is created and the trained model and standard scalar models are loaded
* The values required for house price prediction are captured from the user using HTML templates
* The city_rank is calculated based on the primary city
* A dataframe is created with the available values for features entered and null values for features that were not entered
* The housedata is filtered for the city that the user entered
* A for loop was created to loop through columns that do not have values and the median value based on the filtered dataset is populated for these columns
* The predicted dataframe is scaled using previous scalar model
* The house price is then predicted using the previously trained model
* The perdicted results are then displayed to the users using HTML
