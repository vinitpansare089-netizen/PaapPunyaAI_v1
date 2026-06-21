import json

def load_stories(file_path):

    """
    from here stories will load from json file
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data['stories']
    

