# filepath: src/card.py
from enum import Enum
import json

class CardType(Enum):
    TECHNOLOGY = "technology"
    FACTORY = "factory"
    TRANSPORT = "transport"
    WORKER = "worker"
    RESOURCE = "resource"

class Card:
    def __init__(self, id, name, type, data):
        self.id = id
        self.name = name
        self.type = type
        self.data = data
        self.selected = False
        
    @property
    def cost(self):
        if self.type == CardType.FACTORY:
            return self.data.get("initial_cost", 0)
        elif self.type == CardType.TECHNOLOGY:
            return self.data.get("initial_cost", 0)
        elif self.type == CardType.TRANSPORT:
            return self.data.get("initial_cost", 0)
        return 0

    @property
    def maintenance_cost(self):
        return self.data.get("maintenance_cost_per_round", 0)

    @property
    def pollution_rate(self):
        if self.type == CardType.FACTORY:
            return self.data.get("pollution_per_round", 0)
        elif self.type == CardType.TRANSPORT:
            return self.data.get("pollution_per_round", 0)
        return 0

class TechnologyCard(Card):
    def __init__(self, id, name, cost, effects):
        super().__init__(id, name, CardType.TECHNOLOGY, cost, effects)
        self.research_time = effects.get('research_time', 1)  # Rounds needed to complete

class FactoryCard(Card):
    def __init__(self, id, name, cost, effects):
        super().__init__(id, name, CardType.FACTORY, cost, effects)
        self.production_rate = effects.get('production_rate', 1)
        self.pollution_rate = effects.get('pollution_rate', 1)

class TransportCard(Card):
    def __init__(self, id, name, cost, effects):
        super().__init__(id, name, CardType.TRANSPORT, cost, effects)
        self.range = effects.get('range', 1)
        self.capacity = effects.get('capacity', 1)

class Deck:
    def __init__(self, card_data):
        self.technology_cards = []
        self.factory_cards = []
        self.transport_cards = []
        self.load_cards(card_data)

    def load_cards(self, card_data):
        for tech in card_data['technologies']:
            self.technology_cards.append(TechnologyCard(
                tech['id'], 
                tech['name'],
                tech['cost'],
                tech['effects']
            ))
        
        for factory in card_data['factories']:
            self.factory_cards.append(FactoryCard(
                factory['id'],
                factory['name'],
                factory['cost'],
                factory['effects']
            ))
        
        for transport in card_data['transports']:
            self.transport_cards.append(TransportCard(
                transport['id'],
                transport['name'],
                transport['cost'],
                transport['effects']
            ))