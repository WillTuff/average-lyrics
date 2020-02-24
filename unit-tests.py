import unittest
import ConfigParser

class testProgram(unittest.TestCase):

    def setUp(self):
        config = ConfigParser.ConfigParser()
        config.read("settings.ini")
        settings = "info"

        self.artistIds = ["A1", "A2", "A3"]
        self.mBUrl = config.get(settings, 'mBUrl')

    def test_firstArtistId(self):
        self.assertEqual(self.artistIds[0], "A1")

    def test_settingsFile(self):
        self.assertEqual(self.mBUrl, 'https://musicbrainz.org/ws/2/')

if __name__ == '__main__':
    unittest.main()