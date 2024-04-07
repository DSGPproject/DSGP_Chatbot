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


class ActionGreet(Action):
    def name(self) -> Text:
        return "utter_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_greet")
        return []


class ActionThankYou(Action):
    def name(self) -> Text:
        return "utter_thank_you"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_thank_you")
        return []


class ActionCheerUp(Action):
    def name(self) -> Text:
        return "utter_cheer_up"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_cheer_up")
        return []


class ActionDidThatHelp(Action):
    def name(self) -> Text:
        return "utter_did_that_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_did_that_help")
        return []


class ActionHappy(Action):
    def name(self) -> Text:
        return "utter_happy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_happy")
        return []


class ActionGoodbye(Action):
    def name(self) -> Text:
        return "utter_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_goodbye")
        return []


class ActionWhatCanYouDo(Action):
    def name(self) -> Text:
        return "utter_what_can_you_do"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_what_can_you_do")
        return []


class ActionHowCanYouHelp(Action):
    def name(self) -> Text:
        return "utter_how_can_you_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_how_can_you_help")
        return []


class ActionOfferAdditionalInformation(Action):
    def name(self) -> Text:
        return "utter_offer_additional_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_offer_additional_information")
        return []


class ActionHelpConfusion(Action):
    def name(self) -> Text:
        return "utter_help_confusion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_help_confusion")
        return []


class ActionExplainAnthracnose(Action):
    def name(self) -> Text:
        return "utter_explain_anthracnose"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_explain_anthracnose")
        return []


class ActionAnthracnoseSymptoms(Action):
    def name(self) -> Text:
        return "utter_anthracnose_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_anthracnose_symptoms")
        return []


class ActionAnthracnoseManagement(Action):
    def name(self) -> Text:
        return "utter_anthracnose_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_anthracnose_management")
        return []


class ActionExplainAlgalLeaf(Action):
    def name(self) -> Text:
        return "utter_explain_algal_leaf"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_explain_algal_leaf")
        return []


class ActionAlgalLeafSymptoms(Action):
    def name(self) -> Text:
        return "utter_algal_leaf_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_algal_leaf_symptoms")
        return []


class ActionAlgalLeafManagement(Action):
    def name(self) -> Text:
        return "utter_algal_leaf_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_algal_leaf_management")
        return []


class ActionExplainBirdEyeSpot(Action):
    def name(self) -> Text:
        return "utter_explain_bird_eye_spot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_explain_bird_eye_spot")
        return []


class ActionBirdEyeSpotSymptoms(Action):
    def name(self) -> Text:
        return "utter_bird_eye_spot_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_bird_eye_spot_symptoms")
        return []


class ActionBirdEyeSpotManagement(Action):
    def name(self) -> Text:
        return "utter_bird_eye_spot_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_bird_eye_spot_management")
        return []


class ActionExplainBrownBlight(Action):
    def name(self) -> Text:
        return "utter_explain_brown_blight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_explain_brown_blight")
        return []


class ActionBrownBlightSymptoms(Action):
    def name(self) -> Text:
        return "utter_brown_blight_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_blight_symptoms")
        return []


class ActionBrownBlightManagement(Action):
    def name(self) -> Text:
        return "utter_brown_blight_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_blight_management")
        return []


class ActionExplainGrayLight(Action):
    def name(self) -> Text:
        return "utter_explain_gray_light"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_explain_gray_light")
        return []


class ActionTransmissionGrayLight(Action):
    def name(self) -> Text:
        return "utter_gray_light_transmission"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gray_light_transmission")
        return []


class ActionEnvironmentalFactorsGrayLight(Action):
    def name(self) -> Text:
        return "utter_gray_light_environmental_factors"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gray_light_environmental_factors")
        return []


class ActionTreatmentGrayLight(Action):
    def name(self) -> Text:
        return "utter_gray_light_treatment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gray_light_treatment")
        return []


