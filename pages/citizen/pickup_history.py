import streamlit as st
import pandas as pd

from utils.database import (
    PICKUPS_FILE,
    load_data
)

# ==========================================================
# PICKUP HISTORY PAGE
# ==========================================================

def show_pickup_history():

    st.title("📜 Pickup History")

    st.markdown(
        """
        View all your pickup requests,
        their status, and assigned collectors.
        """
    )

    st.markdown("---")

    user_id = st.session_state.get(
        "user_id",
        ""
    )

    pickups = load_data(
        PICKUPS_FILE
    )

    user_pickups = [

        pickup

        for pickup in pickups

        if pickup.get("user_id")
        == user_id

    ]

    if not user_pickups:

        st.info(
            "No pickup requests found."
        )

        return

    # ======================================================
    # SUMMARY METRICS
    # ======================================================

    pending = len([
        p for p in user_pickups
        if p.get("status") == "Pending"
    ])

    accepted = len([
        p for p in user_pickups
        if p.get("status") == "Accepted"
    ])

    collected = len([
        p for p in user_pickups
        if p.get("status") == "Collected"
    ])

    rejected = len([
        p for p in user_pickups
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
    # TABLE VIEW
    # ======================================================

    table_data = []

    for pickup in user_pickups:

        table_data.append({

            "Pickup ID":
            pickup.get(
                "pickup_id",
                ""
            ),

            "Waste Type":
            pickup.get(
                "waste_type",
                ""
            ),

            "Quantity (KG)":
            pickup.get(
                "quantity",
                ""
            ),

            "Pickup Date":
            pickup.get(
                "pickup_date",
                ""
            ),

            "Collector":
            pickup.get(
                "collector_name",
                "Not Assigned"
            ),

            "Status":
            pickup.get(
                "status",
                ""
            )

        })

    df = pd.DataFrame(
        table_data
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.markdown("---")

    # ======================================================
    # DETAILED CARDS
    # ======================================================

    st.subheader(
        "📦 Request Details"
    )

    for pickup in reversed(
        user_pickups
    ):

        with st.expander(
            f"{pickup['pickup_id']} - {pickup['waste_type']}"
        ):

            st.write(
                f"🗑 Waste Type: "
                f"{pickup['waste_type']}"
            )

            st.write(
                f"⚖ Quantity: "
                f"{pickup['quantity']} KG"
            )

            st.write(
                f"📅 Pickup Date: "
                f"{pickup['pickup_date']}"
            )

            st.write(
                f"⏰ Pickup Time: "
                f"{pickup['pickup_time']}"
            )

            st.write(
                f"📍 Address: "
                f"{pickup['address']}"
            )

            st.write(
                f"🚛 Collector: "
                f"{pickup.get('collector_name', 'Not Assigned')}"
            )

            status = pickup.get(
                "status",
                "Pending"
            )

            if status == "Pending":

                st.warning(
                    "🟡 Pending"
                )

            elif status == "Accepted":

                st.info(
                    "🟢 Accepted"
                )

            elif status == "Collected":

                st.success(
                    "♻ Collected"
                )

            elif status == "Rejected":

                st.error(
                    "🔴 Rejected"
                )

            st.write(
                f"🕒 Requested At: "
                f"{pickup.get('requested_at', '')}"
            )

    st.markdown("---")

    st.success(
        "🌱 Thank you for contributing to a cleaner environment."
    )