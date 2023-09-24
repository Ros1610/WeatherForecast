import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast")
place = st.text_input("Place:", help="Enter a city")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature (C)", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# Check if place isn't none
if place:

    try:
        # Fetch filtered data from the API
        filtered_data = get_data(place, days)

        # Get date list
        date = [i["dt_txt"] for i in filtered_data]

        match option:

            # Create a temperature plot
            case "Temperature (C)":
                temp = [(i["main"]["temp"]) / 10 for i in filtered_data]
                figure = px.line(x=date, y=temp,
                                 labels={"x": "Date", "y": option})
                st.plotly_chart(figure)

            # Create sky images
            case "Sky":
                weathers = [i["weather"][0]["main"] for i in filtered_data]
                image_paths = [f"images/{weather}.png" for weather in weathers]
                st.image(image_paths, width=115, caption=date)

    # Check if place exists
    except KeyError:
        st.info("You have entered a non-existing place")