class ActionGrayLightSymptoms(Action):
    def name(self) -> Text:
        return "utter_gray_light_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gray_light_symptoms")
        return []


class ActionGrayLightManagement(Action):
    def name(self) -> Text:
        return "utter_gray_light_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gray_light_management")
        return []


class ActionExplainWhiteSpot(Action):
    def name(self) -> Text:
        return "utter_explain_white_spot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_explain_white_spot")
        return []


class ActionWhiteSpotSymptoms(Action):
    def name(self) -> Text:
        return "utter_white_spot_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_white_spot_symptoms")
        return []


class ActionWhiteSpotManagement(Action):
    def name(self) -> Text:
        return "utter_white_spot_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_white_spot_management")
        return []


class ActionTreatmentWhiteSpot(Action):
    def name(self) -> Text:
        return "utter_white_spot_treatment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_white_spot_treatment")
        return []


class ActionRedLeafSpotExplanation(Action):
    def name(self) -> Text:
        return "utter_red_leaf_spot_explanation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_leaf_spot_explanation")
        return []


class ActionRedLeafSpotTreatment(Action):
    def name(self) -> Text:
        return "utter_red_leaf_spot_treatment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_leaf_spot_treatment")
        return []


class ActionRedLeafSpotSymptoms(Action):
    def name(self) -> Text:
        return "utter_red_leaf_spot_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_leaf_spot_symptoms")
        return []


class ActionRedLeafSpotManagement(Action):
    def name(self) -> Text:
        return "utter_red_leaf_spot_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_leaf_spot_management")
        return []


class ActionAnthracnoseCauses(Action):
    def name(self) -> Text:
        return "utter_anthracnose_causes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_anthracnose_causes")
        return []


class ActionAlgalLeafCauses(Action):
    def name(self) -> Text:
        return "utter_algal_leaf_causes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_algal_leaf_causes")
        return []


class ActionBirdEyeSpotCauses(Action):
    def name(self) -> Text:
        return "utter_bird_eye_spot_causes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_bird_eye_spot_causes")
        return []


class ActionBrownBlightCauses(Action):
    def name(self) -> Text:
        return "utter_brown_blight_causes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_blight_causes")
        return []


class ActionGrayLightCauses(Action):
    def name(self) -> Text:
        return "utter_gray_light_causes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gray_light_causes")
        return []


class ActionWhiteSpotCauses(Action):
    def name(self) -> Text:
        return "utter_white_spot_causes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_white_spot_causes")
        return []


class ActionRedLeafSpotCauses(Action):
    def name(self) -> Text:
        return "utter_red_leaf_spot_causes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_leaf_spot_causes")
        return []


class ActionAnthracnoseDistribution(Action):
    def name(self) -> Text:
        return "utter_anthracnose_distribution"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_anthracnose_distribution")
        return []


class ActionAlgalLeafDistribution(Action):
    def name(self) -> Text:
        return "utter_algal_leaf_distribution"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_algal_leaf_distribution")
        return []


class ActionBirdEyeSpotDistribution(Action):
    def name(self) -> Text:
        return "utter_bird_eye_spot_distribution"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_bird_eye_spot_distribution")
        return []


class ActionBrownBlightDistribution(Action):
    def name(self) -> Text:
        return "utter_brown_blight_distribution"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_blight_distribution")
        return []


class ActionGrayLightDistribution(Action):
    def name(self) -> Text:
        return "utter_gray_light_distribution"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gray_light_distribution")
        return []


class ActionWhiteSpotDistribution(Action):
    def name(self) -> Text:
        return "utter_white_spot_distribution"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_white_spot_distribution")
        return []


class ActionRedLeafSpotDistribution(Action):
    def name(self) -> Text:
        return "utter_red_leaf_spot_distribution"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_leaf_spot_distribution")
        return []


class ActionAnthracnosePrevention(Action):
    def name(self) -> Text:
        return "utter_anthracnose_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_anthracnose_prevention")
        return []


