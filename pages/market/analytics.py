import streamlit as st
import pandas as pd
import plotly.express as px

from utils.database import (
    MARKET_FILE,
    load_data
)

# ==========================================================
# MARKET ANALYTICS PAGE
# ==========================================================

def show_market_analytics():

    st.title("📊 Marketplace Analytics")

    listings = load_data(
        MARKET_FILE
    )

    if not listings:

        st.info(
            "No marketplace data available."
        )

        return

    st.markdown("---")

    # ======================================================
    # SUMMARY METRICS
    # ======================================================

    total_listings = len(
        listings
    )

    active_listings = len([

        listing

        for listing in listings

        if listing.get(
            "status"
        ) == "Active"

    ])

    inactive_listings = len([

        listing

        for listing in listings

        if listing.get(
            "status"
        ) == "Inactive"

    ])

    avg_price = round(

        sum(
            float(
                listing.get(
                    "price_per_kg",
                    0
                )
            )
            for listing in listings
        )

        / max(
            total_listings,
            1
        ),

        2

    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "📋 Total Listings",
            total_listings
        )

    with col2:

        st.metric(
            "🟢 Active",
            active_listings
        )

    with col3:

        st.metric(
            "🔴 Inactive",
            inactive_listings
        )

    with col4:

        st.metric(
            "💰 Avg Price/KG",
            f"₹{avg_price}"
        )

    st.markdown("---")

    # ======================================================
    # WASTE DEMAND DISTRIBUTION
    # ======================================================

    st.subheader(
        "♻ Waste Demand Distribution"
    )

    waste_counts = {}

    for listing in listings:

        waste_type = listing.get(
            "waste_type",
            "Unknown"
        )

        waste_counts[
            waste_type
        ] = waste_counts.get(
            waste_type,
            0
        ) + 1

    waste_df = pd.DataFrame({

        "Waste Type":
        list(
            waste_counts.keys()
        ),

        "Count":
        list(
            waste_counts.values()
        )

    })

    pie_chart = px.pie(
        waste_df,
        names="Waste Type",
        values="Count",
        title="Marketplace Demand by Waste Type"
    )

    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )

    st.markdown("---")

    # ======================================================
    # PRICE ANALYSIS
    # ======================================================

    st.subheader(
        "💰 Price Analysis"
    )

    price_df = pd.DataFrame({

        "Waste Type": [

            listing.get(
                "waste_type",
                ""
            )

            for listing in listings

        ],

        "Price": [

            listing.get(
                "price_per_kg",
                0
            )

            for listing in listings

        ]

    })

    bar_chart = px.bar(
        price_df,
        x="Waste Type",
        y="Price",
        title="Price Per KG by Waste Type"
    )

    st.plotly_chart(
        bar_chart,
        use_container_width=True
    )

    st.markdown("---")

    # ======================================================
    # QUANTITY DEMAND
    # ======================================================

    st.subheader(
        "⚖ Quantity Demand Analysis"
    )

    quantity_df = pd.DataFrame({

        "Waste Type": [

            listing.get(
                "waste_type",
                ""
            )

            for listing in listings

        ],

        "Quantity": [

            listing.get(
                "quantity",
                0
            )

            for listing in listings

        ]

    })

    quantity_chart = px.bar(
        quantity_df,
        x="Waste Type",
        y="Quantity",
        title="Required Quantity by Waste Type"
    )

    st.plotly_chart(
        quantity_chart,
        use_container_width=True
    )

    st.markdown("---")

    # ======================================================
    # MARKET INSIGHTS
    # ======================================================

    st.subheader(
        "📈 Market Insights"
    )

    highest_demand = max(
        waste_counts,
        key=waste_counts.get
    )

    st.success(
        f"Most Requested Waste Type: {highest_demand}"
    )

    st.info(
        f"Average Marketplace Price: ₹{avg_price}/KG"
    )

    st.success(
        "Monitor waste demand trends to optimize pricing and sourcing strategies."
    )

    st.markdown("---")

    st.success(
        "🌍 A thriving recycling marketplace supports a strong circular economy."
    )