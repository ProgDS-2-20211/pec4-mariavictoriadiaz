import unittest
import pandas as pd
from exploratory_analysis import count_tracks_artist, count_track_contain, count_tracks_years,track_popularity,artists_every_decade
from one_artist_one_feature import summary_audio_feature


class TestDataExpl(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Loading dataset")
        cls._df = pd.read_csv("../data/tracks.csv")

    def test_statistics(self):
        print("Starting test_statistics")
        self.assertEqual(count_tracks_artist(self._df, "Radiohead"), 159)
        self.assertEqual(count_track_contain(self._df, "police"), 11)
        self.assertEqual(count_tracks_years(self._df, 1990), 380)
        self.assertEqual(track_popularity(self._df, 10), "Beggin'")
        self.assertEqual(artists_every_decade(self._df, 1960,7), ['Ennio Morricone', 'David Bowie'])

    def features(self):
        print("Starting test_features_summary")
        mini, maxi, meani = summary_audio_feature(self._df, "energy", "Metallica")
        self.assertEqual(mini, 0.0533)
        self.assertEqual(maxi, 0.998)
        self.assertEqual(meani, 0.8463)

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestDataExpl))
unittest.TextTestRunner(verbosity=2).run(suite)
