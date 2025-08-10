"""Streamlit app for UI of nutritional crew."""

import os

import dotenv
import streamlit as st

from health.data_schemas import UserInfo
from health.main import run

dotenv.load_dotenv()


def app() -> None:
    """Run the main Streamlit application."""
    st.set_page_config(page_title="Personalized Nutrition Advisor", page_icon="🥗", layout="wide")

    st.title("🥗 Personalized Nutrition Advisor")
    st.markdown("""
    Get a detailed nutrition plan based on your demographics, health conditions, and preferences.
    Our AI team of nutrition specialists will create a personalized recommendation just for you.
    """)

    # Create tabs for organization
    tab1, tab2, tab3 = st.tabs(["Basic Information", "Health Details", "Preferences & Lifestyle"])

    with tab1:
        st.header("Personal Information")
        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input("Age", min_value=1, max_value=120, value=30)
            gender = st.selectbox("Gender", ["Male", "Female", "Non-binary/Other"])
            height = st.text_input("Height (e.g., 5'10\" or 178 cm)", "5'10\"")

        with col2:
            weight = st.text_input("Weight (e.g., 160 lbs or 73 kg)", "160 lbs")
            activity_level = st.select_slider(
                "Activity Level",
                options=[
                    "Sedentary",
                    "Lightly Active",
                    "Moderately Active",
                    "Very Active",
                    "Extremely Active",
                ],
            )
            goals = st.multiselect(
                "Nutrition Goals",
                [
                    "Weight Loss",
                    "Weight Gain",
                    "Maintenance",
                    "Muscle Building",
                    "Better Energy",
                    "Improved Athletic Performance",
                    "Disease Management",
                    "General Health",
                ],
            )

    with tab2:
        st.header("Health Information")

        medical_conditions = st.text_area(
            "Medical Conditions (separate with commas)",
            placeholder="E.g., Diabetes Type 2, Hypertension, Hypothyroidism...",
        )

        medications = st.text_area(
            "Current Medications (separate with commas)",
            placeholder="E.g., Metformin, Lisinopril, Levothyroxine...",
        )

        allergies = st.text_area(
            "Food Allergies/Intolerances (separate with commas)",
            placeholder="E.g., Lactose, Gluten, Shellfish, Peanuts...",
        )

    with tab3:
        st.header("Preferences & Lifestyle")

        col1, col2 = st.columns(2)

        with col1:
            food_preferences = st.text_area(
                "Food Preferences & Dislikes",
                placeholder="E.g., Prefer plant-based, dislike seafood...",
            )

            cooking_ability = st.select_slider(
                "Cooking Skills & Available Time",
                options=[
                    "Very Limited",
                    "Basic/Quick Meals",
                    "Average",
                    "Advanced/Can Spend Time",
                    "Professional Level",
                ],
            )

        with col2:
            budget = st.select_slider(
                "Budget Considerations",
                options=[
                    "Very Limited",
                    "Budget Conscious",
                    "Moderate",
                    "Flexible",
                    "No Constraints",
                ],
            )

            cultural_factors = st.text_area(
                "Cultural or Religious Dietary Factors",
                placeholder="E.g., Halal, Kosher, Mediterranean tradition...",
            )

    # Collect all user information
    user_info = UserInfo(
        age=age,
        gender=gender,
        height=height,
        weight=weight,
        activity_level=activity_level,
        goals=", ".join(goals) if goals else "General health improvement",
        medical_conditions=medical_conditions or "None reported",
        medications=medications or "None reported",
        allergies=allergies or "None reported",
        food_preferences=food_preferences or "No specific preferences",
        cooking_ability=cooking_ability,
        budget=budget,
        cultural_factors=cultural_factors or "No specific factors",
    )

    # Check if API keys are present
    if not os.getenv("SERPER_API_KEY"):
        st.warning("⚠️ API keys not detected. Please add your SERPER_API_KEY to your .env file.")

    # Create a submission button
    if st.button("Generate Nutrition Plan"):
        if not goals:
            st.error("Please select at least one nutrition goal.")
            return

        # Display user information summary
        with st.expander("Summary of Your Information"):
            st.json(user_info)

        # Run the nutrition advisor
        result = run(user_info)

        if result:
            st.success("✅ Your personalized nutrition plan is ready!")
            st.markdown("## Your Personalized Nutrition Plan")
            st.markdown(result.raw)

            # Add download capability
            st.download_button(
                label="Download Nutrition Plan",
                data=result.raw,
                file_name="my_nutrition_plan.md",
                mime="text/markdown",
            )


if __name__ == "__main__":
    app()
