import json


class Settings:
    """ Asettings object that is responsible of managing a single settings file """

    def __init__(self, settings_file_path="settings.json"):
        """ Initialize a Settings object """
        self._settings_file_path = settings_file_path
        self._settings_dict = {}
        self.load()

    def load(self):
        """ Load settings from file """
        with open(self._settings_file_path) as f:
            self._settings_dict = dict(self._settings_dict, **json.load(f))

    def add(self, settings):
        """ Add one or more extra settings to this object without persisting them.
            settings must be a mapping object"""
        self._settings_dict = dict(self._settings_dict, **settings)

    def save(self):
        """ Save this object to file as it is, possibly overriting un-synced changed in the file """
        with open(self._settings_file_path, "w") as f:
            json.dump(self._settings_dict, f)

    def persist(self, settings=None):
        """ Potentially add settings to this object, then persist all the settings in it """
        # if new settings received, add them to this object
        if settings:
            self.add(settings)

        # synchronize settings with file
        self.load()

        # persist all settings to file
        self.save()

    def __getitem__(self, key):
        """ Access Settings using square brackets """
        return self._settings_dict[key]

    def __setitem__(self, key, value):
        """ Set items using square brackets without persisting the change """
        self._settings_dict[key] = value
