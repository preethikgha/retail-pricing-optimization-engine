import streamlit as st
import pandas as pd
import joblib
import numpy as np
from pathlib import Path
import plotly.express as px

st.set_page_config(page_title="Dynamic Pricing Engine", layout="wide")

MODEL_PATH = Path("pricing_model.pkl")

@st.cache_resource
def load_model(path):
    return joblib.load(path)

model = load_model(MODEL_PATH)

st.markdown("""
    <h1 style='color:white;'>Dynamic Pricing Engine</h1>
    <p style='color:#b3b3b3;'>Predict optimal selling price using demand signals, seasonality, product attributes, and competitor benchmarks.</p>
""", unsafe_allow_html=True)

st.sidebar.header("Product Inputs")

category = st.sidebar.selectbox("Product Category", ["Electronics", "Clothing", "Home", "Beauty", "Sports", "Automotive", "Others"])
shipping_cost = st.sidebar.number_input("Shipping Cost (₹)", min_value=0.0, value=120.0, step=1.0)
weight = st.sidebar.number_input("Product Weight (grams)", min_value=1.0, value=500.0, step=1.0)
review_score = st.sidebar.slider("Customer Rating (1-5)", 1.0, 5.0, 4.0, 0.1)
competitor_price = st.sidebar.number_input("Competitor Price (₹)", min_value=0.0, value=150.0, step=1.0)
demand_level = st.sidebar.selectbox("Demand Level", ["Low", "Medium", "High"])
month = st.sidebar.slider("Purchase Month", 1, 12, 7)
year = st.sidebar.selectbox("Purchase Year (2015–2025)", list(range(2015, 2026)))
current_price = st.sidebar.number_input("Your Current Selling Price (₹)", min_value=0.0, value=120.0, step=1.0)

price_freight_ratio = competitor_price / (shipping_cost + 1)
weight_price_ratio = weight / (competitor_price + 1)

input_df = pd.DataFrame([{
    "freight_value": shipping_cost,
    "review_score": review_score,
    "month": month,
    "year": year,
    "price_freight_ratio": price_freight_ratio,
    "weight_price_ratio": weight_price_ratio
}])

left, right = st.columns([2.2, 1])

with left:
    st.subheader("Optimal Price Prediction")
    if st.button("Predict Optimal Price", use_container_width=True):
        predicted = model.predict(input_df)[0]
        st.markdown(f"""
            <div style="padding:20px; background-color:#111; border-radius:12px;">
                <h2 style="color:#00ffb0; font-size:46px;">₹ {predicted:.2f}</h2>
                <p style="color:#b3b3b3;">Recommended Optimal Selling Price</p>
            </div>
        """, unsafe_allow_html=True)
        delta = predicted - current_price
        color = "#00ffb0" if delta >= 0 else "#ff5e5e"
        st.markdown(
            f"<p style='color:white; font-size:18px;'>Difference vs current price: "
            f"<span style='color:{color}; font-weight:700'>₹ {delta:+.2f}</span></p>",
            unsafe_allow_html=True
        )

with right:
    st.subheader("Key Insights (Model Feature Importance)")
    try:
        feat_names = [
            "freight_value",
            "review_score",
            "month",
            "year",
            "price_freight_ratio",
            "weight_price_ratio"
        ]
        fi = model.feature_importances_
        fi_df = pd.DataFrame({"feature": feat_names, "importance": fi}).sort_values("importance")
        fig = px.bar(fi_df, x="importance", y="feature", orientation="h", template="plotly_dark", height=400)
        fig.update_layout(
            xaxis=dict(range=[0, fi_df["importance"].max() * 1.1]),
            yaxis=dict(autorange="reversed"),
            margin=dict(l=20, r=20, t=20, b=20)
        )
        st.plotly_chart(fig, use_container_width=True)
    except:
        st.write("Feature importance not available.")

st.markdown("""
<br><hr>
<p style='color:#888; text-align:center;'> •
Dynamic Pricing Engine • 
</p>
""", unsafe_allow_html=True)

