import streamlit as st

def apply_branding():
    st.sidebar.markdown(
        """
        <div style="text-align:center; padding:10px;">
            <h1 style="color:#00C2FF; margin-bottom:0;">🛡️ GuardianX AI</h1>
            <p style="font-size:15px; color:#B8C7D1; margin-top:0;">
                Predict. Protect. Prevent.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown("---")

    st.markdown(
        """
        <h1 style="margin-bottom:0;">🛡️ GuardianX AI</h1>
        <p style="font-size:18px;color:#00C2FF;">
        Predict. Protect. Prevent.
        </p>
        <p style="color:gray;">
        AI-Powered Smart Factory Platform for MSMEs
        </p>
        """,
        unsafe_allow_html=True,
    )