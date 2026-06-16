import json
import os


# ==========================================================
# ENSURE FILE EXISTS
# ==========================================================

def ensure_file(file_path, default_data=None):

    if default_data is None:
        default_data = []

    directory = os.path.dirname(file_path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    if not os.path.exists(file_path):

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                default_data,
                file,
                indent=4
            )


# ==========================================================
# LOAD JSON DATA
# ==========================================================

def load_data(file_path):

    ensure_file(file_path)

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except json.JSONDecodeError:

        return []

    except Exception:

        return []


# ==========================================================
# SAVE JSON DATA
# ==========================================================

def save_data(file_path, data):

    ensure_file(file_path)

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


# ==========================================================
# APPEND RECORD
# ==========================================================

def append_data(file_path, record):

    data = load_data(file_path)

    data.append(record)

    save_data(file_path, data)


# ==========================================================
# FIND RECORD
# ==========================================================

def find_record(
    file_path,
    key,
    value
):

    data = load_data(file_path)

    for record in data:

        if record.get(key) == value:
            return record

    return None


# ==========================================================
# UPDATE RECORD
# ==========================================================

def update_record(
    file_path,
    key,
    value,
    updated_data
):

    data = load_data(file_path)

    updated = False

    for i, record in enumerate(data):

        if record.get(key) == value:

            data[i].update(updated_data)

            updated = True

            break

    save_data(file_path, data)

    return updated


# ==========================================================
# DELETE RECORD
# ==========================================================

def delete_record(
    file_path,
    key,
    value
):

    data = load_data(file_path)

    filtered_data = [

        item
        for item in data
        if item.get(key) != value

    ]

    save_data(
        file_path,
        filtered_data
    )

    return True


# ==========================================================
# FILTER RECORDS
# ==========================================================

def filter_records(
    file_path,
    key,
    value
):

    data = load_data(file_path)

    return [

        record
        for record in data
        if record.get(key) == value

    ]


# ==========================================================
# COUNT RECORDS
# ==========================================================

def count_records(file_path):

    data = load_data(file_path)

    return len(data)


import json
import os

# ==========================================================
# FILE PATH CONSTANTS
# ==========================================================

USERS_FILE = "data/users.json"

PICKUPS_FILE = "data/pickups.json"

REWARDS_FILE = "data/rewards.json"

COMPLAINTS_FILE = "data/complaints.json"

MARKET_FILE = "data/market_listings.json"

SCAN_HISTORY_FILE = "data/scan_history.json"

COLLECTOR_STATS_FILE = "data/collector_stats.json"

COLLECTED_WASTE_FILE = "data/collected_waste.json"

PURCHASES_FILE = "data/purchases.json"

# ==========================================================
# ENSURE FILE EXISTS
# ==========================================================

def ensure_file(
    file_path,
    default_data=None
):

    if default_data is None:

        default_data = []

    directory = os.path.dirname(
        file_path
    )

    if directory:

        os.makedirs(
            directory,
            exist_ok=True
        )

    if not os.path.exists(
        file_path
    ):

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                default_data,
                file,
                indent=4
            )

# ==========================================================
# LOAD DATA
# ==========================================================

def load_data(file_path):

    ensure_file(file_path)

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except json.JSONDecodeError:

        return []

    except Exception:

        return []

# ==========================================================
# SAVE DATA
# ==========================================================

def save_data(
    file_path,
    data
):

    ensure_file(file_path)

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

# ==========================================================
# APPEND RECORD
# ==========================================================

def append_data(
    file_path,
    record
):

    data = load_data(
        file_path
    )

    data.append(record)

    save_data(
        file_path,
        data
    )

# ==========================================================
# FIND RECORD
# ==========================================================

def find_record(
    file_path,
    key,
    value
):

    data = load_data(
        file_path
    )

    for record in data:

        if record.get(key) == value:

            return record

    return None

# ==========================================================
# UPDATE RECORD
# ==========================================================

def update_record(
    file_path,
    key,
    value,
    updated_data
):

    data = load_data(
        file_path
    )

    updated = False

    for i, record in enumerate(data):

        if record.get(key) == value:

            data[i].update(
                updated_data
            )

            updated = True

            break

    save_data(
        file_path,
        data
    )

    return updated

# ==========================================================
# DELETE RECORD
# ==========================================================

def delete_record(
    file_path,
    key,
    value
):

    data = load_data(
        file_path
    )

    filtered_data = [

        item

        for item in data

        if item.get(key) != value

    ]

    save_data(
        file_path,
        filtered_data
    )

    return True

# ==========================================================
# FILTER RECORDS
# ==========================================================

def filter_records(
    file_path,
    key,
    value
):

    data = load_data(
        file_path
    )

    return [

        record

        for record in data

        if record.get(key) == value

    ]

# ==========================================================
# COUNT RECORDS
# ==========================================================

def count_records(
    file_path
):

    data = load_data(
        file_path
    )

    return len(data)

# ==========================================================
# GENERATE NEXT ID
# ==========================================================

def generate_id(
    file_path
):

    data = load_data(
        file_path
    )

    return len(data) + 1

# ==========================================================
# INITIALIZE DATABASE FILES
# ==========================================================

def initialize_database():

    files = [

        USERS_FILE,

        PICKUPS_FILE,

        REWARDS_FILE,

        COMPLAINTS_FILE,

        MARKET_FILE,

        SCAN_HISTORY_FILE,

        COLLECTOR_STATS_FILE,

        COLLECTED_WASTE_FILE,

        PURCHASES_FILE

    ]

    for file in files:

        ensure_file(file)

# ==========================================================
# AUTO INITIALIZATION
# ==========================================================

initialize_database()