import streamlit as st
from streamlit_option_menu import option_menu

# ==========================================================
# CITIZEN MODULES
# ==========================================================

from pages.citizen.citizen_home import show_citizen_home
from pages.citizen.ai_scanner import show_ai_scanner
from pages.citizen.pickup_request import show_pickup_request
from pages.citizen.pickup_history import show_pickup_history
from pages.citizen.rewards import show_rewards
from pages.citizen.environmental_impact import show_environmental_impact
from pages.citizen.education_hub import show_education_hub
from pages.citizen.complaints import show_complaints

# ==========================================================
# COLLECTOR MODULES
# ==========================================================

from pages.collector.collector_home import show_collector_home
from pages.collector.manage_pickups import show_manage_pickups
from pages.collector.pickup_history import show_collector_history
from pages.collector.statistics import show_collector_statistics
from pages.collector.manage_inventory import show_manage_inventory

# ==========================================================
# MARKET MODULES
# ==========================================================

from pages.market.market_home import show_market_home
from pages.market.create_listing import show_create_listing
from pages.market.listings import show_listings
from pages.market.analytics import show_market_analytics
from pages.market.direct_purchase import show_direct_purchase

# ==========================================================
# CITIZEN DASHBOARD
# ==========================================================

def citizen_dashboard():

    with st.sidebar:

        selected = option_menu(
            menu_title="🌱 Citizen Portal",
            options=[
                "Home",
                "AI Scanner",
                "Request Pickup",
                "Pickup History",
                "Rewards",
                "Environmental Impact",
                "Education Hub",
                "Complaints"
            ],
            icons=[
                "house",
                "camera",
                "truck",
                "clock-history",
                "gift",
                "globe",
                "book",
                "exclamation-circle"
            ],
            default_index=0
        )

    if selected == "Home":
        show_citizen_home()

    elif selected == "AI Scanner":
        show_ai_scanner()

    elif selected == "Request Pickup":
        show_pickup_request()

    elif selected == "Pickup History":
        show_pickup_history()

    elif selected == "Rewards":
        show_rewards()

    elif selected == "Environmental Impact":
        show_environmental_impact()

    elif selected == "Education Hub":
        show_education_hub()

    elif selected == "Complaints":
        show_complaints()


# ==========================================================
# COLLECTOR DASHBOARD
# ==========================================================

def collector_dashboard():

    with st.sidebar:

        selected = option_menu(
            menu_title="🚛 Collector Portal",
            options=[
                "Home",
                "Manage Pickups",
                "Waste Inventory",
                "Pickup History",
                "Statistics"
            ],
            icons=[
                "house",
                "truck",
                "boxes",
                "clock-history",
                "bar-chart"
            ],
            default_index=0
        )

    if selected == "Home":
        show_collector_home()

    elif selected == "Manage Pickups":
        show_manage_pickups()

    elif selected == "Waste Inventory":
        show_manage_inventory()    

    elif selected == "Pickup History":
        show_collector_history()

    elif selected == "Statistics":
        show_collector_statistics()


# ==========================================================
# MARKET DASHBOARD
# ==========================================================

def market_dashboard():

    with st.sidebar:

        selected = option_menu(
            menu_title="🏪 Market Portal",
            options=[
                "Home",
                "Create Listing",
                "Listings",
                "Analytics",
                "Direct Purchase"
            ],
            icons=[
                "house",
                "plus-circle",
                "list-ul",
                "graph-up",
                "cart-plus"
            ],
            default_index=0
        )

    if selected == "Home":
        show_market_home()

    elif selected == "Create Listing":
        show_create_listing()

    elif selected == "Listings":
        show_listings()

    elif selected == "Analytics":
        show_market_analytics()

    elif selected == "Direct Purchase":
        show_direct_purchase()


# ==========================================================
# MAIN ROUTER
# ==========================================================
with st.sidebar:
    st.title("GREENIFY")
    st.write("Sidebar Test")
    
def show_dashboard():

    role = st.session_state.get("role")

    if role == "Citizen":

        citizen_dashboard()

    elif role == "Waste Collector":

        collector_dashboard()

    elif role == "Market Partner":

        market_dashboard()

    else:

        st.error(
            "Invalid user role detected."
        )