class ActionAlgalLeafPrevention(Action):
    def name(self) -> Text:
        return "utter_algal_leaf_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_algal_leaf_prevention")
        return []


class ActionBirdEyeSpotPrevention(Action):
    def name(self) -> Text:
        return "utter_bird_eye_spot_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_bird_eye_spot_prevention")
        return []


class ActionBrownBlightPrevention(Action):
    def name(self) -> Text:
        return "utter_brown_blight_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_blight_prevention")
        return []


class ActionGrayLightPrevention(Action):
    def name(self) -> Text:
        return "utter_gray_light_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gray_light_prevention")
        return []


class ActionWhiteSpotPrevention(Action):
    def name(self) -> Text:
        return "utter_white_spot_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_white_spot_prevention")
        return []


class ActionRedLeafSpotPrevention(Action):
    def name(self) -> Text:
        return "utter_red_leaf_spot_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_leaf_spot_prevention")
        return []


class ActionAnthracnoseSpreadPrevention(Action):
    def name(self) -> Text:
        return "utter_anthracnose_spread_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_anthracnose_spread_prevention")
        return []


class ActionAlgalLeafSpreadPrevention(Action):
    def name(self) -> Text:
        return "utter_algal_leaf_spread_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_algal_leaf_spread_prevention")
        return []


class ActionBirdEyeSpotSpreadPrevention(Action):
    def name(self) -> Text:
        return "utter_bird_eye_spot_spread_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_bird_eye_spot_spread_prevention")
        return []


class ActionBrownBlightSpreadPrevention(Action):
    def name(self) -> Text:
        return "utter_brown_blight_spread_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_blight_spread_prevention")
        return []


class ActionGrayLightSpreadPrevention(Action):
    def name(self) -> Text:
        return "utter_gray_light_spread_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gray_light_spread_prevention")
        return []


class ActionWhiteSpotSpreadPrevention(Action):
    def name(self) -> Text:
        return "utter_white_spot_spread_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_white_spot_spread_prevention")
        return []


class ActionRedLeafSpotSpreadPrevention(Action):
    def name(self) -> Text:
        return "utter_red_leaf_spot_spread_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_leaf_spot_spread_prevention")
        return []


class ActionAnthracnoseSymptomsAdditional(Action):
    def name(self) -> Text:
        return "utter_anthracnose_symptoms_additional"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_anthracnose_symptoms_additional")
        return []


class ActionAnthracnoseOccurrenceReasons(Action):
    def name(self) -> Text:
        return "utter_anthracnose_occurrence_reasons"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_anthracnose_occurrence_reasons")
        return []


class ActionAnthracnoseRemedies(Action):
    def name(self) -> Text:
        return "utter_anthracnose_remedies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_anthracnose_remedies")
        return []


class ActionAlgalLeafSymptomsAdditional(Action):
    def name(self) -> Text:
        return "utter_algal_leaf_symptoms_additional"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_algal_leaf_symptoms_additional")
        return []


class ActionAlgalLeafOccurrenceReasons(Action):
    def name(self) -> Text:
        return "utter_algal_leaf_occurrence_reasons"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_algal_leaf_occurrence_reasons")
        return []


class ActionAlgalLeafRemedies(Action):
    def name(self) -> Text:
        return "utter_algal_leaf_remedies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_algal_leaf_remedies")
        return []


class ActionBirdEyeSpotSymptomsAdditional(Action):
    def name(self) -> Text:
        return "utter_bird_eye_spot_symptoms_additional"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_bird_eye_spot_symptoms_additional")
        return []


class ActionBirdEyeSpotOccurrenceReasons(Action):
    def name(self) -> Text:
        return "utter_bird_eye_spot_occurrence_reasons"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_bird_eye_spot_occurrence_reasons")
        return []


class ActionBirdEyeSpotRemedies(Action):
    def name(self) -> Text:
        return "utter_bird_eye_spot_remedies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_bird_eye_spot_remedies")
        return []


