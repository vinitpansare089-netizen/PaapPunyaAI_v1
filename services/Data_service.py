"""
data_service.py

Purpose:
Handles loading and management of mythology datasets.

Current Responsibilities:
- Load Krishna stories from JSON files.

Future Responsibilities:
- Dataset validation
- Multi-deity support
- Database integration

Author:
Vinit (Trinovous)

Created For:
PaapPunyaAI_v1
"""


import json

def load_stories(file_path):

    """
    from here stories will load from json file
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data['stories']


