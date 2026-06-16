import streamlit as st
import pandas as pd
from utils.database import (
    load_data,
    save_data,
    COLLECTED_WASTE_FILE
)


def show_manage_inventory():

    st.title("♻ Waste Inventory")

    st.markdown(
        """
        Add collected recyclable waste
        and make it available for
        direct purchase by market partners.
        """
    )

    inventory = load_data(
        COLLECTED_WASTE_FILE
    )

    st.subheader("➕ Add Waste")

    waste_type = st.selectbox(
        "Waste Type",
        [
            "Plastic",
            "Paper",
            "Glass",
            "Metal",
            "E-Waste",
            "Organic"
        ]
    )

    quantity = st.number_input(
        "Quantity (KG)",
        min_value=1.0
    )

    price = st.number_input(
        "Expected Price per KG",
        min_value=1.0
    )

    location = st.text_input(
        "Storage Location"
    )

    if st.button("Add Inventory"):

        inventory.append({

            "inventory_id":
            len(inventory) + 1,

            "collector_id":
            st.session_state.get(
                "user_id"
            ),

            "collector_name":
            st.session_state.get(
                "user_name"
            ),

            "waste_type":
            waste_type,

            "quantity":
            quantity,

            "price":
            price,

            "location":
            location,

            "status":
            "Available"

        })

        save_data(
            COLLECTED_WASTE_FILE,
            inventory
        )

        st.success(
            "Inventory Added Successfully"
        )

        st.rerun()

    st.markdown("---")

    st.subheader("📦 Current Inventory")

    if inventory:

        df = pd.DataFrame(inventory)

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No inventory added yet."
        )