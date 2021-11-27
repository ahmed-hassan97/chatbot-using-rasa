# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from apiRequest import *


class ActionHelloWorld(Action):

    def capitalName(self) -> Text:
        return "action_capital_api"
    def populationName(self) -> Text:
        return "action_population_api"    

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city=tracker.latest_message['text']
        capital = getCapitalOfCountry(str(city))
        dispatcher.utter_template("utter_capital_country",tracker,cap=capital)

        return []