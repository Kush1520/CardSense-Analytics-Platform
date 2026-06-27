# CardSense Analytics Platform

An end-to-end Financial Analytics Platform that transforms raw banking and transaction data into actionable business intelligence using Google BigQuery, SQL, Python, Machine Learning, and Tableau.

The project focuses on customer analytics, merchant intelligence, fraud detection, customer engagement analysis, and cross-sell opportunity identification through an automated analytics pipeline.

---

# Dashboard Preview

<p align="center">
  <img src="Dashboard/CardSense%20Analytics%20Dashboard.png" width="100%">
</p>

---

# Project Overview

CardSense Analytics Platform is designed to simulate a real-world banking analytics system.

The project processes raw financial datasets, performs large-scale SQL analysis in Google BigQuery, generates analytical datasets, trains a fraud detection model using Machine Learning, and visualizes business insights through an interactive Tableau dashboard.

The workflow closely resembles how analytics teams operate in fintech companies such as American Express, Visa, Mastercard, Capital One, and JPMorgan.

---

# Project Architecture

```
Raw Financial Datasets
            │
            ▼
Google BigQuery
(SQL Analytics)
            │
            ▼
Feature Engineering
(SQL + Python)
            │
            ▼
Machine Learning
Fraud Detection
            │
            ▼
Business Summary Tables
            │
            ▼
Tableau Dashboard
            │
            ▼
Business Insights
```

---

# Technologies Used

| Category | Technologies |
|-----------|-------------|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Database | Google BigQuery |
| Query Language | SQL |
| Visualization | Tableau |
| Notebook | Jupyter |
| Version Control | Git, GitHub |

---

# Repository Structure

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
├── model
│   ├── train_model.py
│   ├── predict.py
│   ├── inspect_predictions.py
│   └── requirements.txt
│
├── notebooks
│
├── sql
│
├── README.md
└── requirements.txt
```

---

# Methodology

## Data Collection

Multiple banking datasets containing customer, transaction, merchant, marketing, and fraud information were collected.

---

## Data Cleaning

The datasets were cleaned using Python.

Cleaning steps included:

- Missing value treatment
- Duplicate removal
- Feature validation
- Data type correction
- Outlier inspection

---

## SQL Analytics

Google BigQuery was used to perform large-scale analytical queries.

Generated analytical tables include:

- Customer Segments
- Executive KPIs
- Merchant Summary
- Customer Engagement Summary
- Fraud Summary
- Cross Sell Candidates
- Fraud Predictions

---

## Feature Engineering

Business features were created to improve analytics.

Examples include:

- Customer Engagement Score
- Credit Utilization
- Customer Segments
- Merchant Performance
- Fraud Probability
- Executive KPIs

---

## Machine Learning

A fraud detection model was developed using Python and Scikit-learn.

Pipeline:

- Data preprocessing
- Feature scaling
- Train/Test split
- Model training
- Fraud prediction
- Probability estimation

Predictions were exported for visualization in Tableau.

---

# Dashboard Analytics

The Tableau dashboard is divided into multiple business sections.

## Executive KPIs

Displays overall banking performance.

Metrics include:

- Total Customers
- Total Spend
- Average Spend
- Average Utilization
- Churned Customers

---

## Customer Insights

Business analysis includes:

- Customer Segmentation
- Customer Portfolio Distribution
- Engagement Analysis
- Spending Behavior
- Credit Utilization

Visualizations:

- Bar Charts
- Treemaps
- Scatter Plots

---

## Merchant Insights

Merchant performance is analyzed using:

- Merchant Categories
- Packed Bubble Charts
- Category Comparison
- Cross Sell Opportunities

---

## Fraud Analytics

Fraud analysis includes:

- Fraud Probability
- High Risk Transactions
- Prediction Summary
- Fraud Dashboard

---

# Business Insights Generated

The project reveals several valuable business insights.

Customer Insights

- Regular customers contribute the largest customer base.
- High-value customers generate maximum revenue.
- Customer engagement is positively associated with spending.

Merchant Insights

- Certain merchant categories consistently outperform others.
- Spending distribution varies significantly by merchant type.

Fraud Insights

- Machine Learning successfully identifies suspicious transactions.
- High-risk customers can be monitored proactively.

Cross Sell Insights

- Customers with high engagement and strong spending behavior are ideal candidates for cross-selling campaigns.

---

# Skills Demonstrated

- Data Analytics
- SQL
- Google BigQuery
- Machine Learning
- Feature Engineering
- Data Cleaning
- Customer Analytics
- Fraud Detection
- Business Intelligence
- Tableau Dashboard Development
- Data Visualization
- Git
- GitHub

---

# Future Improvements

- Docker Deployment
- AWS Cloud Deployment
- Apache Airflow Pipelines
- Real-Time Streaming Analytics
- Customer Lifetime Value Prediction
- Recommendation System
- REST API Integration
- Interactive Web Dashboard

---

# Author

**Krrish Gagneja**

GitHub

https://github.com/Kush1520/CardSense-Analytics-Platform
