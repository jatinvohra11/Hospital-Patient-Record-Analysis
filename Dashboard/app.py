
import streamlit as st
import pandas as pd
import plotly.express as px
from pymongo import MongoClient

# Page Configuration
st.set_page_config(
    page_title="Hospital Analytics Dashboard",
    page_icon="🏥",
    layout="wide"
)

# MongoDB Connection
@st.cache_resource
def connect_mongodb():
    client = MongoClient("mongodb://localhost:27017/")
    client.admin.command("ping")
    return client["hospital_analysis"]

try:
    db = connect_mongodb()
    st.success("MongoDB Connected Successfully!")
except Exception as e:
    st.error(f"MongoDB Connection Failed: {e}")
    st.stop()

# Dashboard Header
st.title("🏥 Hospital Patient Record Analysis")
st.markdown("### MongoDB Powered Healthcare Analytics Dashboard")
st.divider()

# Collections
appointments = db["appointments"]
prescriptions = db["prescriptions"]
laboratory = db["laboratory"]
imaging = db["imaging"]
pharmacy = db["pharmacy"]

# KPI Cards
st.subheader("Hospital Overview")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Appointments", f"{appointments.count_documents({}):,}")
col2.metric("Prescriptions", f"{prescriptions.count_documents({}):,}")
col3.metric("Laboratory", f"{laboratory.count_documents({}):,}")
col4.metric("Imaging", f"{imaging.count_documents({}):,}")
col5.metric("Pharmacy", f"{pharmacy.count_documents({}):,}")

st.divider()

# Monthly Appointment Analysis
st.subheader("📈 Monthly Appointment Analysis")

monthly_data = list(appointments.aggregate([
    {
        "$group": {
            "_id": "$appointment_month",
            "total": {"$sum": 1}
        }
    },
    {"$sort": {"_id": 1}}
]))

if monthly_data:
    monthly_df = pd.DataFrame(monthly_data)
    monthly_df.columns = ["Month", "Appointments"]

    fig = px.line(
        monthly_df,
        x="Month",
        y="Appointments",
        markers=True,
        title="Monthly Hospital Appointments"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# Top 10 Active Patients
st.subheader("👥 Top 10 Most Active Patients")

patient_data = list(appointments.aggregate([
    {
        "$group": {
            "_id": "$patient_id",
            "total_visits": {"$sum": 1}
        }
    },
    {"$sort": {"total_visits": -1}},
    {"$limit": 10}
]))

patient_df = pd.DataFrame(patient_data)

if not patient_df.empty:
    patient_df.columns = ["Patient ID", "Total Visits"]
    st.dataframe(patient_df, use_container_width=True)

st.divider()

# Top 10 Doctors
st.subheader("👨‍⚕️ Top 10 Doctors by Prescriptions")

doctor_data = list(prescriptions.aggregate([
    {
        "$group": {
            "_id": "$prescription_doctor_name",
            "total": {"$sum": 1}
        }
    },
    {"$sort": {"total": -1}},
    {"$limit": 10}
]))

doctor_df = pd.DataFrame(doctor_data)

if not doctor_df.empty:
    doctor_df.columns = ["Doctor", "Prescriptions"]
    fig = px.bar(
        doctor_df,
        x="Doctor",
        y="Prescriptions",
        title="Top 10 Doctors"
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# Top Laboratory Tests
st.subheader("🧪 Top 10 Laboratory Tests")

lab_data = list(laboratory.aggregate([
    {
        "$group": {
            "_id": "$lab_name",
            "total": {"$sum": 1}
        }
    },
    {"$sort": {"total": -1}},
    {"$limit": 10}
]))

lab_df = pd.DataFrame(lab_data)

if not lab_df.empty:
    lab_df.columns = ["Lab Test", "Total Tests"]
    fig = px.bar(
        lab_df,
        x="Total Tests",
        y="Lab Test",
        orientation="h",
        title="Most Common Laboratory Tests"
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# Imaging Analysis
st.subheader("🩻 Imaging Analysis")

imaging_data = list(imaging.aggregate([
    {
        "$group": {
            "_id": "$imaging_name",
            "total": {"$sum": 1}
        }
    },
    {"$sort": {"total": -1}},
    {"$limit": 10}
]))

imaging_df = pd.DataFrame(imaging_data)

if not imaging_df.empty:
    imaging_df.columns = ["Imaging Type", "Total"]
    fig = px.pie(
        imaging_df,
        names="Imaging Type",
        values="Total",
        title="Imaging Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# Pharmacy Analysis
st.subheader("💊 Top Medicines")

medicine_data = list(pharmacy.aggregate([
    {
        "$group": {
            "_id": "$medicine_name",
            "total": {"$sum": 1}
        }
    },
    {"$sort": {"total": -1}},
    {"$limit": 10}
]))

medicine_df = pd.DataFrame(medicine_data)

if not medicine_df.empty:
    medicine_df.columns = ["Medicine", "Sales Records"]
    st.dataframe(medicine_df, use_container_width=True)

st.divider()

st.caption("Hospital Patient Record Analysis | Built with Python, MongoDB, PyMongo and Streamlit")
