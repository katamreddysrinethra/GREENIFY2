import streamlit as st

from utils.database import (
    PICKUPS_FILE,
    load_data
)

# ==========================================================
# COLLECTOR HOME PAGE
# ==========================================================

def show_collector_home():

    st.title("🚛 Collector Dashboard")

    collector_name = st.session_state.get(
        "user_name",
        "Collector"
    )

    st.markdown(
        f"""
        Welcome **{collector_name}**!

        Manage pickup requests, monitor collection
        activities, and contribute to a cleaner city.
        """
    )

    st.markdown("---")

    pickups = load_data(
        PICKUPS_FILE
    )

    # ======================================================
    # STATISTICS
    # ======================================================

    pending = len([
        p for p in pickups
        if p.get("status") == "Pending"
    ])

    accepted = len([
        p for p in pickups
        if p.get("status") == "Accepted"
    ])

    collected = len([
        p for p in pickups
        if p.get("status") == "Collected"
    ])

    rejected = len([
        p for p in pickups
        if p.get("status") == "Rejected"
    ])

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🟡 Pending",
            pending
        )

    with col2:
        st.metric(
            "🟢 Accepted",
            accepted
        )

    with col3:
        st.metric(
            "♻ Collected",
            collected
        )

    with col4:
        st.metric(
            "🔴 Rejected",
            rejected
        )

    st.markdown("---")

    # ======================================================
    # QUICK ACTIONS
    # ======================================================

    st.subheader(
        "⚡ Quick Actions"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="dashboard-card">
                <h3>📦 Manage Pickups</h3>
                <p>
                Accept or reject citizen pickup requests.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="dashboard-card">
                <h3>📜 Pickup History</h3>
                <p>
                View completed and assigned collections.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="dashboard-card">
                <h3>📊 Statistics</h3>
                <p>
                Monitor performance and collection metrics.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # ======================================================
    # RECENT REQUESTS
    # ======================================================

    st.subheader(
        "📋 Recent Pickup Requests"
    )

    recent_pickups = pickups[-5:]

    if not recent_pickups:

        st.info(
            "No pickup requests available."
        )

    else:

        for pickup in reversed(
            recent_pickups
        ):

            with st.expander(
                f"{pickup['pickup_id']} - {pickup['waste_type']}"
            ):

                st.write(
                    f"👤 Citizen: "
                    f"{pickup.get('user_name','')}"
                )

                st.write(
                    f"⚖ Quantity: "
                    f"{pickup.get('quantity','')} KG"
                )

                st.write(
                    f"📍 Address: "
                    f"{pickup.get('address','')}"
                )

                st.write(
                    f"📅 Date: "
                    f"{pickup.get('pickup_date','')}"
                )

                st.write(
                    f"📊 Status: "
                    f"{pickup.get('status','')}"
                )

    st.markdown("---")

    # ======================================================
    # COLLECTOR TIPS
    # ======================================================

    st.subheader(
        "💡 Collection Tips"
    )

    st.success(
        "Verify waste type before collection."
    )

    st.success(
        "Update pickup status immediately after collection."
    )

    st.success(
        "Follow proper waste handling guidelines."
    )

    st.success(
        "Promote segregation awareness among citizens."
    )

    st.markdown("---")

    st.info(
        "🌱 Your work plays a vital role in creating a sustainable environment."
    )