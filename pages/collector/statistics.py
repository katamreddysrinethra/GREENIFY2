import streamlit as st
import pandas as pd
import plotly.express as px

from utils.database import (
    PICKUPS_FILE,
    load_data
)

# ==========================================================
# COLLECTOR STATISTICS PAGE
# ==========================================================

def show_collector_statistics():

    st.title("📊 Collection Statistics")

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
            "No collection data available."
        )

        return

    st.markdown("---")

    # ======================================================
    # METRICS
    # ======================================================

    total_pickups = len(
        collector_pickups
    )

    completed_pickups = len([

        pickup

        for pickup in collector_pickups

        if pickup.get("status")
        == "Collected"

    ])

    accepted_pickups = len([

        pickup

        for pickup in collector_pickups

        if pickup.get("status")
        == "Accepted"

    ])

    total_weight = sum(

        float(
            pickup.get(
                "quantity",
                0
            )
        )

        for pickup in collector_pickups

        if pickup.get("status")
        == "Collected"

    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📦 Total Pickups",
            total_pickups
        )

    with col2:
        st.metric(
            "♻ Completed",
            completed_pickups
        )

    with col3:
        st.metric(
            "🟢 Accepted",
            accepted_pickups
        )

    with col4:
        st.metric(
            "⚖ Total Weight (KG)",
            round(
                total_weight,
                2
            )
        )

    st.markdown("---")

    # ======================================================
    # WASTE TYPE DISTRIBUTION
    # ======================================================

    st.subheader(
        "🗑 Waste Type Distribution"
    )

    waste_data = {}

    for pickup in collector_pickups:

        waste_type = pickup.get(
            "waste_type",
            "Unknown"
        )

        waste_data[
            waste_type
        ] = waste_data.get(
            waste_type,
            0
        ) + 1

    waste_df = pd.DataFrame({

        "Waste Type":
        list(
            waste_data.keys()
        ),

        "Count":
        list(
            waste_data.values()
        )

    })

    if not waste_df.empty:

        pie_chart = px.pie(
            waste_df,
            names="Waste Type",
            values="Count",
            title="Waste Collection Distribution"
        )

        st.plotly_chart(
            pie_chart,
            use_container_width=True
        )

    st.markdown("---")

    # ======================================================
    # COLLECTION TREND
    # ======================================================

    st.subheader(
        "📈 Collection Trend"
    )

    date_counts = {}

    for pickup in collector_pickups:

        date = pickup.get(
            "pickup_date",
            "Unknown"
        )

        date_counts[
            date
        ] = date_counts.get(
            date,
            0
        ) + 1

    trend_df = pd.DataFrame({

        "Date":
        list(
            date_counts.keys()
        ),

        "Pickups":
        list(
            date_counts.values()
        )

    })

    if not trend_df.empty:

        trend_chart = px.line(
            trend_df,
            x="Date",
            y="Pickups",
            markers=True,
            title="Pickup Activity Trend"
        )

        st.plotly_chart(
            trend_chart,
            use_container_width=True
        )

    st.markdown("---")

    # ======================================================
    # STATUS BREAKDOWN
    # ======================================================

    st.subheader(
        "📊 Status Overview"
    )

    status_counts = {}

    for pickup in collector_pickups:

        status = pickup.get(
            "status",
            "Unknown"
        )

        status_counts[
            status
        ] = status_counts.get(
            status,
            0
        ) + 1

    status_df = pd.DataFrame({

        "Status":
        list(
            status_counts.keys()
        ),

        "Count":
        list(
            status_counts.values()
        )

    })

    if not status_df.empty:

        bar_chart = px.bar(
            status_df,
            x="Status",
            y="Count",
            title="Pickup Status Distribution"
        )

        st.plotly_chart(
            bar_chart,
            use_container_width=True
        )

    st.markdown("---")

    # ======================================================
    # PERFORMANCE SCORE
    # ======================================================

    st.subheader(
        "⭐ Performance Score"
    )

    score = min(
        100,
        completed_pickups * 5
    )

    st.progress(
        score / 100
    )

    st.write(
        f"Performance Score: {score}/100"
    )

    if score >= 80:

        st.success(
            "Excellent collection performance!"
        )

    elif score >= 50:

        st.info(
            "Good performance. Keep going!"
        )

    else:

        st.warning(
            "Accept and complete more pickups to improve your score."
        )

    st.markdown("---")

    st.success(
        "🌱 Every completed pickup contributes to a cleaner environment."
    )