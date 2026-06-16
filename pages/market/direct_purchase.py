import streamlit as st
import pandas as pd

from utils.database import (
    load_data,
    save_data,
    COLLECTED_WASTE_FILE,
    PURCHASES_FILE
)


def show_direct_purchase():

    st.title("🛒 Direct Waste Marketplace")

    st.markdown(
        """
        Buy recyclable waste directly
        from registered waste collectors.
        """
    )

    inventory = load_data(
        COLLECTED_WASTE_FILE
    )

    if not inventory:

        st.info(
            "No waste available for purchase."
        )
        return

    st.subheader("♻ Available Waste")

    for item in inventory:

        if item.get("status") != "Available":
            continue

        with st.container():

            col1, col2, col3 = st.columns([4,2,2])

            with col1:

                st.markdown(
                    f"""
                    ### {item['waste_type']}

                    👤 Collector:
                    {item['collector_name']}

                    📍 Location:
                    {item['location']}
                    """
                )

            with col2:

                st.metric(
                    "Quantity",
                    f"{item['quantity']} KG"
                )

                st.metric(
                    "Price/KG",
                    f"₹{item['price']}"
                )

            with col3:

                total_price = (
                    item["quantity"]
                    * item["price"]
                )

                st.metric(
                    "Total Price",
                    f"₹{total_price}"
                )

                if st.button(
                    f"💰 Buy Now #{item['inventory_id']}"
                ):

                    purchases = load_data(
                        PURCHASES_FILE
                    )

                    purchases.append({

                        "purchase_id":
                        len(purchases) + 1,

                        "inventory_id":
                        item["inventory_id"],

                        "collector_name":
                        item["collector_name"],

                        "market_partner":
                        st.session_state.get(
                            "user_name"
                        ),

                        "waste_type":
                        item["waste_type"],

                        "quantity":
                        item["quantity"],

                        "price":
                        item["price"],

                        "total_price":
                        total_price

                    })

                    for waste in inventory:

                        if (
                            waste["inventory_id"]
                            ==
                            item["inventory_id"]
                        ):

                            waste["status"] = "Sold"

                    save_data(
                        PURCHASES_FILE,
                        purchases
                    )

                    save_data(
                        COLLECTED_WASTE_FILE,
                        inventory
                    )

                    st.success(
                        "Purchase Successful!"
                    )

                    st.rerun()

        st.markdown("---")

    st.subheader("📦 Purchase History")

    purchases = load_data(
        PURCHASES_FILE
    )

    partner_name = st.session_state.get(
        "user_name"
    )

    partner_purchases = [

        p

        for p in purchases

        if p.get(
            "market_partner"
        )
        ==
        partner_name

    ]

    if partner_purchases:

        st.dataframe(
            pd.DataFrame(
                partner_purchases
            ),
            use_container_width=True
        )

    else:

        st.info(
            "No purchases yet."
        )