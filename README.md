# Group Project 4
## <i>A supervised learning model predicting accident prone areas in Victoria.</i>

## Project Overview
 To work cohesively as a team to create a machine learning model that is linked to a front end web application as depicted in the image below: 
<img width="760" alt="image" src="https://github.com/teacher-analyst/project4/assets/130710065/0cca414d-5f6c-44eb-9080-5f5a183161aa">

### Understanding the problem
1. Victorian Police plan for emergency response annually especially around significant public holidays such as easter, christmas and melbourne cup. 
   Which Local Government Areas should the police target their resources? 
2. Examine road crashes data over the past five years to find out: Which factors contribute to car accidents on Victorian roads?
   Which areas are prone to accidents?
3. Can Victorian Police employ a deep learning application to predict Local Government Areas prone to accidents based on specific factors? 

### Requirements
    -   Clean, normalise and standardise data before modelling
    -   Write a python script to initialise, train and evaluate a model with at least 75% accuracy
    -   Optimise and evaluate the model ensuring iterative changes are made to the model
    -   Overall model performance is printed/displayed at the end of the cript
    -   Create a web application that links to the model through an API

## File structure

├──Images\
│  ├──Elbow Curve.png\
│  ├──severity v light condition.png\
│  ├──severity v road geometry.png\
├──Resources\
│  ├──Road_Crashes_for_five_Years_Victoria.csv\
│  ├──crashes_cleaned_df.csv\
├──analysis\
│  ├──data_analysis_graphs.ipynb\
│  ├──dataanalysis_pvalues.ipynb\
├──data cleaning and prep\
│  ├──data_prep.ipynb\
│  ├──output.json\
│  ├──prep_output.ipynb\
├──model\
│  ├──data_modelling.ipynb\
│  ├──deep_learning_model.ipynb\
│  ├──scaler.pkl\
│  ├──tree_model.ipynb\
│  ├──tree_model.sav\
├──static/js\
│  ├──script.js\
├──.gitignore\
├──Form.html\
├──README.md\
├──app.py

## Tools
- Python
- Pandas
- Flask API
- D3 Library
- Javascript
- HTML/CSS
  
***
## Project details

### Data Retrieval & Cleaning 


### Analysis
The numerical variables provided with the data did not contain any meaningful correlations. When running pearson correlation analysis across all combinations of the numerical variables provided, there were no meaningful correlations > 60%. 

We did p-value analysis on various combinations of categorical variables, including Light Condition, Speed Zone, Road Geometry v Severity, or Fatality. The largest p-value we came across was 10^-30, indicating very strong correlations. 

Severity v Light Condition

<img width="503" alt="severity v light condition" src="https://github.com/teacher-analyst/project4/assets/61260651/3d7477de-3627-44f2-ad0a-dbf6bf7e033e">


Severity v Road Geometry

<img width="500" alt="severity v road geometry" src="https://github.com/teacher-analyst/project4/assets/61260651/646a779e-5874-4520-8085-4863093ae851">


These graphs show how severity is correlated with Light Condition and Road Geometry. We have similar graphs for other combinations in analysis/data_analysis_graphs.ipynb

### Model
We initially were hoping to predict a single Local Government Area (LGA), of which there were 87 used within the data. We tried clustering the data, but even up to 87 clusters, there was no elbow for us to hone in on. We changed tack and looked at predicting a larger potential area. 

The supervised learning to predict DEG_URBAN_NAME was very successful for both Tree and Random Forest, although Tree was much better for my computer’s processor. Even with a significantly reduced number of inputs, they were able to achieve over 80% accuracy. However, we learned that no meaningful level of accuracy could be achieved without some geographical data included in the models input. We therefore began including Region Name as input in all our model testing. 

The Neural Network/Deep Learning tests were unsuccessful. We were aiming to predict DEG_URBAN_NAME, which has 7 options, and we have included REGION_NAME in the input data. However, over 50 epochs the accuracy of the models plummeted from their initial 50-60%, down to less than 1%. Nothing we tried showed any promise in salvaging the models. 

Ultimately, we chose the Tree model as it was less taxing on our computers than the Random Forest. 


### Conclusion

***
## Resources and Acknowledgements

