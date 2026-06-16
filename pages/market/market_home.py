import streamlit as st

from utils.database import (
    MARKET_FILE,
    load_data
)

# ==========================================================
# MARKET HOME PAGE
# ==========================================================

def show_market_home():

    st.title("🏪 Market Dashboard")

    user_name = st.session_state.get(
        "user_name",
        "Market Partner"
    )

    st.markdown(
        f"""
        Welcome **{user_name}**!

        Manage waste listings, monitor market demand,
        and contribute to the circular economy.
        """
    )

    st.markdown("---")

    listings = load_data(
        MARKET_FILE
    )

    # ======================================================
    # STATISTICS
    # ======================================================

    total_listings = len(
        listings
    )

    active_listings = len([

        listing

        for listing in listings

        if listing.get(
            "status",
            "Active"
        ) == "Active"

    ])

    waste_types = len(

        set(

            listing.get(
                "waste_type",
                ""
            )

            for listing in listings

        )

    )

    total_quantity = sum(

        float(
            listing.get(
                "quantity",
                0
            )
        )

        for listing in listings

    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📋 Listings",
            total_listings
        )

    with col2:
        st.metric(
            "🟢 Active",
            active_listings
        )

    with col3:
        st.metric(
            "♻ Waste Types",
            waste_types
        )

    with col4:
        st.metric(
            "⚖ Total Quantity",
            round(
                total_quantity,
                2
            )
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
                <h3>➕ Create Listing</h3>
                <p>
                Add new waste purchase requirements.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="dashboard-card">
                <h3>📃 Listings</h3>
                <p>
                Manage active marketplace listings.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="dashboard-card">
                <h3>📊 Analytics</h3>
                <p>
                View market trends and demand analysis.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # ======================================================
    # RECENT LISTINGS
    # ======================================================

    st.subheader(
        "📋 Recent Listings"
    )

    recent_listings = listings[-5:]

    if not recent_listings:

        st.info(
            "No listings available."
        )

    else:

        for listing in reversed(
            recent_listings
        ):

            with st.expander(

                f"{listing.get('listing_id','')} "
                f"- "
                f"{listing.get('waste_type','')}"

            ):

                st.write(
                    f"🗑 Waste Type: "
                    f"{listing.get('waste_type','')}"
                )

                st.write(
                    f"💰 Price/KG: ₹"
                    f"{listing.get('price_per_kg','')}"
                )

                st.write(
                    f"⚖ Quantity Required: "
                    f"{listing.get('quantity','')} KG"
                )

                st.write(
                    f"📞 Contact: "
                    f"{listing.get('contact_number','')}"
                )

                st.write(
                    f"📊 Status: "
                    f"{listing.get('status','Active')}"
                )

    st.markdown("---")

    # ======================================================
    # MARKET INSIGHTS
    # ======================================================

    st.subheader(
        "💡 Market Insights"
    )

    st.success(
        "Monitor waste demand trends regularly."
    )

    st.success(
        "Maintain competitive pricing."
    )

    st.success(
        "Update listings frequently."
    )

    st.success(
        "Promote sustainable recycling markets."
    )

    st.markdown("---")

    st.info(
        "🌍 Circular economy initiatives help maximize resource utilization."
    )