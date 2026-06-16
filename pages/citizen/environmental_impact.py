import streamlit as st
import pandas as pd
import plotly.express as px

from utils.database import (
    SCAN_HISTORY_FILE,
    PICKUPS_FILE,
    load_data
)

# ==========================================================
# IMPACT CALCULATIONS
# ==========================================================

def calculate_impact():

    user_id = st.session_state.get(
        "user_id",
        ""
    )

    scans = load_data(
        SCAN_HISTORY_FILE
    )

    pickups = load_data(
        PICKUPS_FILE
    )

    user_scans = [

        scan

        for scan in scans

        if scan.get("user_id")
        == user_id

    ]

    user_pickups = [

        pickup

        for pickup in pickups

        if pickup.get("user_id")
        == user_id

    ]

    total_scans = len(
        user_scans
    )

    total_pickups = len(
        user_pickups
    )

    co2_saved = round(
        total_scans * 0.2,
        2
    )

    waste_recycled = round(
        total_pickups * 2.5,
        2
    )

    trees_saved = round(
        co2_saved / 21,
        2
    )

    sustainability_score = min(
        100,
        total_scans * 2 +
        total_pickups * 5
    )

    return {

        "scans":
        total_scans,

        "pickups":
        total_pickups,

        "co2":
        co2_saved,

        "waste":
        waste_recycled,

        "trees":
        trees_saved,

        "score":
        sustainability_score

    }


# ==========================================================
# ENVIRONMENTAL IMPACT PAGE
# ==========================================================

def show_environmental_impact():

    st.title(
        "🌍 Environmental Impact"
    )

    st.markdown(
        """
        Track your contribution
        towards a cleaner and
        greener environment.
        """
    )

    st.markdown("---")

    stats = calculate_impact()

    # ======================================================
    # METRICS
    # ======================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🌱 CO₂ Saved",
            f"{stats['co2']} kg"
        )

    with col2:

        st.metric(
            "♻ Waste Recycled",
            f"{stats['waste']} kg"
        )

    with col3:

        st.metric(
            "🌳 Trees Saved",
            stats["trees"]
        )

    with col4:

        st.metric(
            "⭐ Sustainability Score",
            f"{stats['score']}/100"
        )

    st.markdown("---")

    # ======================================================
    # IMPACT DISTRIBUTION
    # ======================================================

    st.subheader(
        "📊 Sustainability Breakdown"
    )

    impact_df = pd.DataFrame({

        "Category": [

            "CO₂ Saved",
            "Waste Recycled",
            "Trees Saved"

        ],

        "Value": [

            stats["co2"],
            stats["waste"],
            stats["trees"]

        ]

    })

    pie_chart = px.pie(
        impact_df,
        names="Category",
        values="Value",
        title="Environmental Contributions"
    )

    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )

    st.markdown("---")

    # ======================================================
    # ACTIVITY CHART
    # ======================================================

    st.subheader(
        "📈 Activity Overview"
    )

    activity_df = pd.DataFrame({

        "Activity": [

            "Waste Scans",
            "Pickup Requests"

        ],

        "Count": [

            stats["scans"],
            stats["pickups"]

        ]

    })

    bar_chart = px.bar(
        activity_df,
        x="Activity",
        y="Count",
        title="Your GREENIFY Activity"
    )

    st.plotly_chart(
        bar_chart,
        use_container_width=True
    )

    st.markdown("---")

    # ======================================================
    # SUSTAINABILITY SCORE
    # ======================================================

    st.subheader(
        "⭐ Sustainability Score"
    )

    score = stats["score"]

    st.progress(
        score / 100
    )

    st.write(
        f"Current Score: {score}/100"
    )

    if score >= 80:

        st.success(
            "Excellent environmental contribution!"
        )

    elif score >= 50:

        st.info(
            "Good progress. Keep recycling!"
        )

    else:

        st.warning(
            "Start scanning and recycling more waste to increase your impact."
        )

    st.markdown("---")

    # ======================================================
    # ENVIRONMENTAL INSIGHTS
    # ======================================================

    st.subheader(
        "💡 Environmental Insights"
    )

    st.info(
        f"You have helped prevent approximately "
        f"{stats['co2']} kg of CO₂ emissions."
    )

    st.info(
        f"You have contributed to recycling "
        f"{stats['waste']} kg of waste."
    )

    st.info(
        f"Your efforts are equivalent to saving "
        f"{stats['trees']} trees."
    )

    st.markdown("---")

    st.success(
        "🌍 Every action matters. Thank you for helping build a sustainable future."
    )