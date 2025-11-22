# retail-pricing-optimization-engine

This project is a production-style machine learning pricing engine that predicts the optimal selling price for e-commerce products using demand patterns, seasonality, competitor benchmarks, and product attributes.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-success)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-blueviolet)
![Plotly](https://img.shields.io/badge/Plotly-Visualizations-lightgrey)
---

# Project Overview

This dynamic pricing engine converts raw e-commerce data into real-time pricing recommendations.  
The model is trained on the Olist Brazilian E-commerce dataset (120,000+ records) and achieves:

- R² score of 0.99  
- MAE less than 1.0  

The Streamlit application provides:
- Business-friendly input fields  
- Recommended optimal selling price in Indian Rupees (₹)
- Difference compared to the user's current selling price  
- Global feature importance for explainability  

This reflects how pricing teams in large retail organizations make data-driven pricing decisions.

---

# Features

## Optimal Price Prediction
Users input:
- Shipping cost (₹)
- Product weight (grams)
- Competitor price (₹)
- Customer rating
- Demand level
- Purchase month and year
- Product category
- Current selling price (₹)

The application returns:
- Recommended optimal price  
- Suggested price adjustment based on the difference from the current price  

## Business-Layer User Experience
All engineered ML features are handled internally.  
The interface exposes only meaningful business variables for clarity and usability.

## Model Insights
A feature importance chart provides a global view of how the trained model makes pricing decisions.

---

# Tech Stack

| Component       | Technology      |
|-----------------|------------------|
| Model Training  | Scikit-learn     |
| Data Handling   | Pandas, NumPy    |
| Application UI  | Streamlit        |
| Visualization   | Plotly           |
| Model Storage   | Joblib           |

---

# How to Use the Application

1. Start the Streamlit app locally.  
2. Use the sidebar to enter product information:
   - Category  
   - Shipping cost  
   - Product weight  
   - Competitor price  
   - Customer rating  
   - Demand level  
   - Purchase month and year  
   - Current selling price  
3. Click the "Predict Optimal Price" button.  
4. The main panel will display:
   - The recommended optimal selling price  
   - The price difference compared to the user's current price  
5. The right-side panel displays feature importance to help understand the model’s global behavior.

---

# Dataset

Olist Brazilian E-Commerce Dataset  
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

# Author

Preethikgha M  


