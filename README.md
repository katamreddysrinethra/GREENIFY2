 🌱 GREENIFY

## Smart Waste Management & Recycling Platform

GREENIFY is a Streamlit-powered smart waste management platform that connects citizens, waste collectors, and recycling markets through a unified digital ecosystem.

The platform encourages responsible waste disposal, efficient waste collection, recycling awareness, and participation in the circular economy through AI-powered waste identification, reward systems, and waste trading.

---

# 🚀 Key Features

## 👨‍👩‍👧 Citizen Interface

### 📸 AI Waste Scanner

Upload or capture an image of waste.

The AI scanner automatically identifies:

* Plastic Waste
* Paper Waste
* Glass Waste
* Metal Waste
* Organic Waste
* E-Waste
* Hazardous Waste
* Biomedical Waste

The scanner provides:

* Waste Type
* Waste Category
* Recyclable / Non-Recyclable Status
* Recommended Bin Color
* Disposal Instructions
* Reward Points
* Environmental Impact Information

---

### 🚛 Pickup Requests

Citizens can:

* Request waste pickups
* Upload waste images
* Select preferred pickup times
* Track request status

Status Types:

* Pending
* Accepted
* Rejected
* Collected

---

### 📜 Pickup History

View:

* Pickup Date
* Waste Type
* Quantity
* Collector Details
* Pickup Status

---

### 🎁 Rewards & Gamification

Citizens earn Green Points for proper waste segregation.

Reward Examples:

| Waste Type | Points |
| ---------- | ------ |
| Plastic    | 10     |
| Paper      | 5      |
| Glass      | 8      |
| Metal      | 15     |
| E-Waste    | 20     |

Badges:

* 🌱 Eco Beginner
* ♻ Recycling Champion
* 🏆 Green Hero
* 🌍 Sustainability Leader

Leaderboard rankings are also available.

---

### 🌍 Environmental Impact Dashboard

Track:

* CO₂ Saved
* Waste Recycled
* Trees Saved
* Landfill Reduction
* Recycling Accuracy

Interactive charts are powered by Plotly.

---

### 📚 Education Hub

Provides educational content about:

* Wet Waste
* Dry Waste
* Plastic Waste
* E-Waste
* Glass Waste
* Metal Waste
* Hazardous Waste

Includes:

* Images
* Infographics
* Segregation Guides
* Recycling Tips
* Awareness Articles

---

### ⚠ Complaint Management

Citizens can:

* Raise complaints
* Upload supporting images
* Track complaint status

---

# 🚛 Waste Collector Interface

Collectors can:

* View Pickup Requests
* Accept Requests
* Reject Requests
* Mark Pickups as Completed
* View Pickup History
* Track Collection Statistics

Analytics include:

* Total Pickups
* Daily Collections
* Monthly Collections
* Waste Category Distribution

---

# 🏪 Market Interface

Market partners can:

* Create Waste Listings
* Publish Waste Prices
* Update Listings
* Track Transactions
* View Demand Analytics

Examples:

| Waste Type | Price/kg |
| ---------- | -------- |
| Plastic    | ₹25      |
| Paper      | ₹12      |
| Metal      | ₹40      |
| Glass      | ₹15      |

---

# 🤖 AI Waste Scanner

GREENIFY uses Google's Gemini Vision API to classify waste images.

Workflow:

Citizen Uploads Image
↓
Gemini Vision Analysis
↓
Waste Identification
↓
Segregation Guidance
↓
Reward Allocation
↓
Environmental Impact Calculation
↓
Scan History Storage

Output Example:

Detected Waste:
Plastic Bottle

Category:
Recyclable Plastic

Recommended Bin:
Blue Bin

Reward:
+10 Green Points

Environmental Impact:
0.2 kg CO₂ prevented

---

# 🏗 Project Structure

```text
GREENIFY/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   ├── logo.png
│   ├── landing_bg.jpg
│   ├── citizen_banner.png
│   ├── collector_banner.png
│   ├── market_banner.png
│   ├── recycle.png
│   ├── rewards.png
│   └── waste_scan.png
│
├── styles/
│   └── style.css
│
├── pages/
│   ├── landing.py
│   ├── login.py
│   ├── register.py
│   ├── dashboard.py
│   │
│   ├── citizen/
│   │   ├── citizen_home.py
│   │   ├── ai_scanner.py
│   │   ├── pickup_request.py
│   │   ├── pickup_history.py
│   │   ├── rewards.py
│   │   ├── complaints.py
│   │   ├── environmental_impact.py
│   │   └── education_hub.py
│   │
│   ├── collector/
│   │   ├── collector_home.py
│   │   ├── manage_pickups.py
│   │   ├── pickup_history.py
│   │   └── statistics.py
│   │
│   └── market/
│       ├── market_home.py
│       ├── create_listing.py
│       ├── listings.py
│       ├── analytics.py
│       └── transactions.py
│
├── utils/
│   ├── auth.py
│   ├── database.py
│   ├── image_classifier.py
│   ├── rewards.py
│   ├── impact.py
│   ├── notifications.py
│   └── helpers.py
│
├── data/
│   ├── users.json
│   ├── pickups.json
│   ├── rewards.json
│   ├── complaints.json
│   ├── market_listings.json
│   ├── collector_stats.json
│   └── scan_history.json
│
└── models/
    └── categories.json
```

---

# 🎨 Theme Colors

Primary: #2E7D32

Secondary: #4CAF50

Accent: #81C784

Background: #F4FFF4

Text: #1B5E20

---

# 🔐 Authentication

Registration Fields:

* Full Name
* Email
* Password
* Role
* Address
* Mobile Number

Supported Roles:

1. Citizen
2. Waste Collector
3. Market Partner

After login, users are automatically redirected to their respective dashboards.

---

# 📊 Analytics & Reporting

GREENIFY supports:

* Interactive Charts
* Waste Statistics
* Pickup Analytics
* Reward Tracking
* Environmental Impact Reports

Export Formats:

* Excel
* PDF

---

# ▶ Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 🌱 GREENIFY Vision

Reduce Waste.

Increase Recycling.

Reward Sustainability.

Build a Cleaner and Greener Future Together.