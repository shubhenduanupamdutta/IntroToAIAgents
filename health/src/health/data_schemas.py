"""Schemas and Models for passing data."""

from pydantic import BaseModel


class UserInfo(BaseModel):
    """Represents user health and lifestyle information.

    Attributes
    ----------
    age : str
        The age of the user.
    gender : str
        The gender of the user.
    height : str
        The height of the user.
    weight : str
        The weight of the user.
    activity_level : str
        The user's activity level.
    goals : str
        The user's health or fitness goals.
    medical_conditions : str
        Any medical conditions the user has.
    medications : str
        Medications the user is taking.
    allergies : str
        Allergies the user has.
    food_preferences : str
        The user's food preferences.
    cooking_ability : str
        The user's cooking ability.
    budget : str
        The user's budget for food.
    cultural_factors : str
        Cultural factors relevant to the user.

    """

    age: int
    gender: str
    height: str
    weight: str
    activity_level: str
    goals: str
    medical_conditions: str
    medications: str
    allergies: str
    food_preferences: str
    cooking_ability: str
    budget: str
    cultural_factors: str
