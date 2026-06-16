import streamlit as st
from datetime import datetime

from utils.database import (
    MARKET_FILE,
    load_data,
    save_data
)

# ==========================================================
# GENERATE LISTING ID
# ==========================================================

def generate_listing_id():

    listings = load_data(
        MARKET_FILE
    )

    return f"LST{len(listings)+1:04d}"


# ==========================================================
# SAVE LISTING
# ==========================================================

def save_listing(record):

    listings = load_data(
        MARKET_FILE
    )

    listings.append(record)

    save_data(
        MARKET_FILE,
        listings
    )


# ==========================================================
# CREATE LISTING PAGE
# ==========================================================

def show_create_listing():

    st.title("➕ Create Waste Listing")

    st.markdown(
        """
        Create a marketplace listing for waste
        materials you want to purchase.
        """
    )

    st.markdown("---")

    with st.form(
        "create_listing_form"
    ):

        waste_type = st.selectbox(
            "♻ Waste Type",
            [
                "Plastic",
                "Paper",
                "Glass",
                "Metal",
                "Organic Waste",
                "E-Waste",
                "Mixed Waste"
            ]
        )

        price_per_kg = st.number_input(
            "💰 Price Per KG (₹)",
            min_value=1.0,
            step=1.0
        )

        quantity = st.number_input(
            "⚖ Quantity Required (KG)",
            min_value=1.0,
            step=1.0
        )

        description = st.text_area(
            "📝 Description"
        )

        contact_number = st.text_input(
            "📞 Contact Number"
        )

        submit = st.form_submit_button(
            "🚀 Create Listing"
        )

        if submit:

            if not description.strip():

                st.error(
                    "Please enter a description."
                )

                return

            if not contact_number.strip():

                st.error(
                    "Please enter a contact number."
                )

                return

            listing_record = {

                "listing_id":
                generate_listing_id(),

                "partner_id":
                st.session_state.get(
                    "user_id",
                    ""
                ),

                "partner_name":
                st.session_state.get(
                    "user_name",
                    ""
                ),

                "waste_type":
                waste_type,

                "price_per_kg":
                price_per_kg,

                "quantity":
                quantity,

                "description":
                description,

                "contact_number":
                contact_number,

                "status":
                "Active",

                "created_at":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            }

            save_listing(
                listing_record
            )

            st.success(
                "✅ Listing created successfully."
            )

            st.info(
                f"Listing ID: "
                f"{listing_record['listing_id']}"
            )

    st.markdown("---")

    st.success(
        "🌱 Waste marketplaces help build a strong circular economy."
    )