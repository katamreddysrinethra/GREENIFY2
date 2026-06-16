import streamlit as st
from datetime import datetime

from utils.database import (
    PICKUPS_FILE,
    load_data,
    save_data
)

# ==========================================================
# GENERATE PICKUP ID
# ==========================================================

def generate_pickup_id():

    pickups = load_data(
        PICKUPS_FILE
    )

    return f"PICKUP{len(pickups)+1:04d}"


# ==========================================================
# SAVE PICKUP REQUEST
# ==========================================================

def save_pickup_request(record):

    pickups = load_data(
        PICKUPS_FILE
    )

    pickups.append(record)

    save_data(
        PICKUPS_FILE,
        pickups
    )


# ==========================================================
# PICKUP REQUEST PAGE
# ==========================================================

def show_pickup_request():

    st.title("🚛 Request Waste Pickup")

    st.markdown(
        """
        Schedule a pickup and our registered
        waste collectors will handle the rest.
        """
    )

    st.markdown("---")

    with st.form("pickup_request_form"):

        waste_type = st.selectbox(
            "🗑 Waste Type",
            [
                "Plastic",
                "Paper",
                "Glass",
                "Metal",
                "Organic Waste",
                "E-Waste",
                "Mixed Waste",
                "Hazardous Waste"
            ]
        )

        quantity = st.number_input(
            "⚖ Quantity (KG)",
            min_value=1.0,
            step=0.5
        )

        address = st.text_area(
            "📍 Pickup Address",
            value=st.session_state.get(
                "address",
                ""
            )
        )

        pickup_date = st.date_input(
            "📅 Preferred Pickup Date"
        )

        pickup_time = st.time_input(
            "⏰ Preferred Pickup Time"
        )

        uploaded_image = st.file_uploader(
            "📸 Upload Waste Image (Optional)",
            type=[
                "jpg",
                "jpeg",
                "png"
            ]
        )

        submit = st.form_submit_button(
            "✅ Submit Pickup Request"
        )

        if submit:

            if not address.strip():

                st.error(
                    "Please provide a pickup address."
                )

                return

            image_name = ""

            if uploaded_image is not None:

                image_name = uploaded_image.name

            pickup_record = {

                "pickup_id":
                generate_pickup_id(),

                "user_id":
                st.session_state.get(
                    "user_id",
                    ""
                ),

                "user_name":
                st.session_state.get(
                    "user_name",
                    ""
                ),

                "email":
                st.session_state.get(
                    "user_email",
                    ""
                ),

                "mobile":
                st.session_state.get(
                    "mobile",
                    ""
                ),

                "waste_type":
                waste_type,

                "quantity":
                quantity,

                "address":
                address,

                "pickup_date":
                str(pickup_date),

                "pickup_time":
                str(pickup_time),

                "image":
                image_name,

                "status":
                "Pending",

                "collector_id":
                "",

                "collector_name":
                "",

                "requested_at":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            }

            save_pickup_request(
                pickup_record
            )

            st.success(
                "🎉 Pickup request submitted successfully!"
            )

            st.info(
                f"Request ID: {pickup_record['pickup_id']}"
            )

    st.markdown("---")

    st.subheader("📋 Pickup Process")

    st.markdown(
        """
        1️⃣ Submit Pickup Request

        2️⃣ Waste Collector Reviews Request

        3️⃣ Request Accepted or Rejected

        4️⃣ Waste Collected

        5️⃣ Rewards & Environmental Impact Updated
        """
    )

    st.markdown("---")

    st.success(
        "♻ Proper waste disposal helps keep our communities clean and sustainable."
    )