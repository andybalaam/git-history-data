import unittest
import json
import os
from githistorydata.settings import Settings

""" Tests file for unittest/nose2 """

TEST_SETTINGS_FILE = "test_settings.json"


def get_test_settings():
    return Settings(TEST_SETTINGS_FILE)


def persist_test_settings(settings):
    with open(TEST_SETTINGS_FILE, "w") as f:
        json.dump(settings, f)


def update_test_settings(settings):
    """ Update the file 'manually' (not through the Settings API)
    and create a new Settings object """
    persist_test_settings(settings)
    return get_test_settings()


class TestSettings(unittest.TestCase):

    def setUp(self):
        settings = {}
        persist_test_settings(settings)

    def tearDown(self):
        os.remove(TEST_SETTINGS_FILE)
    
    def test_ctor(self):
        # test default ctor
        settings = Settings()
        self.assertEqual(settings["git_path"], "/usr/bin/git")

        # test ctor with settings_file_path argument
        settings = {"key1": "value1"}
        settings = update_test_settings(settings)
        self.assertEqual(settings["key1"], "value1")

    def test_load(self):
        settings1 = get_test_settings()
        # assert 'key1' is not in the settings
        with self.assertRaises(KeyError):
            s = settings1["key1"]
        # write the 'key1' setting to the test file
        # (not using the Settings API)
        settings2 = {"key1": "value1"}
        persist_test_settings(settings2)
        # perform 'load'
        settings1.load()
        # assert 'key1' is in settings
        self.assertEqual(settings1["key1"], "value1")

    def test_add(self):
        settings = get_test_settings()
        # assert 'key1' is not in the settings
        with self.assertRaises(KeyError):
            s = settings["key1"]
        # add 'key1'
        settings.add({"key1": "value1"})
        # assert 'key1' is in settings
        self.assertEqual(settings["key1"], "value1")
        # assert 'key1' not persisted
        settings = get_test_settings()
        with self.assertRaises(KeyError):
            s = settings["key1"]

    def test_save(self):
        settings = get_test_settings()
        # assert 'key1' is not in the settings
        with self.assertRaises(KeyError):
            s = settings["key1"]
        # add 'key1'
        settings.add({"key1": "value1"})
        # save settings
        settings.save()
        # assert 'key1' persisted
        settings = get_test_settings()
        self.assertEqual(settings["key1"], "value1")

    def test_persist(self):
        settings = get_test_settings()
        # assert 'key1' is not in the settings
        with self.assertRaises(KeyError):
            s = settings["key1"]
        # persist 'key1'
        settings.persist({"key1": "value1"})
        # assert 'key1' persisted
        settings = get_test_settings()
        self.assertEqual(settings["key1"], "value1")

    def test___getitmem__(self):
        # test the [] accessors
        settings = Settings()
        self.assertEqual(settings["git_path"], "/usr/bin/git")

    def test___setitem__(self):
        settings = get_test_settings()
        # assert 'key1' is not in the settings
        with self.assertRaises(KeyError):
            s = settings["key1"]
        # set 'key1'
        settings["key1"] = "value1"
        # assert 'key1' is in settings
        self.assertEqual(settings["key1"], "value1")
        # assert 'key1' not persisted
        settings = get_test_settings()
        with self.assertRaises(KeyError):
            s = settings["key1"]
        
