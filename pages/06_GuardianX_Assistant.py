import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="GuardianX Assistant",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🤖 GuardianX Assistant")
st.markdown("### Offline AI Factory Copilot")
st.markdown("---")

# --------------------------------------------------
# Load Data
# --------------------------------------------------
machines = pd.read_csv("data/machines.csv")
energy = pd.read_csv("data/energy.csv")
maintenance = pd.read_csv("data/maintenance.csv")
alerts = pd.read_csv("data/alerts.csv")

# --------------------------------------------------
# Quick Actions
# --------------------------------------------------
st.subheader("💬 Quick Actions")

question = st.selectbox(
    "Choose a question",
    [
        "Select...",
        "Today's Factory Summary",
        "Which machine needs immediate attention?",
        "Show pending maintenance",
        "Which machine consumes the highest power?",
        "Show critical alerts"
    ]
)

if question == "Today's Factory Summary":

    st.success(f"""
🏭 **Total Machines:** {len(machines)}

🚨 **Critical Alerts:** {len(alerts[alerts['Severity']=='Critical'])}

📅 **Pending Maintenance:** {len(maintenance[maintenance['Status']=='Pending'])}

⚡ **Total Power Consumption:** {energy['Current_Power_W'].sum()} W
""")

elif question == "Which machine needs immediate attention?":

    critical = machines[machines["Status"] == "Critical"]

    if len(critical) > 0:
        row = critical.iloc[0]

        st.error(f"""
🚨 **Machine:** {row['Machine_Name']}

📊 **Health Score:** {row['Health_Score']}

⚠ **Failure Probability:** {row['Failure_Probability']}%

### Recommendation

Immediate maintenance is strongly recommended.
""")

elif question == "Show pending maintenance":

    pending = maintenance[maintenance["Status"] == "Pending"]

    st.dataframe(
        pending,
        use_container_width=True
    )

elif question == "Which machine consumes the highest power?":

    highest = energy.loc[energy["Current_Power_W"].idxmax()]

    st.warning(f"""
⚡ **Machine:** {highest['Machine_Name']}

🔋 **Current Power:** {highest['Current_Power_W']} W

📌 **Status:** {highest['Status']}
""")

elif question == "Show critical alerts":

    critical = alerts[alerts["Severity"] == "Critical"]

    st.dataframe(
        critical,
        use_container_width=True
    )

st.divider()

# --------------------------------------------------
# Ask GuardianX
# --------------------------------------------------
st.subheader("⌨ Ask GuardianX")

user = st.text_input(
    "Ask a factory-related question"
)

if st.button("Ask GuardianX"):

    q = user.lower()

    if "summary" in q:

        st.success(
            "🏭 Factory operations are stable. Minor maintenance activities are pending, and overall performance remains within acceptable limits."
        )

    elif "energy" in q:

        st.info(
            "⚡ Overall energy consumption is within the expected operating range. One machine requires further inspection due to higher power usage."
        )

    elif "maintenance" in q:

        st.warning(
            "📅 Two maintenance activities are currently pending. Schedule them to avoid unexpected downtime."
        )

    elif "machine" in q:

        st.error(
            "🛠 Conveyor Motor requires immediate inspection due to its high failure probability."
        )

    elif "safety" in q:

        st.success(
            "🦺 No major worker safety violations have been detected today."
        )

    elif "alerts" in q:

        st.warning(
            "🚨 Two critical alerts are currently active in the factory."
        )

    else:

        st.info(
            "GuardianX Assistant supports queries related to machines, maintenance, energy, safety, alerts, and factory summary."
        )

st.divider()

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.caption("🛡️ GuardianX AI v1.0")
st.caption("AI-Powered Smart Factory Platform for MSMEs")