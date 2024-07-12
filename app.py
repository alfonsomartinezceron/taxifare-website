import streamlit as st
from datetime import datetime
import requests

st.title('Taxi Ride Fare Application')

st.header('Taxi Ride Data Input')

# Date and Time
pickup_date = st.date_input("Pickup Date", datetime.now().date())
#st.time_input("Pickup Time", datetime.now().time())
pickup_time = st.time_input("Pickup Time",)
pickup_datetime = datetime.combine(pickup_date, pickup_time)

# Coordinates
#pickup_longitude = st.number_input("Pickup Longitude", value=0.0, format="%.6f")
pickup_longitude = st.number_input("Pickup Longitude", value=0.0, format="%.6f")
pickup_latitude = st.number_input("Pickup Latitude", value=0.0, format="%.6f")
dropoff_longitude = st.number_input("Dropoff Longitude", value=0.0, format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude", value=0.0, format="%.6f")

# Passenger Count
#passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, value=1)
passenger_count = st.slider('Number of passengers',1,8,1)

# Model to call for the prediction
api_url = 'https://taxifare.lewagon.ai/predict'

    # Build the dictionary with input parameters
input_data = {
        "pickup_datetime": pickup_datetime.isoformat(),
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

if st.button("Get the predict"):
    # Call the API using POST
    response = requests.get(api_url,input_data)

    # Check if the request was successful
    if response.status_code == 200:
        # Retrieve the prediction from the JSON response
        prediction = response.json()['fare']
        st.write("## Prediction")
        st.write(f"Predicted value: {prediction}")
    else:
        st.write("## Error")
        st.write(f"Error: {response.status_code}")
        st.write(response.json().get("detail", "Unknown error"))

# Create a DataFrame for the map centered on New York City
map_data = {
    'lat': [40.7128],
    'lon': [-74.0060]
}

# Display the map
st.map(map_data)