class ActionBrownBlightSymptomsAdditional(Action):
    def name(self) -> Text:
        return "utter_brown_blight_symptoms_additional"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_blight_symptoms_additional")
        return []


class ActionBrownBlightOccurrenceReasons(Action):
    def name(self) -> Text:
        return "utter_brown_blight_occurrence_reasons"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_blight_occurrence_reasons")
        return []


class ActionBrownBlightRemedies(Action):
    def name(self) -> Text:
        return "utter_brown_blight_remedies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_blight_remedies")
        return []


class ActionGrayLightSymptomsAdditional(Action):
    def name(self) -> Text:
        return "utter_gray_light_symptoms_additional"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gray_light_symptoms_additional")
        return []


class ActionGrayLightOccurrenceReasons(Action):
    def name(self) -> Text:
        return "utter_gray_light_occurrence_reasons"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gray_light_occurrence_reasons")
        return []


class ActionGrayLightRemedies(Action):
    def name(self) -> Text:
        return "utter_gray_light_remedies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gray_light_remedies")
        return []


class ActionWhiteSpotSymptomsAdditional(Action):
    def name(self) -> Text:
        return "utter_white_spot_symptoms_additional"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_white_spot_symptoms_additional")
        return []


class ActionWhiteSpotOccurrenceReasons(Action):
    def name(self) -> Text:
        return "utter_white_spot_occurrence_reasons"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_white_spot_occurrence_reasons")
        return []


class ActionWhiteSpotRemedies(Action):
    def name(self) -> Text:
        return "utter_white_spot_remedies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_white_spot_remedies")
        return []


class ActionRedLeafSpotSymptomsAdditional(Action):
    def name(self) -> Text:
        return "utter_red_leaf_spot_symptoms_additional"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_leaf_spot_symptoms_additional")
        return []


class ActionRedLeafSpotOccurrenceReasons(Action):
    def name(self) -> Text:
        return "utter_red_leaf_spot_occurrence_reasons"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_leaf_spot_occurrence_reasons")
        return []


class ActionRedLeafSpotRemedies(Action):
    def name(self) -> Text:
        return "utter_red_leaf_spot_remedies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_leaf_spot_remedies")
        return []


class ActionExplainTeaMosquitoBug(Action):
    def name(self) -> Text:
        return "utter_explain_tea_mosquito_bug"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_explain_tea_mosquito_bug")
        return []


class ActionTeaMosquitoBugImpact(Action):
    def name(self) -> Text:
        return "utter_tea_mosquito_bug_impact"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_tea_mosquito_bug_impact")
        return []


class ActionTeaMosquitoBugManagement(Action):
    def name(self) -> Text:
        return "utter_tea_mosquito_bug_management"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_tea_mosquito_bug_management")
        return []


class ActionExplainRedSpiderMite(Action):
    def name(self) -> Text:
        return "utter_explain_red_spider_mite"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_explain_red_spider_mite")
        return []


class ActionRedSpiderMiteImpact(Action):
    def name(self) -> Text:
        return "utter_red_spider_mite_impact"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_spider_mite_impact")
        return []


class ActionRedSpiderMiteManagement(Action):
    def name(self) -> Text:
        return "utter_red_spider_mite_management"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_spider_mite_management")
        return []


class ActionExplainTeaGreenLeafhopper(Action):
    def name(self) -> Text:
        return "utter_explain_tea_green_leafhopper"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_explain_tea_green_leafhopper")
        return []


class ActionTeaGreenLeafhopperImpact(Action):
    def name(self) -> Text:
        return "utter_tea_green_leafhopper_impact"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_tea_green_leafhopper_impact")
        return []


class ActionTeaGreenLeafhopperManagement(Action):
    def name(self) -> Text:
        return "utter_tea_green_leafhopper_management"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_tea_green_leafhopper_management")
        return []


class ActionExplainBlisterBlight(Action):
    def name(self) -> Text:
        return "utter_explain_blister_blight"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_explain_blister_blight")
        return []


