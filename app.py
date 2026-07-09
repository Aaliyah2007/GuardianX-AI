import streamlit as st

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="GuardianX AI",
    page_icon="🛡️",
    layout="wide"
)

# ------------------------------
# Header
# ------------------------------
st.title("🛡️ GuardianX AI")
st.markdown("## Predict. Protect. Prevent.")
st.markdown("---")

# ------------------------------
# Welcome Section
# ------------------------------
st.markdown("## Welcome to GuardianX AI")
st.markdown("### AI-Powered Smart Factory Platform for MSMEs")

st.write("")

st.markdown("""
GuardianX AI is an **Industry 4.0 intelligent monitoring platform** designed for
**Micro, Small and Medium Enterprises (MSMEs)** to improve factory safety,
machine reliability, energy efficiency, and maintenance using Artificial Intelligence.

### 🚀 Core Modules

- 🛠 **Guardian Predict** – AI-Based Machine Health Monitoring
- ⚡ **Guardian Energy** – Real-Time Energy Consumption Analytics
- 📅 **Guardian Care** – Predictive Maintenance Management
- 🦺 **Guardian Safe** – Computer Vision-Based Worker Safety Monitoring
- 🤖 **GuardianX Assistant** – Offline AI Factory Copilot
""")

st.info("👈 Select a module from the sidebar to begin monitoring your factory.")

st.divider()

# ------------------------------
# Features
# ------------------------------
col1, col2 = st.columns(2)

with col1:
    st.success("✅ AI-Powered Predictive Maintenance")
    st.success("✅ Smart Energy Monitoring")
    st.success("✅ Worker Safety Analytics")

with col2:
    st.success("✅ Preventive Maintenance Scheduling")
    st.success("✅ Interactive Dashboards")
    st.success("✅ Offline AI Factory Assistant")

st.divider()

# ------------------------------
# Footer
# ------------------------------
st.caption("🛡️ GuardianX AI v1.0")
st.caption("AI-Powered Smart Factory Platform for MSMEs")