import streamlit as st

# ==========================================================
# CITIZEN HOME PAGE
# ==========================================================

def show_citizen_home():

    st.title("🌱 Citizen Dashboard")

    st.subheader("⚡ Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            ### 📸 AI Scanner
            Identify waste instantly using AI.
            """
        )

        if st.button(
            "Open AI Scanner",
            use_container_width=True
        ):
            st.info(
                "Use the sidebar and select AI Scanner."
            )

    with col2:

        st.markdown(
            """
            ### 🚛 Pickup Request
            Schedule waste pickup from your location.
            """
        )

        if st.button(
            "Request Pickup",
            use_container_width=True
        ):
            st.info(
                "Use the sidebar and select Pickup Request."
            )

    with col3:

        st.markdown(
            """
            ### 🎁 Rewards
            View points and sustainability badges.
            """
        )

        if st.button(
            "View Rewards",
            use_container_width=True
        ):
            st.info(
                "Use the sidebar and select Rewards."
            )

    st.markdown("---")

    st.success(
        "Welcome to GREENIFY Citizen Portal 🌍"
    )