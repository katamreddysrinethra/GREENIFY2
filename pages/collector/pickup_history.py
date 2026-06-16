import streamlit as st
import pandas as pd

from utils.database import (
    PICKUPS_FILE,
    load_data
)

# ==========================================================
# COLLECTOR PICKUP HISTORY
# ==========================================================

def show_collector_history():

    st.title("📜 Pickup History")

    collector_id = st.session_state.get(
        "user_id",
        ""
    )

    pickups = load_data(
        PICKUPS_FILE
    )

    collector_pickups = [

        pickup

        for pickup in pickups

        if pickup.get(
            "collector_id"
        ) == collector_id

    ]

    if not collector_pickups:

        st.info(
            "No assigned pickups found."
        )

        return

    st.markdown("---")

    # ======================================================
    # SUMMARY
    # ======================================================

    accepted = len([
        p for p in collector_pickups
        if p.get("status") == "Accepted"
    ])

    collected = len([
        p for p in collector_pickups
        if p.get("status") == "Collected"
    ])

    rejected = len([
        p for p in collector_pickups
        if p.get("status") == "Rejected"
    ])

    total_weight = sum(

        float(
            p.get("quantity", 0)
        )

        for p in collector_pickups

        if p.get("status")
        == "Collected"

    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🟢 Accepted",
            accepted
        )

    with col2:
        st.metric(
            "♻ Collected",
            collected
        )

    with col3:
        st.metric(
            "🔴 Rejected",
            rejected
        )

    with col4:
        st.metric(
            "⚖ Total KG",
            round(
                total_weight,
                2
            )
        )

    st.markdown("---")

    # ======================================================
    # TABLE
    # ======================================================

    table = []

    for pickup in collector_pickups:

        table.append({

            "Pickup ID":
            pickup.get(
                "pickup_id",
                ""
            ),

            "Citizen":
            pickup.get(
                "user_name",
                ""
            ),

            "Waste Type":
            pickup.get(
                "waste_type",
                ""
            ),

            "Quantity":
            pickup.get(
                "quantity",
                ""
            ),

            "Date":
            pickup.get(
                "pickup_date",
                ""
            ),

            "Status":
            pickup.get(
                "status",
                ""
            )

        })

    df = pd.DataFrame(
        table
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.markdown("---")

    # ======================================================
    # DETAILS
    # ======================================================

    st.subheader(
        "📦 Collection Details"
    )

    for pickup in reversed(
        collector_pickups
    ):

        with st.expander(

            f"{pickup['pickup_id']} "
            f"- "
            f"{pickup['waste_type']}"

        ):

            st.write(
                f"👤 Citizen: "
                f"{pickup.get('user_name','')}"
            )

            st.write(
                f"📍 Address: "
                f"{pickup.get('address','')}"
            )

            st.write(
                f"⚖ Quantity: "
                f"{pickup.get('quantity','')} KG"
            )

            st.write(
                f"📅 Pickup Date: "
                f"{pickup.get('pickup_date','')}"
            )

            st.write(
                f"⏰ Pickup Time: "
                f"{pickup.get('pickup_time','')}"
            )

            status = pickup.get(
                "status",
                ""
            )

            if status == "Collected":

                st.success(
                    "♻ Collected"
                )

            elif status == "Accepted":

                st.info(
                    "🟢 Accepted"
                )

            elif status == "Rejected":

                st.error(
                    "🔴 Rejected"
                )

    st.markdown("---")

    st.success(
        "🌱 Thank you for supporting sustainable waste collection."
    )