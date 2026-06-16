import streamlit as st
import pandas as pd

from utils.database import (
    MARKET_FILE,
    load_data,
    save_data
)

# ==========================================================
# UPDATE LISTING STATUS
# ==========================================================

def update_listing_status(
    listing_id,
    new_status
):

    listings = load_data(
        MARKET_FILE
    )

    for listing in listings:

        if listing.get(
            "listing_id"
        ) == listing_id:

            listing[
                "status"
            ] = new_status

            break

    save_data(
        MARKET_FILE,
        listings
    )


# ==========================================================
# LISTINGS PAGE
# ==========================================================

def show_listings():

    st.title("📃 Marketplace Listings")

    listings = load_data(
        MARKET_FILE
    )

    if not listings:

        st.info(
            "No listings available."
        )

        return

    st.markdown("---")

    # ======================================================
    # FILTERS
    # ======================================================

    waste_types = sorted(

        list(

            set(

                listing.get(
                    "waste_type",
                    ""
                )

                for listing in listings

            )

        )

    )

    waste_types.insert(
        0,
        "All"
    )

    waste_filter = st.selectbox(
        "♻ Filter by Waste Type",
        waste_types
    )

    status_filter = st.selectbox(
        "📊 Filter by Status",
        [
            "All",
            "Active",
            "Inactive"
        ]
    )

    filtered = listings

    if waste_filter != "All":

        filtered = [

            listing

            for listing in filtered

            if listing.get(
                "waste_type"
            ) == waste_filter

        ]

    if status_filter != "All":

        filtered = [

            listing

            for listing in filtered

            if listing.get(
                "status"
            ) == status_filter

        ]

    st.markdown("---")

    # ======================================================
    # TABLE
    # ======================================================

    table_data = []

    for listing in filtered:

        table_data.append({

            "Listing ID":
            listing.get(
                "listing_id",
                ""
            ),

            "Waste Type":
            listing.get(
                "waste_type",
                ""
            ),

            "Price/KG":
            listing.get(
                "price_per_kg",
                ""
            ),

            "Quantity":
            listing.get(
                "quantity",
                ""
            ),

            "Partner":
            listing.get(
                "partner_name",
                ""
            ),

            "Status":
            listing.get(
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
    # DETAILED VIEW
    # ======================================================

    st.subheader(
        "📋 Listing Details"
    )

    current_user = st.session_state.get(
        "user_id",
        ""
    )

    for listing in reversed(
        filtered
    ):

        with st.expander(

            f"{listing['listing_id']} "
            f"- "
            f"{listing['waste_type']}"

        ):

            st.write(
                f"♻ Waste Type: "
                f"{listing.get('waste_type','')}"
            )

            st.write(
                f"💰 Price/KG: ₹"
                f"{listing.get('price_per_kg','')}"
            )

            st.write(
                f"⚖ Quantity: "
                f"{listing.get('quantity','')} KG"
            )

            st.write(
                f"📝 Description: "
                f"{listing.get('description','')}"
            )

            st.write(
                f"👤 Partner: "
                f"{listing.get('partner_name','')}"
            )

            st.write(
                f"📞 Contact: "
                f"{listing.get('contact_number','')}"
            )

            st.write(
                f"📊 Status: "
                f"{listing.get('status','')}"
            )

            st.write(
                f"🕒 Created: "
                f"{listing.get('created_at','')}"
            )

            # ==========================================
            # OWNER CONTROLS
            # ==========================================

            if listing.get(
                "partner_id"
            ) == current_user:

                st.markdown("---")

                col1, col2 = st.columns(2)

                with col1:

                    if st.button(

                        f"🟢 Activate "
                        f"{listing['listing_id']}",

                        key=f"active_"
                        f"{listing['listing_id']}"

                    ):

                        update_listing_status(
                            listing[
                                "listing_id"
                            ],
                            "Active"
                        )

                        st.success(
                            "Listing Activated"
                        )

                        st.rerun()

                with col2:

                    if st.button(

                        f"🔴 Deactivate "
                        f"{listing['listing_id']}",

                        key=f"inactive_"
                        f"{listing['listing_id']}"

                    ):

                        update_listing_status(
                            listing[
                                "listing_id"
                            ],
                            "Inactive"
                        )

                        st.warning(
                            "Listing Deactivated"
                        )

                        st.rerun()

    st.markdown("---")

    st.success(
        "🌍 Recycling markets encourage sustainable resource utilization."
    )