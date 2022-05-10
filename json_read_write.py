import json


def load_settings():
    """Loads the data from the "settings.json" file.

    :return: a dictionary containing the data from the file
    :rtype: dict
    """
    with open('settings.json', 'r') as infile:
        return json.load(infile)


def save_settings(settings):
    """Saves the given dictionary to the "settings.json" file.

    :param dict settings: the settings intended to be saved
    """
    with open('settings.json', 'w') as outfile:
        json.dump(settings, outfile, indent=4, sort_keys=True)
