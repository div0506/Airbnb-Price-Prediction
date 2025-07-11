import streamlit as st
import pandas as pd
import pickle

from model_loader import load_model

model = load_model()


# Load model and expected column order
model = pickle.load(open('model.pkl', 'rb'))
model_columns = pickle.load(open('model_columns.pkl', 'rb'))

st.title("Airbnb Price Prediction 🏠💰")

# --- User Inputs ---
room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room", "Hotel room"])
neighbourhood_group = st.selectbox("Neighbourhood Group", ["Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"])
minimum_nights = st.slider("Minimum Nights", 1, 30, 1)
number_of_reviews = st.slider("Number of Reviews", 0, 300, 10)
reviews_per_month = st.slider("Reviews per Month", 0.0, 10.0, 1.0)
availability_365 = st.slider("Availability (days/year)", 0, 365, 180)
listings_count = st.slider("Host Listings Count", 1, 10, 1)

# --- Input Dictionary ---
input_dict = {
    'minimum_nights': minimum_nights,
    'number_of_reviews': number_of_reviews,
    'reviews_per_month': reviews_per_month,
    'calculated_host_listings_count': listings_count,
    'availability_365': availability_365,
    'neighbourhood_group_Brooklyn': 1 if neighbourhood_group == "Brooklyn" else 0,
    'neighbourhood_group_Manhattan': 1 if neighbourhood_group == "Manhattan" else 0,
    'neighbourhood_group_Queens': 1 if neighbourhood_group == "Queens" else 0,
    'neighbourhood_group_Staten Island': 1 if neighbourhood_group == "Staten Island" else 0,
    'room_type_Private room': 1 if room_type == "Private room" else 0,
    'room_type_Shared room': 1 if room_type == "Shared room" else 0,
    'room_type_Hotel room': 1 if room_type == "Hotel room" else 0
}

# --- Format Input for Model ---
input_df = pd.DataFrame([input_dict])
input_df = input_df.reindex(columns=model_columns, fill_value=0)

# --- Prediction ---
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Price: ${prediction:.2f} per night")
