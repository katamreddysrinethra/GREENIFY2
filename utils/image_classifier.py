import json
import io
from PIL import Image
import google.generativeai as genai
import streamlit as st


# ==========================================================
# GEMINI CONFIGURATION
# ==========================================================

def configure_gemini():

    try:

        api_key = st.secrets["GEMINI_API_KEY"]

        genai.configure(
            api_key=api_key
        )

        return True

    except Exception:

        return False


# ==========================================================
# LOAD GEMINI MODEL
# ==========================================================

def get_model():

    return genai.GenerativeModel(
        "gemini-2.5-flash"
    )


# ==========================================================
# WASTE ANALYSIS
# ==========================================================

def analyze_waste_image(uploaded_file):

    if not configure_gemini():

        return {
            "success": False,
            "message":
            "Gemini API key not configured."
        }

    try:

        image = Image.open(uploaded_file)

        prompt = """
You are an expert waste segregation assistant.

Analyze the uploaded waste image.

Return ONLY valid JSON.

Format:

{
    "waste_type":"",
    "category":"",
    "recyclable":"",
    "bin_color":"",
    "reward_points":"",
    "environmental_impact":"",
    "disposal_instructions":""
}

Rules:

1. waste_type:
Plastic Bottle, Paper, Glass, Metal Can,
Organic Waste, E-Waste, Battery,
Medical Waste, Mixed Waste etc.

2. category:
Dry Waste
Wet Waste
E-Waste
Hazardous Waste
Biomedical Waste

3. recyclable:
Yes or No

4. bin_color:
Blue
Green
Red
Yellow
Black

5. reward_points:
integer only

6. environmental_impact:
short statement

7. disposal_instructions:
short practical instruction
"""

        model = get_model()

        response = model.generate_content(
            [
                prompt,
                image
            ]
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace(
                "```json",
                ""
            ).replace(
                "```",
                ""
            ).strip()

        result = json.loads(text)

        return {
            "success": True,
            "data": result
        }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }


# ==========================================================
# REWARD CALCULATOR
# ==========================================================

def calculate_reward_points(
    waste_type
):

    rewards = {

        "Plastic Bottle": 10,
        "Plastic": 10,

        "Paper": 5,

        "Glass": 8,

        "Metal Can": 15,
        "Metal": 15,

        "E-Waste": 20,

        "Battery": 25,

        "Organic Waste": 3
    }

    return rewards.get(
        waste_type,
        5
    )


# ==========================================================
# BADGE SYSTEM
# ==========================================================

def determine_badge(
    total_points
):

    if total_points >= 1000:
        return "🌍 Sustainability Leader"

    if total_points >= 500:
        return "🏆 Green Hero"

    if total_points >= 250:
        return "♻ Recycling Champion"

    if total_points >= 50:
        return "🌱 Eco Beginner"

    return None