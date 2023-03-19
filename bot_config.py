#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Bot Configuration"""

    ############## Azure Bot Service ###############
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "e11ded0f-61f3-4abd-8aa4-089178d2ccb9") # Multi
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "EEP8Q~JlS7olsAsN9Zi1OLEc.DLLENmpl2aGFc9k") #  #f3108e6e-16ff-4039-9c10-4347b595ba08
    ## Azure
    #APP_ID = os.environ.get("MicrosoftAppId", "e1028877-1f92-4f3f-b783-851b6585d5be") 
    #APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "87C8Q~zNB0fHRT1Szo4qrt43.1MV8ZlXZ2AKxc4q")
    # G
    #
    #

    ############## LUIS Service ###############
    ##LUIS_APP_ID = os.environ.get("LuisAppId", "c9636815-553b-46c8-84aa-900dea6f373a")
    #LUIS_API_KEY = os.environ.get("LuisAPIKey", "0fa672cf0afb4c13831dafac089ac1bb")
    #LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "https://flymeluis-authoring.cognitiveservices.azure.com/")
    ##### V2
    LUIS_APP_ID = os.environ.get("LuisAppId", "26eb04e6-67da-4c77-8c4f-46d9bb6635dc")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "a4983a29ae8348d1a71442db579c51bd")
    
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com" (<your region>.api.cognitive.microsoft.com)
    #LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "francecentral.api.cognitive.microsoft.com")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "https://luis-app-predicition.cognitiveservices.azure.com/")
    
    ############## App Insights Service ###############
    #APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("AppInsightsInstrumentationKey", "a19f3cda-7f37-4f23-b477-3957a640e706")
    ##### V2
    # Insights
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "84b943f3-3bf2-49bb-add9-d16b5cb43694"
    )
