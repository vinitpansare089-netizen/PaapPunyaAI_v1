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


"""
data_service.py

Purpose:
Handles loading and management of mythology datasets.

Current Responsibilities:
- Load mythology stories from JSON files.
- Load stories from multiple deity files.

Future Responsibilities:
- Dataset validation
- Database integration

Author:
Vinit (Trinovous)

Created For:
PaapPunyaAI_v1
"""

import json


def load_stories(file_path):

    """
    Load stories from a single JSON file.
    """

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data['stories']


def load_all_stories(file_paths):

    """
    Load stories from multiple deity JSON files.
    """

    all_stories = []

    for file_path in file_paths:
        stories = load_stories(file_path)
        all_stories.extend(stories)

    return all_stories