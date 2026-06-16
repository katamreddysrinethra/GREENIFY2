import streamlit as st

# ==========================================================
# DATABASE INITIALIZATION
# ==========================================================

from utils.database import initialize_database

initialize_database()

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="GREENIFY",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# IMPORT PAGES
# ==========================================================

from pages.landing import show_landing_page
from pages.login import show_login_page
from pages.register import show_register_page
from pages.dashboard import show_dashboard

# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():

    try:

        with open(
            "styles/style.css",
            "r",
            encoding="utf-8"
        ) as file:

            st.markdown(
                f"<style>{file.read()}</style>",
                unsafe_allow_html=True
            )

    except FileNotFoundError:

        st.warning(
            "styles/style.css not found."
        )


load_css()

# ==========================================================
# SESSION STATE
# ==========================================================

DEFAULT_SESSION = {

    "page": "landing",

    "logged_in": False,

    "user_id": "",

    "user_name": "",

    "user_email": "",

    "role": "",

    "address": "",

    "mobile": ""

}

for key, value in DEFAULT_SESSION.items():

    if key not in st.session_state:

        st.session_state[key] = value

# ==========================================================
# VALID ROLES
# ==========================================================

VALID_ROLES = [

    "Citizen",

    "Waste Collector",

    "Market Partner"

]

# ==========================================================
# LOGOUT
# ==========================================================

def logout():

    st.session_state.clear()

    st.rerun()

# ==========================================================
# TOP BAR
# ==========================================================

def render_topbar():

    if not st.session_state.get(
        "logged_in",
        False
    ):
        return

    col1, col2, col3 = st.columns(
        [7, 2, 1]
    )

    with col1:

        st.markdown(
            """
            <h2 style='color:#2E7D32'>
            🌱 GREENIFY
            </h2>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.write(
            f"👤 {st.session_state.get('user_name','User')}"
        )

        st.caption(
            st.session_state.get(
                "role",
                ""
            )
        )

    with col3:

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            logout()

# ==========================================================
# FOOTER
# ==========================================================

def render_footer():

    st.markdown(
        """
        <br><br>

        <hr>

        <div style="text-align:center">

        🌱 GREENIFY

        <br>

        Smart Waste Management Platform

        <br><br>

        ♻ Reduce • Recycle • Reward ♻

        <br><br>

        Built for a Cleaner & Greener Future

        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================================
# ROUTER
# ==========================================================

def app_router():

    # ------------------------------------------------------
    # LOGGED-IN USER
    # ------------------------------------------------------

    if st.session_state.logged_in:

        # Session validation

        if not st.session_state.user_id:

            logout()
            return

        # Role validation

        if (

            st.session_state.role

            and

            st.session_state.role not in VALID_ROLES

        ):

            st.error(
                "Invalid role detected."
            )

            logout()

            return

        render_topbar()

        try:

            show_dashboard()

        except Exception as e:

            st.error(
                f"Dashboard Error: {e}"
            )

        return

    # ------------------------------------------------------
    # PUBLIC PAGES
    # ------------------------------------------------------

    page = st.session_state.page

    if page == "landing":

        show_landing_page()

    elif page == "login":

        show_login_page()

    elif page == "register":

        show_register_page()

    else:

        st.session_state.page = "landing"

        st.rerun()

# ==========================================================
# MAIN
# ==========================================================

app_router()

render_footer()