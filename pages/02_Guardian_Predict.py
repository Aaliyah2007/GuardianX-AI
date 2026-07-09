import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Guardian Predict",
    page_icon="🛠",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🛠 Guardian Predict")
st.markdown("### AI-Powered Predictive Maintenance")
st.markdown("---")

# --------------------------------------------------
# Load Machine Data
# --------------------------------------------------
machines = pd.read_csv("data/machines.csv")

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------
healthy = len(machines[machines["Status"] == "Healthy"])
warning = len(machines[machines["Status"] == "Warning"])
critical = len(machines[machines["Status"] == "Critical"])

c1, c2, c3 = st.columns(3)

c1.metric("🟢 Healthy Machines", healthy)
c2.metric("🟡 Warning Machines", warning)
c3.metric("🔴 Critical Machines", critical)

st.divider()

# --------------------------------------------------
# Machine Health Chart
# --------------------------------------------------
st.subheader("📊 Machine Health Score")

fig = px.bar(
    machines,
    x="Machine_Name",
    y="Health_Score",
    color="Status",
    text="Health_Score",
    title="Machine Health Performance"
)

fig.update_layout(height=450)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# --------------------------------------------------
# Machine Details
# --------------------------------------------------
st.subheader("📋 Machine Health Details")

st.dataframe(
    machines,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# AI Recommendations
# --------------------------------------------------
st.subheader("🤖 GuardianX AI Recommendations")

for _, row in machines.iterrows():

    if row["Status"] == "Critical":

        st.error(
            f"🚨 **{row['Machine_Name']}** has a **{row['Failure_Probability']}%** failure probability.\n\n"
            "Immediate maintenance is strongly recommended to avoid unexpected downtime."
        )

    elif row["Status"] == "Warning":

        st.warning(
            f"⚠️ **{row['Machine_Name']}** should be inspected within **{row['Maintenance_Due']}**."
        )

    else:

        st.success(
            f"✅ **{row['Machine_Name']}** is operating within normal health limits."
        )

st.divider()

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.caption("🛡️ GuardianX AI v1.0")
st.caption("AI-Powered Smart Factory Platform for MSMEs")