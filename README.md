# CardSense Analytics Platform

An end-to-end financial analytics platform that combines BigQuery, SQL, Python, Machine Learning, and Tableau to generate customer intelligence, merchant insights, fraud detection, and cross-sell recommendations from large-scale transaction data.

The project demonstrates a complete analytics pipeline starting from raw data ingestion to interactive dashboards and predictive analytics.

Repository Structure

```
CardSense-Analytics-Platform
│
├── BigQuery_Files
│   ├── Cross Sell Candidates.csv
│   ├── Customer Segments.csv
│   ├── Engagement Summary.csv
│   ├── Executive KPIs.csv
│   ├── Fraud Predictions.csv
│   ├── Fraud Summary.csv
│   └── Merchant Summary.csv
│
├── Dashboard
│   ├── CardSense Analytics Dashboard.png
│   ├── Customer_segments_preview.png
│   ├── Customer_engagement_preview.png
│   ├── High_value_customer_preview.png
│   ├── Merchant_category_preview.png
│   └── Merchant_insights_preview.png
│
├── notebooks
│
├── sql
│
├── model
│   ├── train_model.py
│   ├── predict.py
│   └── inspect_predictions.py
│
├── README.md
└── requirements.txt
```

Project Architecture

Raw Datasets

↓

Google BigQuery

↓

SQL Feature Engineering

↓

Python Data Processing

↓

Machine Learning Fraud Detection

↓

Business Aggregations

↓

Tableau Dashboard

↓

Business Insights

Technology Stack

Python

Pandas

NumPy

Scikit-learn

Google BigQuery

SQL

Tableau

Jupyter Notebook

Git

GitHub

Business Problems Solved

Customer segmentation using spending behavior

Customer engagement analysis

Merchant category performance analysis

Cross-sell opportunity identification

High-value customer discovery

Credit utilization analysis

Fraud prediction using machine learning

Executive KPI reporting

Project Workflow

Data Collection

Transaction, customer, merchant, marketing, and fraud datasets were collected from multiple structured sources.

Data Cleaning

Handled missing values

Removed duplicates

Standardized categorical variables

Created analytical features

Validated data quality

Feature Engineering

Created customer engagement score

Calculated utilization ratio

Generated customer segments

Prepared merchant-level aggregations

Computed executive KPIs

Fraud probability scoring

BigQuery SQL Analytics

SQL was used extensively to create analytical datasets.

Customer Segmentation

Merchant Analytics

Fraud Summary

Cross Sell Candidates

Executive KPIs

Customer Engagement Summary

Machine Learning

A supervised machine learning model was trained to identify potentially fraudulent transactions.

Model Pipeline

Data preprocessing

Feature scaling

Train-test split

Model training

Prediction generation

Fraud probability scoring

Exporting prediction datasets

Tableau Dashboard

The dashboard provides interactive business intelligence across multiple business domains.

Dashboard Sections

Executive KPIs

Customer Insights

Merchant Insights

Customer Engagement Analysis

Cross Sell Opportunities

Fraud Detection

Dashboard Features

Interactive filters

Customer drill-down

Merchant category comparison

Bubble charts

Treemaps

Scatter plots

Bar charts

KPI cards

Dashboard Preview

![Dashboard](Dashboard/CardSense%20Analytics%20Dashboard.png)

Analytics Performed

Customer Analytics

Customer segmentation

Average spend analysis

Customer portfolio distribution

Engagement score analysis

Credit utilization analysis

Merchant Analytics

Merchant category performance

Transaction volume analysis

Packed bubble visualization

Revenue contribution analysis

Fraud Analytics

Fraud probability prediction

High-risk transaction identification

Fraud summary generation

Cross Sell Analytics

Eligible customer identification

Opportunity ranking

High-value customer discovery

Executive KPIs

Total Customers

Total Spend

Average Spend

Average Utilization

Churned Customers

Customer Engagement

Business Insights Generated

Regular customers represent the largest customer segment.

High-value customers provide the highest revenue opportunities.

Customer engagement has a positive relationship with spending.

Several merchant categories outperform others in transaction volume.

Machine learning successfully identifies high-risk transactions.

Cross-sell recommendations enable targeted marketing campaigns.

Files Generated Using SQL

Customer Segments.csv

Engagement Summary.csv

Merchant Summary.csv

Cross Sell Candidates.csv

Executive KPIs.csv

Fraud Summary.csv

Fraud Predictions.csv

Future Improvements

Real-time streaming analytics

Cloud deployment on AWS

Apache Airflow pipeline

Docker containerization

Power BI integration

Customer lifetime value prediction

Recommendation engine

Interactive web application

Skills Demonstrated

Data Analytics

SQL

BigQuery

Machine Learning

Python

Feature Engineering

Business Intelligence

Dashboard Design

Fraud Analytics

Customer Analytics

Data Visualization

Git Version Control

Author

Krrish Gagneja

GitHub

https://github.com/Kush1520/CardSense-Analytics-Platform
