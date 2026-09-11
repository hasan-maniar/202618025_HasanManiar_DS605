import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="NYC Airbnb Price Predictor", page_icon="🏠")


@st.cache_resource
def load_model():
    return joblib.load("model/price_pipeline.pkl")

model = load_model()

st.title("🏠 NYC Airbnb Price Predictor")
st.write("Enter listing details to estimate the nightly price.")

# --- Reference values used to build the neighbourhood frequency feature ---
NEIGHBOURHOOD_GROUPS = ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"]
ROOM_TYPES = ["Entire home/apt", "Private room", "Shared room"]

col1, col2 = st.columns(2)

with col1:
    neighbourhood_group = st.selectbox("Neighbourhood Group", NEIGHBOURHOOD_GROUPS)
    room_type = st.selectbox("Room Type", ROOM_TYPES)
    latitude = st.number_input("Latitude", value=40.7128, format="%.6f")
    longitude = st.number_input("Longitude", value=-73.9560, format="%.6f")
    neighbourhood_freq = st.slider(
        "Neighbourhood popularity (share of listings)", 0.0, 0.10, 0.01, step=0.001
    )

with col2:
    minimum_nights = st.number_input("Minimum Nights", min_value=1, max_value=365, value=3)
    number_of_reviews = st.number_input("Number of Reviews", min_value=0, value=10)
    reviews_per_month = st.number_input("Reviews per Month", min_value=0.0, value=1.0, step=0.1)
    calculated_host_listings_count = st.number_input("Host's Total Listings", min_value=1, value=1)
    availability_365 = st.slider("Availability (days/year)", 0, 365, 180)

if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        "neighbourhood_group": str(neighbourhood_group),
        "room_type": str(room_type),
        "latitude": float(latitude),
        "longitude": float(longitude),
        "minimum_nights": float(minimum_nights),
        "number_of_reviews": float(number_of_reviews),
        "reviews_per_month": float(reviews_per_month),
        "calculated_host_listings_count": float(calculated_host_listings_count),
        "availability_365": float(availability_365),
        "neighbourhood_freq": float(neighbourhood_freq)
    }])

    try:
        log_pred = model.predict(input_df)[0]
        price_pred = np.expm1(log_pred)
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        st.write("Input data sent to model:")
        st.write(input_df)
        st.write(input_df.dtypes)
        st.stop()

    st.success(f"### Estimated Nightly Price: **${price_pred:,.2f}**")
    st.caption("This is an estimate based on historical NYC Airbnb data (2019) and may not reflect current market rates.")