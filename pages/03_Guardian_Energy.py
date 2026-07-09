import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Guardian Energy",
    page_icon="⚡",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("⚡ Guardian Energy")
st.markdown("### Real-Time AI-Powered Energy Analytics")
st.markdown("---")

# --------------------------------------------------
# Load Data
# --------------------------------------------------
energy = pd.read_csv("data/energy.csv")

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------
total_power = energy["Current_Power_W"].sum()
abnormal = len(energy[energy["Status"] == "Abnormal"])
normal = len(energy[energy["Status"] == "Normal"])
avg_power = round(energy["Current_Power_W"].mean(), 1)

c1, c2, c3, c4 = st.columns(4)

c1.metric("⚡ Total Power", f"{total_power} W")
c2.metric("🟢 Normal Machines", normal)
c3.metric("🔴 Abnormal Machines", abnormal)
c4.metric("📊 Average Power", f"{avg_power} W")

st.divider()

# --------------------------------------------------
# Energy Chart
# --------------------------------------------------
st.subheader("📊 Machine-wise Power Consumption")

fig = px.bar(
    energy,
    x="Machine_Name",
    y="Current_Power_W",
    color="Status",
    text="Current_Power_W",
    title="Machine Power Consumption"
)

fig.update_layout(height=450)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# --------------------------------------------------
# Energy Details
# --------------------------------------------------
st.subheader("📋 Energy Usage Details")

st.dataframe(
    energy,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# AI Recommendations
# --------------------------------------------------
st.subheader("🤖 GuardianX AI Recommendations")

for _, row in energy.iterrows():

    if row["Status"] == "Abnormal":

        st.error(
            f"🚨 **{row['Machine_Name']}** is consuming **{row['Current_Power_W']} W**, "
            "which is above the expected operating range.\n\n"
            "Inspect the machine for overload, mechanical issues, or electrical faults."
        )

    else:

        st.success(
            f"✅ **{row['Machine_Name']}** is operating within normal energy consumption limits."
        )

st.divider()

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.caption("🛡️ GuardianX AI v1.0")
st.caption("AI-Powered Smart Factory Platform for MSMEs")