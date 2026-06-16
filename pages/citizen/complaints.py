import streamlit as st
from datetime import datetime

from utils.database import (
    COMPLAINTS_FILE,
    load_data,
    save_data
)

# ==========================================================
# GENERATE COMPLAINT ID
# ==========================================================

def generate_complaint_id():

    complaints = load_data(
        COMPLAINTS_FILE
    )

    return f"CMP{len(complaints)+1:04d}"


# ==========================================================
# SAVE COMPLAINT
# ==========================================================

def save_complaint(record):

    complaints = load_data(
        COMPLAINTS_FILE
    )

    complaints.append(record)

    save_data(
        COMPLAINTS_FILE,
        complaints
    )


# ==========================================================
# GET USER COMPLAINTS
# ==========================================================

def get_user_complaints():

    user_id = st.session_state.get(
        "user_id",
        ""
    )

    complaints = load_data(
        COMPLAINTS_FILE
    )

    return [

        complaint

        for complaint in complaints

        if complaint.get(
            "user_id"
        ) == user_id

    ]


# ==========================================================
# COMPLAINTS PAGE
# ==========================================================

def show_complaints():

    st.title("⚠ Complaints & Support")

    st.markdown(
        """
        Report issues related to waste collection,
        pickups, rewards, marketplace activities,
        or any other GREENIFY services.
        """
    )

    st.markdown("---")

    # ======================================================
    # SUBMIT COMPLAINT
    # ======================================================

    st.subheader(
        "📝 Submit Complaint"
    )

    with st.form(
        "complaint_form"
    ):

        category = st.selectbox(
            "Complaint Category",
            [
                "Missed Pickup",
                "Late Pickup",
                "Collector Behavior",
                "Rewards Issue",
                "AI Scanner Issue",
                "Marketplace Issue",
                "App Technical Problem",
                "Other"
            ]
        )

        subject = st.text_input(
            "Subject"
        )

        description = st.text_area(
            "Describe Your Issue"
        )

        uploaded_image = st.file_uploader(
            "Upload Supporting Image (Optional)",
            type=[
                "jpg",
                "jpeg",
                "png"
            ]
        )

        submit = st.form_submit_button(
            "🚀 Submit Complaint"
        )

        if submit:

            if not subject.strip():

                st.error(
                    "Please enter a subject."
                )

                return

            if not description.strip():

                st.error(
                    "Please enter a description."
                )

                return

            image_name = ""

            if uploaded_image:

                image_name = uploaded_image.name

            complaint_record = {

                "complaint_id":
                generate_complaint_id(),

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

                "category":
                category,

                "subject":
                subject,

                "description":
                description,

                "image":
                image_name,

                "status":
                "Open",

                "created_at":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            }

            save_complaint(
                complaint_record
            )

            st.success(
                "✅ Complaint submitted successfully."
            )

            st.info(
                f"Complaint ID: "
                f"{complaint_record['complaint_id']}"
            )

    st.markdown("---")

    # ======================================================
    # COMPLAINT HISTORY
    # ======================================================

    st.subheader(
        "📋 My Complaints"
    )

    complaints = get_user_complaints()

    if not complaints:

        st.info(
            "No complaints submitted yet."
        )

        return

    for complaint in reversed(
        complaints
    ):

        with st.expander(

            f"{complaint['complaint_id']} "
            f"- "
            f"{complaint['subject']}"

        ):

            st.write(
                f"📂 Category: "
                f"{complaint['category']}"
            )

            st.write(
                f"📝 Description: "
                f"{complaint['description']}"
            )

            status = complaint.get(
                "status",
                "Open"
            )

            if status == "Open":

                st.warning(
                    "🟡 Open"
                )

            elif status == "In Progress":

                st.info(
                    "🔵 In Progress"
                )

            elif status == "Resolved":

                st.success(
                    "🟢 Resolved"
                )

            else:

                st.error(
                    f"🔴 {status}"
                )

            st.write(
                f"🕒 Submitted On: "
                f"{complaint['created_at']}"
            )

    st.markdown("---")

    # ======================================================
    # SUPPORT INFORMATION
    # ======================================================

    st.subheader(
        "📞 Support Information"
    )

    st.info(
        "For urgent issues, contact the GREENIFY support team."
    )

    st.success(
        "🌱 We are committed to improving your waste management experience."
    )