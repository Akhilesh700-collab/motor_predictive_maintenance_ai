import streamlit as st
import pandas as pd

st.set_page_config(page_title="Motor Predictive Maintenance")

st.title("Industrial Motor Predictive Maintenance Dashboard")

df = pd.read_csv("data/motor_sensor_data.csv", header=None)
df.columns = ["Temperature", "Vibration", "Current"]

st.subheader("Latest Sensor Data")
st.write(df.tail(1))

st.subheader("Sensor Trends")
st.line_chart(df)

st.subheader("Statistics")
st.write(df.describe())
