# Interim Report: Insurance Risk Analytics & Predictive Modeling

## AlphaCare Insurance Solutions (ACIS)

### Week 3 Challenge

---

# 1. Executive Summary

This project focuses on exploratory insurance risk analytics for AlphaCare Insurance Solutions (ACIS), using historical insurance policy and claims data to identify profitability patterns, high-risk customer segments, and opportunities for data-driven pricing optimization.

The interim phase of the project focused on:
- setting up a reproducible analytics environment
- conducting exploratory data analysis (EDA)
- identifying initial insurance risk patterns
- implementing Data Version Control (DVC) for dataset reproducibility

The analysis revealed notable differences in insurance risk across provinces, vehicle categories, and customer groups, highlighting opportunities for improved customer segmentation and risk-based pricing.

---

# 2. Business Understanding

AlphaCare Insurance Solutions (ACIS) aims to optimize its marketing strategy and insurance pricing framework using historical claims data.

The key business objectives include:
- identifying low-risk customer segments
- improving pricing accuracy
- reducing portfolio risk
- enhancing profitability
- supporting evidence-based decision-making

Insurance profitability is strongly influenced by claims behavior, premium collection, customer risk characteristics, and geographic trends. Therefore, exploratory analysis was conducted to better understand the structure and behavior of the portfolio.

---

# 3. Project Environment & Repository Setup

A structured analytics environment was created using:
- Git and GitHub for version control
- Jupyter Notebook for analysis
- Python for data analytics
- GitHub Actions structure for CI/CD preparation
- DVC for dataset versioning and reproducibility

The repository was organized into modular folders for notebooks, source code, reports, tests, and data management.

---

# 4. Exploratory Data Analysis (EDA)

## 4.1 Data Overview

The dataset contains customer, vehicle, policy, premium, and claims information used to evaluate insurance risk and profitability patterns.

Key variables analyzed include:
- TotalPremium
- TotalClaims
- Province
- VehicleType
- Gender
- RiskScore
- Vehicle Value Estimates
- Claim indicators

---

## 4.2 Data Quality Assessment

Data quality checks were performed to identify:
- missing values
- duplicate records
- incorrect data types
- outliers

The analysis revealed the presence of skewed financial variables and several high-value outliers in claims and vehicle valuation fields.

---

## 4.3 Insurance Risk Metrics

Two major business metrics were calculated:

### Loss Ratio

Loss Ratio = TotalClaims / TotalPremium

This metric measures portfolio profitability and insurance risk.

### Margin

Margin = TotalPremium − TotalClaims

This metric evaluates the profit contribution of individual policies.

---

## 4.4 Key EDA Findings

### Geographic Risk Differences

The analysis showed that insurance risk varies across provinces, with some regions exhibiting significantly higher loss ratios than others.

This suggests opportunities for:
- regional pricing adjustments
- location-based segmentation
- targeted risk mitigation

### Vehicle Risk Patterns

Certain vehicle categories and vehicle makes contributed disproportionately to total claims, indicating varying levels of insurance exposure across vehicle segments.

### Claims Distribution

Claims and premium distributions were highly right-skewed, with a relatively small number of policies contributing to large claim amounts.

### Temporal Trends

Monthly premium and claims trends revealed fluctuations over time, suggesting possible seasonal or operational influences on insurance activity.

### Correlation Analysis

Correlation analysis identified relationships between premiums, claims, profitability metrics, and customer risk indicators.

---

# 5. Visual Analytics

Several visualizations were developed to communicate portfolio risk patterns, including:
- Loss Ratio by Province
- Loss Ratio by Gender
- Vehicle Risk Analysis
- Claims Distribution
- Correlation Heatmaps
- Premium vs Claims Scatterplots
- Monthly Claims Trends

These visualizations support business interpretation and risk segmentation decisions.

---

# 6. Data Version Control (DVC)

DVC was implemented to establish a reproducible and auditable data pipeline.

The workflow included:
- DVC initialization
- local DVC storage configuration
- dataset tracking
- versioning of raw and cleaned datasets
- reproducible data management

Two dataset versions were tracked:
1. Raw insurance dataset
2. Cleaned insurance dataset

This setup improves:
- reproducibility
- collaboration
- auditability
- experiment tracking

---

# 7. Challenges Encountered

Some challenges encountered during the interim phase included:
- environment configuration issues
- dataset column naming inconsistencies
- DVC setup and environment synchronization
- handling skewed insurance variables and outliers

These issues were resolved through iterative debugging and workflow refinement.

---

# 8. Next Steps

The next phase of the project will focus on:
- hypothesis testing
- statistical validation of risk factors
- predictive modeling
- premium optimization
- model evaluation
- feature importance analysis using SHAP/LIME

The goal is to develop a data-driven pricing framework capable of predicting insurance risk and supporting strategic pricing decisions.

---

# 9. Conclusion

The interim phase established a strong analytical and technical foundation for the project.

The exploratory analysis provided meaningful insights into portfolio profitability, customer risk segmentation, and insurance claims behavior, while DVC implementation ensured reproducible data management practices.

These findings will guide the next stages of statistical testing and predictive modeling.