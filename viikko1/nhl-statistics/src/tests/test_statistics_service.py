from statistics_service import StatisticsService
from player import Player
import unittest

class StubPlayerReader:
    def get_players(self):
        return [
            Player("Player1", "PHI", 5, 10),
            Player("Player2", "PHI", 3, 8),
            Player("Player3", "EDM", 10, 12),
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        reader = StubPlayerReader()
        self.stats = StatisticsService(reader)

    def test_team(self):
        phi_players = self.stats.team("PHI")
        self.assertEqual(len(phi_players), 2)
        self.assertEqual(phi_players[0].name, "Player1")
        self.assertEqual(phi_players[1].name, "Player2")