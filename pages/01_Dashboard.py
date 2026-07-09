import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="GuardianX AI Dashboard",
    page_icon="🏭",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🏭 GuardianX AI Dashboard")
st.markdown("### Real-Time Smart Factory Monitoring")
st.markdown("---")

# --------------------------------------------------
# Load Data
# --------------------------------------------------
machines = pd.read_csv("data/machines.csv")
energy = pd.read_csv("data/energy.csv")
maintenance = pd.read_csv("data/maintenance.csv")
alerts = pd.read_csv("data/alerts.csv")

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------
healthy = len(machines[machines["Status"] == "Healthy"])
critical = len(alerts[alerts["Severity"] == "Critical"])
pending = len(maintenance[maintenance["Status"] == "Pending"])
power = energy["Current_Power_W"].sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric("🟢 Healthy Machines", healthy)
c2.metric("🔴 Critical Alerts", critical)
c3.metric("⚡ Total Power", f"{power} W")
c4.metric("📅 Pending Tasks", pending)

st.divider()

# --------------------------------------------------
# Charts
# --------------------------------------------------
left, right = st.columns(2)

with left:
    fig = px.pie(
        machines,
        names="Status",
        title="Machine Health Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    fig2 = px.bar(
        energy,
        x="Machine_Name",
        y="Current_Power_W",
        color="Status",
        title="Machine-wise Energy Consumption"
    )
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# --------------------------------------------------
# Alerts
# --------------------------------------------------
st.subheader("🚨 Recent Factory Alerts")
st.dataframe(alerts, use_container_width=True)

st.divider()

# --------------------------------------------------
# AI Recommendations
# --------------------------------------------------
st.subheader("🤖 GuardianX AI Recommendations")

st.success("""
✅ Conveyor Motor requires immediate inspection.

⚠️ Hydraulic Press should undergo bearing maintenance.

🦺 Improve PPE compliance in the production area.

⚡ Factory energy consumption is currently above the normal threshold.

📅 Schedule preventive maintenance for pending machines.
""")

st.divider()

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.caption("🛡️ GuardianX AI v1.0")
st.caption("AI-Powered Smart Factory Platform for MSMEs")