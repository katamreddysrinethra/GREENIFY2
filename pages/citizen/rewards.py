import streamlit as st

from utils.auth import get_user_by_id


# ==========================================================
# REWARD LEVELS
# ==========================================================

BADGE_LEVELS = [

    {
        "points": 50,
        "badge": "🌱 Eco Beginner"
    },

    {
        "points": 250,
        "badge": "♻ Recycling Champion"
    },

    {
        "points": 500,
        "badge": "🏆 Green Hero"
    },

    {
        "points": 1000,
        "badge": "🌍 Sustainability Leader"
    }

]


# ==========================================================
# GET NEXT BADGE
# ==========================================================

def get_next_badge(points):

    for level in BADGE_LEVELS:

        if points < level["points"]:

            return level

    return None


# ==========================================================
# REWARDS PAGE
# ==========================================================

def show_rewards():

    st.title("🎁 Rewards & Achievements")

    user_id = st.session_state.get(
        "user_id"
    )

    user = get_user_by_id(
        user_id
    )

    if not user:

        st.error(
            "User data not found."
        )
        return

    points = user.get(
        "green_points",
        0
    )

    badges = user.get(
        "badges",
        []
    )

    # ======================================================
    # POINTS CARD
    # ======================================================

    st.metric(
        "🌱 Total Green Points",
        points
    )

    st.markdown("---")

    # ======================================================
    # BADGES
    # ======================================================

    st.subheader(
        "🏆 Earned Badges"
    )

    if badges:

        cols = st.columns(
            min(4, len(badges))
        )

        for idx, badge in enumerate(
            badges
        ):

            with cols[
                idx % len(cols)
            ]:

                st.success(
                    badge
                )

    else:

        st.info(
            "No badges earned yet."
        )

    st.markdown("---")

    # ======================================================
    # PROGRESS
    # ======================================================

    st.subheader(
        "📈 Progress To Next Badge"
    )

    next_badge = get_next_badge(
        points
    )

    if next_badge:

        target = next_badge[
            "points"
        ]

        progress = min(
            points / target,
            1.0
        )

        st.progress(
            progress
        )

        st.write(
            f"Current: {points} Points"
        )

        st.write(
            f"Target: {target} Points"
        )

        st.info(
            f"Next Badge: {next_badge['badge']}"
        )

    else:

        st.success(
            "🎉 Highest Badge Achieved!"
        )

    st.markdown("---")

    # ======================================================
    # ACHIEVEMENT LEVEL
    # ======================================================

    st.subheader(
        "⭐ Achievement Level"
    )

    if points >= 1000:

        level = "Sustainability Leader"

    elif points >= 500:

        level = "Green Hero"

    elif points >= 250:

        level = "Recycling Champion"

    elif points >= 50:

        level = "Eco Beginner"

    else:

        level = "Starter"

    st.success(
        f"Current Level: {level}"
    )

    st.markdown("---")

    # ======================================================
    # LEADERBOARD PLACEHOLDER
    # ======================================================

    st.subheader(
        "🏅 Community Leaderboard"
    )

    st.info(
        "Leaderboard will display top GREENIFY users based on Green Points."
    )

    st.markdown("---")

    # ======================================================
    # HOW TO EARN
    # ======================================================

    st.subheader(
        "💡 How To Earn Points"
    )

    st.markdown(
        """
        📸 Scan waste correctly

        🚛 Complete pickup requests

        ♻ Segregate recyclable waste

        🌍 Participate in sustainability initiatives

        📚 Complete educational activities
        """
    )

    st.success(
        "Every action contributes to a cleaner environment and earns rewards."
    )