class ActionBlisterBlightSymptoms(Action):
    def name(self) -> Text:
        return "utter_blister_blight_symptoms"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_blister_blight_symptoms")
        return []


class ActionBlisterBlightTreatment(Action):
    def name(self) -> Text:
        return "utter_blister_blight_treatment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_blister_blight_treatment")
        return []


class ActionExplainTwigDieBack(Action):
    def name(self) -> Text:
        return "utter_explain_twig_die_back"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_explain_twig_die_back")
        return []


class ActionTwigDieBackSymptoms(Action):
    def name(self) -> Text:
        return "utter_twig_die_back_symptoms"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_twig_die_back_symptoms")
        return []


class ActionTwigDieBackTreatment(Action):
    def name(self) -> Text:
        return "utter_twig_die_back_treatment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_twig_die_back_treatment")
        return []


class ActionExplainBrownRootRot(Action):
    def name(self) -> Text:
        return "utter_explain_brown_root_rot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_explain_brown_root_rot")
        return []


class ActionBrownRootRotSymptoms(Action):
    def name(self) -> Text:
        return "utter_brown_root_rot_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_root_rot_symptoms")
        return []


class ActionBrownRootRotTreatment(Action):
    def name(self) -> Text:
        return "utter_brown_root_rot_treatment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_root_rot_treatment")
        return []


class ActionBrownRootRotOccurrenceReason(Action):
    def name(self) -> Text:
        return "utter_brown_root_rot_occurrence_reason"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_root_rot_occurrence_reason")
        return []


class ActionRedRootRotExplanation(Action):
    def name(self) -> Text:
        return "utter_red_root_rot_explanation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_root_rot_explanation")
        return []


class ActionRedRootRotSymptoms(Action):
    def name(self) -> Text:
        return "utter_red_root_rot_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_root_rot_symptoms")
        return []


class ActionRedRootRotTreatment(Action):
    def name(self) -> Text:
        return "utter_red_root_rot_treatment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_root_rot_treatment")
        return []


class ActionRedRootRotOccurrenceReason(Action):
    def name(self) -> Text:
        return "utter_red_root_rot_occurrence_reason"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_root_rot_occurrence_reason")
        return []


class ActionFrostDamageExplanation(Action):
    def name(self) -> Text:
        return "utter_frost_damage_explanation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_frost_damage_explanation")
        return []


class ActionFrostDamageSymptoms(Action):
    def name(self) -> Text:
        return "utter_frost_damage_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_frost_damage_symptoms")
        return []


class ActionFrostDamageTreatment(Action):
    def name(self) -> Text:
        return "utter_frost_damage_treatment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_frost_damage_treatment")
        return []


class ActionFrostDamageOccurrenceReason(Action):
    def name(self) -> Text:
        return "utter_frost_damage_occurrence_reason"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_frost_damage_occurrence_reason")
        return []


class ActionTeaWiltDiseaseExplanation(Action):
    def name(self) -> Text:
        return "utter_tea_wilt_disease_explanation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_tea_wilt_disease_explanation")
        return []


class ActionTeaWiltDiseaseSymptoms(Action):
    def name(self) -> Text:
        return "utter_tea_wilt_disease_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_tea_wilt_disease_symptoms")
        return []


class ActionTeaWiltDiseaseTreatment(Action):
    def name(self) -> Text:
        return "utter_tea_wilt_disease_treatment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_tea_wilt_disease_treatment")
        return []


class ActionTeaWiltDiseaseOccurrenceReason(Action):
    def name(self) -> Text:
        return "utter_tea_wilt_disease_occurrence_reason"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_tea_wilt_disease_occurrence_reason")
        return []


class ActionNluFallback(Action):
    def name(self) -> Text:
        return "utter_nlu_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_nlu_fallback")
        return []


class ActionBotChallenge(Action):
    def name(self) -> Text:
        return "utter_iamabot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_iamabot")
        return []
