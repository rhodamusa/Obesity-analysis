About the Dataset
The dataset used for this analysis, titled "Estimation of Obesity Levels Based on Eating Habits and Physical Condition", is from Kaggle.com. It contains 2,111 records and 17 features, profiling individuals from Mexico, Peru, and Colombia. The dataset covers a variety of factors influencing obesity, from dietary habits and physical activity to lifestyle and personal history.
Key Features:
Gender — Male or Female
Age — Age in years
Height — Height in meters
Weight — Weight in kilograms
family_history_with_overweight — Family history of overweight (yes/no)
FAVC — Frequent consumption of high-calorie foods (yes/no)
FCVC — Frequency of vegetable consumption (1–3 scale)
NCP — Number of main meals per day
CAEC — Snacking frequency (Never, Sometimes, Frequently, Always)
SMOKE — Smoking habit (yes/no)
CH2O — Daily water intake (1–3 scale)
SCC — Monitoring of calorie consumption (yes/no)
FAF — Physical activity frequency (0–3 scale)
TUE — Daily technology usage (0–3 scale)
CALC — Frequency of alcohol consumption (Never, Sometimes, Frequently, Always)
MTRANS — Primary transportation mode (Automobile, Bike, Motorbike, Public Transport, Walking)
NObeyesdad — Obesity level (ranging from Insufficient Weight to Obesity Type III)



Data Preparation and Analysis
I used Python with Pandas, Numpy, Statsmodels, and Scikit-learn for this analysis.

Here’s what I did:
Cleaned the Data: Removed duplicates and ensured data consistency.

Generated Descriptive Statistics: Summarized distributions for numerical features.

Explored Age and Obesity Trends: Grouped by obesity level and calculated ages to observe patterns.

Converted Obesity Levels to Numeric Values: Enabled easier analysis and modeling. 

Encoded Categorical Variables: Translated lifestyle factors into numeric form for modeling using label encoder

Trained a Random Forest Model: Identified key features influencing obesity and their importance scores.

Explored Family History Connections: Analyzed how having a family history of obesity relates to personal weight status.

Case Study Objective
The aim of this project is to explore how lifestyle choices influence obesity levels. Using data on diet, physical activity, and personal habits, I wanted to answer key questions that can help healthcare professionals, policymakers, and individuals make more informed decisions.


Key Questions I Explored:
How does age affect obesity?

Does physical activity frequency impact obesity, and does it differ by gender?

How strong is the relationship between family history and personal obesity risk?

Does alcohol have an effect on obesity?

Why It Matters
By answering these questions, this project aims to provide actionable insights that can support obesity prevention programs and help people make healthier lifestyle choices. After all, just like in agriculture — where timely knowledge can help a farmer harvest more — the right information can help all of us live healthier, longer lives.
