from constants import INITIAL_BUDGET
from card import CardType

class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.budget = INITIAL_BUDGET
        self.pollution = 0
        self.owned_tiles = []  # List of owned terrain coordinates
        self.factories = []    # List of owned factories
        self.technologies = [] # List of owned technologies
        self.workers = []      # List of hired workers
        self.transports = []   # List of owned transport methods
        self.resources = {}  # Resource type -> quantity

    def calculate_score(self):
        if self.pollution == 0:
            return self.budget  # Avoid division by zero
        return self.budget / self.pollution

    def buy_terrain(self, x, y, cost):
        if self.budget >= cost:
            self.budget -= cost
            self.owned_tiles.append((x, y))
            return True
        return False

    def add_pollution(self, amount):
        self.pollution += amount

    def pay_maintenance(self):
        total_maintenance = sum(factory.maintenance_cost_per_round for factory in self.factories)
        self.budget -= total_maintenance

    def can_afford(self, card):
        return self.budget >= card.cost

    def buy_card(self, card):
        if self.can_afford(card):
            self.budget -= card.cost
            if card.type == CardType.FACTORY:
                self.factories.append(card)
            elif card.type == CardType.TECHNOLOGY:
                self.technologies.append(card)
            elif card.type == CardType.TRANSPORT:
                self.transports.append(card)
            elif card.type == CardType.WORKER:
                self.workers.append(card)
            return True
        return False