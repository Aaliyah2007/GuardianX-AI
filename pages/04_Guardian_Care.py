import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Guardian Care",
    page_icon="📅",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("📅 Guardian Care")
st.markdown("### Predictive Maintenance Management")
st.markdown("---")

# --------------------------------------------------
# Load Data
# --------------------------------------------------
maintenance = pd.read_csv("data/maintenance.csv")

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------
total = len(maintenance)
critical = len(maintenance[maintenance["Priority"] == "Critical"])
pending = len(maintenance[maintenance["Status"] == "Pending"])
scheduled = len(maintenance[maintenance["Status"] == "Scheduled"])

c1, c2, c3, c4 = st.columns(4)

c1.metric("🛠 Total Tasks", total)
c2.metric("🔴 Critical Tasks", critical)
c3.metric("⏳ Pending Tasks", pending)
c4.metric("✅ Scheduled Tasks", scheduled)

st.divider()

# --------------------------------------------------
# Priority Chart
# --------------------------------------------------
st.subheader("📊 Maintenance Priority Distribution")

fig = px.pie(
    maintenance,
    names="Priority",
    title="Maintenance Task Priority"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# --------------------------------------------------
# Maintenance Schedule
# --------------------------------------------------
st.subheader("📋 Maintenance Schedule")

st.dataframe(
    maintenance,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# AI Recommendations
# --------------------------------------------------
st.subheader("🤖 GuardianX AI Recommendations")

for _, row in maintenance.iterrows():

    if row["Priority"] == "Critical":

        st.error(
            f"🚨 **{row['Machine_Name']}** requires immediate maintenance to avoid unexpected machine failure."
        )

    elif row["Priority"] == "High":

        st.warning(
            f"⚠️ **{row['Machine_Name']}** should be serviced before **{row['Due_Date']}**."
        )

    else:

        st.success(
            f"✅ **{row['Machine_Name']}** maintenance is scheduled as planned."
        )

st.divider()

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.caption("🛡️ GuardianX AI v1.0")
st.caption("AI-Powered Smart Factory Platform for MSMEs")