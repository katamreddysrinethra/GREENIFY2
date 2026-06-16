import streamlit as st
from datetime import datetime

from utils.image_classifier import (
    analyze_waste_image
)

from utils.database import (
    SCAN_HISTORY_FILE,
    load_data,
    save_data
)

# ==========================================================
# SAVE SCAN HISTORY
# ==========================================================

def save_scan_history(scan_record):

    scans = load_data(
        SCAN_HISTORY_FILE
    )

    scans.append(scan_record)

    save_data(
        SCAN_HISTORY_FILE,
        scans
    )

# ==========================================================
# AI SCANNER PAGE
# ==========================================================

def show_ai_scanner():

    st.title("📸 AI Waste Scanner")

    st.markdown(
        """
        Upload a waste image and let AI identify:

        ✅ Waste Type

        ✅ Waste Category

        ✅ Recyclable Status

        ✅ Correct Disposal Method

        ✅ Reward Points

        ✅ Environmental Impact
        """
    )

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "📷 Upload Waste Image",
        type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )

    if uploaded_file is not None:

        st.image(
            uploaded_file,
            caption="Uploaded Waste Image",
            use_container_width=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "🔍 Analyze Waste",
            use_container_width=True
        ):

            with st.spinner(
                "Analyzing image using AI..."
            ):

                result = analyze_waste_image(
                    uploaded_file
                )

            # =====================================
            # SUCCESS
            # =====================================

            if result["success"]:

                data = result["data"]

                st.success(
                    "Waste Successfully Identified!"
                )

                st.markdown("---")

                col1, col2 = st.columns(2)

                with col1:

                    st.info(
                        f"🗑 Waste Type: "
                        f"{data['waste_type']}"
                    )

                    st.info(
                        f"📂 Category: "
                        f"{data['category']}"
                    )

                    st.info(
                        f"♻ Recyclable: "
                        f"{data['recyclable']}"
                    )

                with col2:

                    st.info(
                        f"🟦 Bin Color: "
                        f"{data['bin_color']}"
                    )

                    st.info(
                        f"🎁 Reward Points: "
                        f"{data['reward_points']}"
                    )

                st.markdown("---")

                st.subheader(
                    "🌍 Environmental Impact"
                )

                st.success(
                    data[
                        "environmental_impact"
                    ]
                )

                st.markdown("---")

                st.subheader(
                    "📋 Disposal Instructions"
                )

                st.warning(
                    data[
                        "disposal_instructions"
                    ]
                )

                # =====================================
                # SAVE SCAN HISTORY
                # =====================================

                scan_record = {

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

                    "waste_type":
                    data["waste_type"],

                    "category":
                    data["category"],

                    "recyclable":
                    data["recyclable"],

                    "bin_color":
                    data["bin_color"],

                    "reward_points":
                    data["reward_points"],

                    "environmental_impact":
                    data[
                        "environmental_impact"
                    ],

                    "timestamp":
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                }

                save_scan_history(
                    scan_record
                )

                st.success(
                    "📁 Scan saved to history."
                )

            # =====================================
            # ERROR
            # =====================================

            else:

                st.error(
                    result["message"]
                )

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.subheader("💡 Tips")

    st.markdown(
        """
        - Clean images produce better results.
        - Capture one waste item at a time.
        - Ensure proper lighting.
        - Avoid blurry photos.
        - Follow the disposal guidance provided.
        """
    )