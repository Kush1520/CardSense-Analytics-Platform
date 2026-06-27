# Visa Transaction Intelligence

## Project Overview

Visa Transaction Intelligence is an end-to-end analytics project designed to simulate how financial institutions monitor customer behavior, identify fraud risks, discover cross-selling opportunities, and generate executive-level business insights.

The project integrates Python, Machine Learning, SQL, BigQuery, and Tableau to build a modern banking analytics pipeline.

## Objectives

The primary objectives of this project are:

* Analyze customer spending behavior.
* Segment customers based on engagement and spending patterns.
* Detect potentially fraudulent transactions.
* Identify high-value customers for targeted marketing campaigns.
* Evaluate merchant performance.
* Create executive dashboards for business decision-making.

## Dataset

The project utilizes transaction-level banking datasets containing information such as:

Customer transactions

Transaction amount

Merchant category

Credit utilization

Customer engagement metrics

Marketing campaign response

Fraud labels

## Methodology

### Phase 1: Data Cleaning

Raw datasets were cleaned and standardized using Python.

Data preprocessing included:

Handling missing values

Removing duplicates

Feature normalization

Formatting categorical variables

Generating analytical features

Notebook Used:

02_data_cleaning.ipynb

---

### Phase 2: Customer Intelligence

Customer-level metrics were aggregated to understand spending behavior.

Metrics generated:

Average spend

Credit utilization

Engagement score

Customer count

Churn indicators

Notebook Used:

03_customer360.ipynb

---

### Phase 3: Retail Feature Engineering

Additional business-oriented features were generated.

Examples:

Merchant level summaries

Cross-sell eligibility

Campaign acceptance indicators

Executive KPIs

Notebook Used:

04_retail_features.ipynb

---

### Phase 4: Fraud Detection Model

A supervised machine learning model was trained for fraud detection.

Steps included:

Dataset splitting

Feature selection

Model training

Performance evaluation

Probability estimation

Model File:

fraud_model.pkl

Training Script:

train_model.py

Performance Metrics:

Accuracy

Precision

Recall

F1 Score

Predictions Generated:

Prediction

Fraud Probability

Prediction Script:

predict.py

Generated File:

fraud_predictions.csv

---

### Phase 5: BigQuery Analytics

Analytical marts were created inside Google BigQuery.

SQL queries were written to generate summarized datasets.

Generated Analytics Tables:

customer_segments

executive_kpis

merchant_summary

engagement_summary

fraud_summary

cross_sell_candidates

fraud_predictions

These tables serve as reusable analytical assets for reporting.

---

### Phase 6: Data Export

BigQuery tables were exported as CSV files.

Exported Files:

Customer Segments.csv

Executive KPIs.csv

Merchant Summary.csv

Fraud Summary.csv

Engagement Summary.csv

Cross Sell Candidates.csv

Fraud Predictions.csv

---

### Phase 7: Tableau Visualization

The exported analytical datasets were connected to Tableau Public.

Several dashboards and worksheets were developed.

Executive Dashboard

KPIs displayed:

Total Customers

Total Spend

Average Spend

Average Utilization

Churned Customers

Engagement Score

Customer Intelligence Dashboard

Visualizations:

Customer Segment Distribution

Cross Sell Opportunities

Merchant Analysis

Campaign Acceptance Metrics

Fraud Dashboard

Visualizations:

Fraud Percentage

Fraud Distribution

Fraud Probability Analysis

Fraud Summary

---

## Technologies Used

Python

Pandas

NumPy

Scikit-learn

Jupyter Notebook

Google BigQuery

SQL

Tableau Public

Joblib

## Project Structure

visa-transaction-intelligence/

data/

images/

notebooks/

01_generate_support_tables.ipynb

02_data_cleaning.ipynb

03_customer360.ipynb

04_retail_features.ipynb

05_split_fraud.ipynb

ml/

fraud_model.pkl

train_model.py

predict.py

sql/

tableau/

requirements.txt

README.md

## Key Insights

Customer segmentation enables personalized marketing.

Merchant analysis highlights spending concentration.

Fraud probability scoring helps prioritize investigations.

Cross-sell candidates improve campaign efficiency.

Executive KPIs provide a high-level view of business health.

## Future Enhancements

Real-time fraud monitoring

Cloud deployment

Interactive web dashboards

Model retraining pipeline

Automated ETL workflows

Streaming transaction analytics 

## Conclusion

This project demonstrates a complete financial analytics workflow from raw transaction data to machine learning predictions, cloud-based analytical marts, and executive-level business dashboards. It showcases practical applications of data engineering, fraud detection, customer intelligence, and business visualization techniques commonly used in modern banking and payment ecosystems.
