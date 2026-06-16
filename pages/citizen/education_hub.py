import streamlit as st


# ==========================================================
# EDUCATION HUB PAGE
# ==========================================================

def show_education_hub():

    st.title("📚 Education Hub")

    st.markdown(
        """
        Learn how to properly segregate waste,
        recycle effectively, and contribute to
        a cleaner environment.
        """
    )

    st.markdown("---")

    # ======================================================
    # WASTE SEGREGATION
    # ======================================================

    st.header("♻ Waste Segregation Guide")

    tab1, tab2, tab3, tab4 = st.tabs([
        "🟢 Wet Waste",
        "🔵 Dry Waste",
        "💻 E-Waste",
        "☣ Hazardous Waste"
    ])

    with tab1:

        st.subheader("🟢 Wet Waste")

        st.markdown(
            """
            Wet waste includes biodegradable materials.

            Examples:

            • Food scraps

            • Fruit peels

            • Vegetable waste

            • Garden waste

            Disposal:

            Use Green Bin
            """
        )

    with tab2:

        st.subheader("🔵 Dry Waste")

        st.markdown(
            """
            Dry waste includes recyclable materials.

            Examples:

            • Plastic bottles

            • Paper

            • Cardboard

            • Glass

            • Metal cans

            Disposal:

            Use Blue Bin
            """
        )

    with tab3:

        st.subheader("💻 E-Waste")

        st.markdown(
            """
            Electronic waste includes:

            • Mobile phones

            • Chargers

            • Computers

            • Batteries

            • Electronic accessories

            Disposal:

            Send to authorized recycling centers.
            """
        )

    with tab4:

        st.subheader("☣ Hazardous Waste")

        st.markdown(
            """
            Hazardous waste includes:

            • Medical waste

            • Chemicals

            • Paints

            • Pesticides

            • Fluorescent bulbs

            Disposal:

            Follow municipal hazardous waste guidelines.
            """
        )

    st.markdown("---")

    # ======================================================
    # BIN COLOR GUIDE
    # ======================================================

    st.header("🗑 Bin Color Guide")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.success(
            """
            🟢 Green Bin

            Wet Waste
            """
        )

    with col2:
        st.info(
            """
            🔵 Blue Bin

            Dry Waste
            """
        )

    with col3:
        st.warning(
            """
            🟡 Yellow Bin

            Biomedical Waste
            """
        )

    with col4:
        st.error(
            """
            🔴 Red Bin

            Hazardous Waste
            """
        )

    st.markdown("---")

    # ======================================================
    # RECYCLING TIPS
    # ======================================================

    st.header("🌍 Sustainability Tips")

    tips = [

        "Carry reusable water bottles.",

        "Avoid single-use plastics.",

        "Separate waste at source.",

        "Reuse containers whenever possible.",

        "Donate old electronics responsibly.",

        "Compost biodegradable waste.",

        "Reduce paper consumption.",

        "Use cloth bags instead of plastic bags."

    ]

    for tip in tips:

        st.success(
            f"✅ {tip}"
        )

    st.markdown("---")

    # ======================================================
    # RECYCLING PROCESS
    # ======================================================

    st.header("♻ How Recycling Works")

    st.markdown(
        """
        1️⃣ Waste Collection

        2️⃣ Waste Segregation

        3️⃣ Recycling Facility Processing

        4️⃣ Material Recovery

        5️⃣ Manufacturing New Products

        6️⃣ Reduced Environmental Impact
        """
    )

    st.markdown("---")

    # ======================================================
    # QUIZ SECTION
    # ======================================================

    st.header("🧠 Quick Waste Segregation Quiz")

    answer = st.radio(
        "Where should a plastic bottle be disposed?",
        [
            "Green Bin",
            "Blue Bin",
            "Red Bin",
            "Yellow Bin"
        ]
    )

    if st.button("Submit Answer"):

        if answer == "Blue Bin":

            st.success(
                "Correct! Plastic bottles belong in the Blue Bin."
            )

        else:

            st.error(
                "Incorrect. Plastic bottles should be placed in the Blue Bin."
            )

    st.markdown("---")

    # ======================================================
    # FACTS
    # ======================================================

    st.header("🌱 Did You Know?")

    st.info(
        "Recycling one aluminum can saves enough energy to power a television for several hours."
    )

    st.info(
        "Plastic can take hundreds of years to decompose naturally."
    )

    st.info(
        "Proper waste segregation significantly improves recycling efficiency."
    )

    st.markdown("---")

    st.success(
        "📚 Knowledge is the first step towards sustainability."
    )