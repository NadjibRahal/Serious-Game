from constants import *
from player import Player
from board import Board


class Game:
    def __init__(self, resources_data):
        self.resources_data = resources_data
        self.players = [Player(i, f"Player {i+1}") for i in range(NUM_PLAYERS)]
        self.current_player = 0
        self.board = Board(resources_data)
        self.round = 1
        self.game_over = False

    def next_turn(self):
        self.current_player = (self.current_player + 1) % NUM_PLAYERS
        if self.current_player == 0:
            self.round += 1
            self.process_round_effects()

    def process_round_effects(self):
        # Process end of round effects for all players
        for player in self.players:
            # Calculate income from factories
            for factory in player.factories:
                player.budget += factory.base_production
                player.pollution += factory.pollution_per_round
            # Pay maintenance costs
            player.pay_maintenance()

    def check_game_over(self):
        # Check if all resources are depleted
        resources_remaining = any(resource["current_stock"] > 0 
                               for resource in self.resources_data["resources"]
                               if resource["current_stock"] is not None)
        if not resources_remaining:
            self.game_over = True
            return True
        return False

    def get_winner(self):
        return max(self.players, key=lambda p: p.calculate_score())