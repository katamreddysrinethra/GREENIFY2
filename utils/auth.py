import bcrypt
from datetime import datetime

from utils.database import (
    USERS_FILE,
    load_data,
    save_data,
    find_record
)

# ==========================================================
# PASSWORD HASHING
# ==========================================================

def hash_password(password):

    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


# ==========================================================
# VERIFY PASSWORD
# ==========================================================

def verify_password(
    password,
    hashed_password
):

    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


# ==========================================================
# CHECK EMAIL EXISTS
# ==========================================================

def email_exists(email):

    users = load_data(USERS_FILE)

    for user in users:

        if user["email"].lower() == email.lower():
            return True

    return False


# ==========================================================
# GENERATE USER ID
# ==========================================================

def generate_user_id():

    users = load_data(USERS_FILE)

    return f"USR{len(users)+1:04d}"


# ==========================================================
# REGISTER USER
# ==========================================================

def register_user(
    name,
    email,
    password,
    role,
    address,
    mobile
):

    if email_exists(email):

        return (
            False,
            "Email already registered."
        )

    users = load_data(USERS_FILE)

    user = {

        "user_id": generate_user_id(),

        "name": name,

        "email": email,

        "password": hash_password(password),

        "role": role,

        "address": address,

        "mobile": mobile,

        "green_points": 0,

        "badges": [],

        "created_at":
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    users.append(user)

    save_data(
        USERS_FILE,
        users
    )

    return (
        True,
        "Registration successful."
    )


# ==========================================================
# LOGIN USER
# ==========================================================

def login_user(
    email,
    password
):

    users = load_data(USERS_FILE)

    for user in users:

        if (
            user["email"].lower()
            == email.lower()
        ):

            if verify_password(
                password,
                user["password"]
            ):

                return (
                    True,
                    user
                )

            return (
                False,
                "Incorrect password."
            )

    return (
        False,
        "Account not found."
    )


# ==========================================================
# GET USER BY EMAIL
# ==========================================================

def get_user_by_email(email):

    users = load_data(USERS_FILE)

    for user in users:

        if (
            user["email"].lower()
            == email.lower()
        ):
            return user

    return None


# ==========================================================
# GET USER BY ID
# ==========================================================

def get_user_by_id(user_id):

    users = load_data(USERS_FILE)

    for user in users:

        if user["user_id"] == user_id:
            return user

    return None


# ==========================================================
# UPDATE USER POINTS
# ==========================================================

def update_green_points(
    user_id,
    points
):

    users = load_data(USERS_FILE)

    for user in users:

        if user["user_id"] == user_id:

            user["green_points"] += points

            save_data(
                USERS_FILE,
                users
            )

            return True

    return False


# ==========================================================
# ADD BADGE
# ==========================================================

def add_badge(
    user_id,
    badge
):

    users = load_data(USERS_FILE)

    for user in users:

        if user["user_id"] == user_id:

            if badge not in user["badges"]:

                user["badges"].append(
                    badge
                )

                save_data(
                    USERS_FILE,
                    users
                )

            return True

    return False


# ==========================================================
# GET ALL USERS
# ==========================================================

def get_all_users():

    return load_data(
        USERS_FILE
    )


# ==========================================================
# GET USERS BY ROLE
# ==========================================================

def get_users_by_role(role):

    users = load_data(
        USERS_FILE
    )

    return [

        user
        for user in users

        if user["role"] == role

    ]