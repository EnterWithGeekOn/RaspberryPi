#--------------------------------------------------------------
# ifttt.py
# Written by David Wise (david@dfwise.net)
#--------------------------------------------------------------
# Triggers the Maker Channel in IFTTT https://ifttt.com/maker
# The Event and Seceret key are set in IFTTTConfig.py
# from IfTTT.com
# Ingredients
# Example	Notes
# EventName	buzzer	The name of the event that was triggered.
# Value1	Hello world	Extra data sent with the event.
# Value2	Hello world	Extra data sent with the event.
# Value3	Hello world	Extra data sent with the event.
# OccurredAt	May 5, 2013 at 11:30PM	Date and time event occurred.
#
# Histroy
# First Draft 05 Jan 2016

import requests
import IFTTTConfig


BaseURL = 'https://maker.ifttt.com/trigger/'
BaseURL = BaseURL + IFTTTConfig.IFTTTEvent + '/with/key/' + IFTTTConfig.IFTTTKey

def iftttmaker(first, second, third):
    report = {}
    report["value1"] = first
    report["value2"] = second
    report["value3"] = third
    requests.post(BaseURL, data=report)

