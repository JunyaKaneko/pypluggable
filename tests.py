import unittest
import pluggable


class PluggableLoadTestCase(unittest.TestCase):
    def test_load_existing_plugin_class(self):
        loader = pluggable.Loader(['plugins', ])
        sample_plugin = loader.load('SamplePlugin')
        assert sample_plugin.say_hello() == 'hello'
        type(sample_plugin).__name__ == 'SamplePlugin'

    def test_load_non_existing_class(self):
        loader = pluggable.Loader(['plugins',])
        try:
            loader.load('NonExistingPlugin')
            raise Exception('Should raise PluginDoesNotExist')
        except pluggable.PluginDoesNotExist:
            pass

    def test_load_non_plugin_class(self):
        loader = pluggable.Loader(['plugins', ])
        try:
            loader.load('SampleNotPlugin')
            raise Exception('Should raise pluginDoesNotExist')
        except pluggable.PluginDoesNotExist:
            pass
