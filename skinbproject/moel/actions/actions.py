# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionRecommendProduct(Action):
    def name(self) -> Text:
        return "action_recommend_product"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Load skin dataset
        skin_data = pd.read_csv(".../dataset/skin_dataset.csv")
        
        # Load products dataset
        products_data = pd.read_csv(".../dataset/nivea_products.csv")
        
        # Get user information from the tracker
        age = tracker.get_slot("age")
        skin_tone = tracker.get_slot("skin_tone")
        race = tracker.get_slot("race")
        gender = tracker.get_slot("gender")
        skin_condition = tracker.get_slot("skin_condition")
        
        # Filter skin dataset based on user information
        filtered_skin_data = skin_data[
            (skin_data["age_group"] == age) &
            (skin_data["fitzpatrick_skin_type"] == skin_tone) &
            (skin_data["race"] == race) &
            (skin_data["sex_at_birth"] == gender) &
            (skin_data["conditions"].str.contains(skin_condition))
        ]
        
        # Get the most common product for the filtered skin data
        recommended_product = filtered_skin_data["product"].mode()[0]
        
        # Get the product details from the products dataset
        product_details = products_data[products_data["Product Name"] == recommended_product]
        product_name = product_details["Product Name"].values[0]
        product_url = product_details["URL"].values[0]
        
        # Provide the product recommendation to the user
        dispatcher.utter_message(text=f"Based on your skin information, I recommend the following product:")
        dispatcher.utter_message(text=f"{product_name}")
        dispatcher.utter_message(text=f"You can find more details about the product here: {product_url}")
        
        return []
    
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionRecommendProduct(Action):
    def name(self) -> Text:
        return "action_recommend_product"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Load skin dataset
        skin_data = pd.read_csv(".../dataset/skin_dataset.csv")
        
        # Load products dataset
        products_data = pd.read_csv(".../dataset/nivea_products.csv")
        
        # Get user information from the tracker
        age = tracker.get_slot("age")
        skin_tone = tracker.get_slot("skin_tone")
        race = tracker.get_slot("race")
        gender = tracker.get_slot("gender")
        
        # Filter skin dataset based on user information
        filtered_skin_data = skin_data[
            (skin_data["age_group"] == age) &
            (skin_data["fitzpatrick_skin_type"] == skin_tone) &
            (skin_data["race"] == race) &
            (skin_data["sex_at_birth"] == gender)
        ]
        
        # Get the most common product for the filtered skin data
        recommended_product = filtered_skin_data["product"].mode()[0]
        
        # Get the product details from the products dataset
        product_details = products_data[products_data["Product Name"] == recommended_product]
        product_name = product_details["Product Name"].values[0]
        product_url = product_details["URL"].values[0]
        product_image_url = product_details["Image URL"].values[0]
        
        # Provide the product recommendation to the user
        dispatcher.utter_message(template="utter_product_recommendation",
                                 product_name=product_name,
                                 product_url=product_url,
                                 product_image_url=product_image_url)
        
        return []