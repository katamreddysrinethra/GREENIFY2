import streamlit as st

from utils.database import (
    PICKUPS_FILE,
    load_data,
    save_data
)

# ==========================================================
# UPDATE PICKUP STATUS
# ==========================================================

def update_pickup_status(
    pickup_id,
    status
):

    pickups = load_data(
        PICKUPS_FILE
    )

    collector_id = st.session_state.get(
        "user_id",
        ""
    )

    collector_name = st.session_state.get(
        "user_name",
        ""
    )

    for pickup in pickups:

        if pickup.get(
            "pickup_id"
        ) == pickup_id:

            pickup["status"] = status

            if status in [
                "Accepted",
                "Collected"
            ]:

                pickup[
                    "collector_id"
                ] = collector_id

                pickup[
                    "collector_name"
                ] = collector_name

            break

    save_data(
        PICKUPS_FILE,
        pickups
    )


# ==========================================================
# MANAGE PICKUPS PAGE
# ==========================================================

def show_manage_pickups():

    st.title(
        "📦 Manage Pickup Requests"
    )

    st.markdown(
        """
        Review citizen pickup requests
        and update their status.
        """
    )

    st.markdown("---")

    pickups = load_data(
        PICKUPS_FILE
    )

    if not pickups:

        st.info(
            "No pickup requests found."
        )

        return

    # ======================================================
    # FILTERS
    # ======================================================

    status_filter = st.selectbox(

        "Filter By Status",

        [
            "All",
            "Pending",
            "Accepted",
            "Collected",
            "Rejected"
        ]

    )

    if status_filter != "All":

        pickups = [

            pickup

            for pickup in pickups

            if pickup.get("status")
            == status_filter

        ]

    st.markdown("---")

    # ======================================================
    # REQUEST CARDS
    # ======================================================

    for pickup in reversed(
        pickups
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
                f"📧 Email: "
                f"{pickup.get('email','')}"
            )

            st.write(
                f"📱 Mobile: "
                f"{pickup.get('mobile','')}"
            )

            st.write(
                f"🗑 Waste Type: "
                f"{pickup.get('waste_type','')}"
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
                f"📅 Pickup Date: "
                f"{pickup.get('pickup_date','')}"
            )

            st.write(
                f"⏰ Pickup Time: "
                f"{pickup.get('pickup_time','')}"
            )

            status = pickup.get(
                "status",
                "Pending"
            )

            st.write(
                f"📊 Current Status: {status}"
            )

            st.markdown("---")

            # =============================================
            # PENDING REQUESTS
            # =============================================

            if status == "Pending":

                col1, col2 = st.columns(2)

                with col1:

                    if st.button(
                        f"✅ Accept {pickup['pickup_id']}",
                        key=f"accept_{pickup['pickup_id']}"
                    ):

                        update_pickup_status(
                            pickup[
                                "pickup_id"
                            ],
                            "Accepted"
                        )

                        st.success(
                            "Pickup Accepted"
                        )

                        st.rerun()

                with col2:

                    if st.button(
                        f"❌ Reject {pickup['pickup_id']}",
                        key=f"reject_{pickup['pickup_id']}"
                    ):

                        update_pickup_status(
                            pickup[
                                "pickup_id"
                            ],
                            "Rejected"
                        )

                        st.warning(
                            "Pickup Rejected"
                        )

                        st.rerun()

            # =============================================
            # ACCEPTED REQUESTS
            # =============================================

            elif status == "Accepted":

                if st.button(
                    f"♻ Mark Collected {pickup['pickup_id']}",
                    key=f"collect_{pickup['pickup_id']}"
                ):

                    update_pickup_status(
                        pickup[
                            "pickup_id"
                        ],
                        "Collected"
                    )

                    st.success(
                        "Marked as Collected"
                    )

                    st.rerun()

            # =============================================
            # COMPLETED STATES
            # =============================================

            elif status == "Collected":

                st.success(
                    "♻ Pickup Completed"
                )

            elif status == "Rejected":

                st.error(
                    "❌ Request Rejected"
                )

    st.markdown("---")

    st.success(
        "🌱 Efficient waste collection helps build sustainable communities."
    )