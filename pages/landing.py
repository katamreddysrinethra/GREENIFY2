import streamlit as st


def show_landing_page():

    # =====================================================
    # HERO SECTION
    # =====================================================

    st.title("🌱 GREENIFY")

    st.subheader(
        "Smart Waste Management & Recycling Platform"
    )

    st.markdown(
        """
        ### ♻ Reduce Waste • Recycle Better • Earn Rewards

        GREENIFY helps citizens, waste collectors,
        and recycling markets work together to build
        a cleaner and greener future.
        """
    )

    st.markdown("---")

    # =====================================================
    # BANNER IMAGE
    # =====================================================

    

        


    # =====================================================
    # IMPACT STATS
    # =====================================================

    st.header("🌍 Making An Environmental Impact")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "♻ Waste Recycled",
            "12,500+ KG"
        )

    with col2:
        st.metric(
            "🚛 Pickups Completed",
            "4,850+"
        )

    with col3:
        st.metric(
            "🌱 CO₂ Saved",
            "7.2 Tons"
        )

    with col4:
        st.metric(
            "👥 Active Users",
            "3,000+"
        )

    st.markdown("---")

    # =====================================================
    # FEATURES
    # =====================================================

    st.header("🚀 Platform Features")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.success(
            """
            📸 AI Waste Scanner

            Upload waste images and let AI
            identify the waste category.
            """
        )

    with col2:

        st.success(
            """
            🚛 Smart Pickup System

            Request pickups and track
            waste collection status.
            """
        )

    with col3:

        st.success(
            """
            🎁 Rewards & Badges

            Earn Green Points and
            unlock achievements.
            """
        )

    col4, col5, col6 = st.columns(3)

    with col4:

        st.info(
            """
            🌍 Environmental Impact

            Track your sustainability
            contribution.
            """
        )

    with col5:

        st.info(
            """
            📚 Education Hub

            Learn waste segregation
            and recycling practices.
            """
        )

    with col6:

        st.info(
            """
            🏪 Recycling Marketplace

            Connect buyers and sellers
            in the recycling ecosystem.
            """
        )

    st.markdown("---")

    # =====================================================
    # HOW IT WORKS
    # =====================================================

    st.header("♻ How GREENIFY Works")

    st.markdown(
        """
        1️⃣ Scan Waste Using AI

        2️⃣ Identify Waste Category

        3️⃣ Request Pickup

        4️⃣ Earn Green Points

        5️⃣ Create Environmental Impact
        """
    )

    st.markdown("---")

    # =====================================================
    # BENEFITS
    # =====================================================

    st.header("🌟 Why Choose GREENIFY?")

    st.write("✅ Easy Waste Segregation")

    st.write("✅ AI Powered Identification")

    st.write("✅ Reward Based Recycling")

    st.write("✅ Smart Pickup Scheduling")

    st.write("✅ Environmental Impact Tracking")

    st.write("✅ Marketplace Integration")

    st.markdown("---")

    # =====================================================
    # CONTINUE BUTTON
    # =====================================================

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        if st.button(
            "🚀 CLICK TO CONTINUE",
            use_container_width=True
        ):

            st.session_state.page = "login"

            st.rerun()

    st.markdown("---")

    # =====================================================
    # FOOTER
    # =====================================================

    st.caption(
        "🌱 Together We Can Build A Cleaner And Greener Future 🌱"
    )