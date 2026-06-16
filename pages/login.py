import streamlit as st

from utils.auth import login_user


# ==========================================================
# LOGIN PAGE
# ==========================================================

def show_login_page():

    st.markdown(
        """
        <div class="form-container">
            <div class="form-title">
                🔐 Login To GREENIFY
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    with st.form(
        "login_form",
        clear_on_submit=False
    ):

        email = st.text_input(
            "📧 Email Address"
        )

        password = st.text_input(
            "🔒 Password",
            type="password"
        )

        login_button = st.form_submit_button(
            "🚀 Login"
        )

        if login_button:

            if not email.strip():

                st.error(
                    "Please enter your email."
                )
                return

            if not password:

                st.error(
                    "Please enter your password."
                )
                return

            success, result = login_user(
                email,
                password
            )

            if success:

                user = result

                # =====================================
                # SESSION STATE
                # =====================================

                st.session_state.logged_in = True

                st.session_state.user_id = user["user_id"]

                st.session_state.user_name = user["name"]

                st.session_state.user_email = user["email"]

                st.session_state.role = user["role"]

                st.session_state.address = user["address"]

                st.session_state.mobile = user["mobile"]

                st.session_state.page = "dashboard"

                st.success(
                    f"Welcome back, {user['name']}! 🌱"
                )

                st.rerun()

            else:

                st.error(result)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        if st.button(
            "📝 Create New Account",
            use_container_width=True
        ):

            st.session_state.page = "register"

            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style='text-align:center;color:gray;'>

        ♻ Join GREENIFY and contribute to a cleaner future.

        </div>
        """,
        unsafe_allow_html=True
    )