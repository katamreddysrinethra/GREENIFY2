import streamlit as st

from utils.auth import register_user


# ==========================================================
# REGISTER PAGE
# ==========================================================

def show_register_page():

    st.markdown(
        """
        <div class="form-container">
            <div class="form-title">
                📝 Create Your GREENIFY Account
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    with st.form(
        "register_form",
        clear_on_submit=False
    ):

        name = st.text_input(
            "👤 Full Name"
        )

        email = st.text_input(
            "📧 Email Address"
        )

        password = st.text_input(
            "🔒 Password",
            type="password"
        )

        confirm_password = st.text_input(
            "🔐 Confirm Password",
            type="password"
        )

        role = st.selectbox(
            "🎭 Select Role",
            [
                "Citizen",
                "Waste Collector",
                "Market Partner"
            ]
        )

        address = st.text_area(
            "📍 Address"
        )

        mobile = st.text_input(
            "📱 Mobile Number"
        )

        submit = st.form_submit_button(
            "✅ Register"
        )

        if submit:

            # =====================================
            # VALIDATION
            # =====================================

            if not name.strip():

                st.error(
                    "Please enter your name."
                )

                return

            if not email.strip():

                st.error(
                    "Please enter email."
                )

                return

            if not password:

                st.error(
                    "Please enter password."
                )

                return

            if password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

                return

            if len(password) < 6:

                st.error(
                    "Password must be at least 6 characters."
                )

                return

            if not address.strip():

                st.error(
                    "Please enter address."
                )

                return

            if not mobile.strip():

                st.error(
                    "Please enter mobile number."
                )

                return

            # =====================================
            # REGISTER USER
            # =====================================

            success, message = register_user(
                name=name,
                email=email,
                password=password,
                role=role,
                address=address,
                mobile=mobile
            )

            if success:

                st.success(
                    "🎉 Registration Successful!"
                )

                st.info(
                    "Redirecting to Login..."
                )

                st.session_state.page = "login"

                st.rerun()

            else:

                st.error(message)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        if st.button(
            "🔐 Already Have An Account? Login",
            use_container_width=True
        ):

            st.session_state.page = "login"

            st.rerun()