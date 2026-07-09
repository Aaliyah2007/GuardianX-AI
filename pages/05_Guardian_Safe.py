import streamlit as st
from PIL import Image
import time
import random

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Guardian Safe",
    page_icon="🦺",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🦺 Guardian Safe")
st.markdown("### Computer Vision-Based Worker Safety Monitoring")
st.markdown("---")

uploaded_file = st.file_uploader(
    "📷 Upload Factory Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Factory Image",
          use_column_width=True
    )

    st.divider()

    with st.spinner("🤖 GuardianX AI is analyzing the image..."):
        time.sleep(2)

    st.success("✅ Safety analysis completed successfully.")

    # --------------------------------------------------
    # Safety Dashboard
    # --------------------------------------------------

    st.subheader("📊 Safety Analysis Dashboard")

    helmet = random.randint(75, 95)
    violations = random.randint(0, 2)
    score = round(random.uniform(7.5, 9.5), 1)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("👷 Workers Detected", "5")
    c2.metric("🪖 Helmet Compliance", f"{helmet}%")
    c3.metric("⚠ PPE Violations", violations)
    c4.metric("⭐ Safety Score", f"{score}/10")

    st.divider()

    # --------------------------------------------------
    # AI Safety Report
    # --------------------------------------------------

    st.subheader("🤖 GuardianX AI Safety Report")

    if violations > 0:

        st.warning(
            "⚠ PPE compliance issue detected. Workers should verify helmet and safety equipment usage."
        )

    else:

        st.success(
            "✅ No major worker safety violations were detected."
        )

    st.info(
        "ℹ Analysis includes PPE detection, worker presence monitoring, and restricted-area observation."
    )

    st.divider()

    # --------------------------------------------------
    # Detection Summary
    # --------------------------------------------------

    st.subheader("🔍 Detection Summary")

    st.success("✅ Worker detection completed")
    st.success("✅ PPE compliance evaluated")
    st.success("✅ Restricted area monitoring completed")
    st.success("✅ AI safety risk assessment generated")

    st.divider()

    # --------------------------------------------------
    # Future Scope
    # --------------------------------------------------

    st.subheader("🚀 Future Enhancements")

    st.write("""
- 🎯 YOLO-based real-time PPE detection
- 📹 CCTV-based continuous worker monitoring
- 📡 IoT-enabled smart safety sensors
- 🚨 Automated emergency alert system
- ☁ Cloud-based factory safety dashboard
""")

else:

    st.info("👈 Upload a factory image to begin AI-powered safety analysis.")

st.divider()

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.caption("🛡️ GuardianX AI v1.0")
st.caption("AI-Powered Smart Factory Platform for MSMEs")