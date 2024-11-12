import unittest
from tests.statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        players = [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
        
        print("player returned: ", players)
        return players

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        self.player = self.stats.search("Semenko")
        self.assertIsNotNone(self.player, "Player 'Semenko' was not found.")
        self.assertEqual(self.player.name, "Semenko")
        