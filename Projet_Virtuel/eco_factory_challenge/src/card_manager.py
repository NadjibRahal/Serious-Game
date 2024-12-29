import json
import os
from card import Card, CardType
from pathlib import Path

class CardManager:
    def __init__(self):
        self.technologies = []
        self.resources = []
        self.transports = []
        self.workers = []
        # Get absolute path to data directory
        self.data_path = Path(__file__).parent.parent / 'resources' / 'data'
        self.load_all_cards()

    def load_all_cards(self):
        try:
            data = self._load_json('technologies.json')
            self.technologies = data.get('technologies', [])
            
            data = self._load_json('ressources.json')
            self.resources = data.get('resources', [])
            
            data = self._load_json('transports.json')
            self.transports = data.get('transports', [])
            
            data = self._load_json('travailleurs.json')
            self.workers = data.get('workers', [])
        except Exception as e:
            print(f"Error loading cards: {e}")
            # Initialize with empty lists if loading fails
            self.technologies = []
            self.resources = []
            self.transports = []
            self.workers = []

    def _load_json(self, filename):
        file_path = self.data_path / filename
        if not file_path.exists():
            print(f"Error: {filename} not found in {self.data_path}")
            return {}
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def _convert_to_cards(self, data, filename):
        cards = []
        card_type = self._determine_card_type(filename)
        
        if filename == 'technologies.json':
            for item in data['technologies']:
                cards.append(Card(item['id'], item['name'], card_type, item))
        elif filename == 'usines.json':
            for item in data['factories']:
                cards.append(Card(item['id'], item['name'], card_type, item))
        elif filename == 'transports.json':
            for item in data['transports']:
                cards.append(Card(item['id'], item['name'], card_type, item))
        elif filename == 'travailleurs.json':
            for item in data['workers']:
                cards.append(Card(item['id'], item['name'], card_type, item))
        elif filename == 'ressources.json':
            for item in data['resources']:
                cards.append(Card(item['id'], item['name'], card_type, item))
        return cards

    def _determine_card_type(self, filename):
        type_map = {
            'technologies.json': CardType.TECHNOLOGY,
            'usines.json': CardType.FACTORY,
            'transports.json': CardType.TRANSPORT,
            'travailleurs.json': CardType.WORKER,
            'ressources.json': CardType.RESOURCE
        }
        return type_map.get(filename)

    def get_all_cards_of_type(self, card_type):
        if card_type == CardType.TECHNOLOGY:
            return self.technologies
        elif card_type == CardType.FACTORY:
            return self.factories
        elif card_type == CardType.TRANSPORT:
            return self.transports
        elif card_type == CardType.WORKER:
            return self.workers
        elif card_type == CardType.RESOURCE:
            return self.resources
        return []

    def get_card_by_id(self, card_type, card_id):
        cards = self.get_all_cards_of_type(card_type)
        return next((card for card in cards if card.id == card_id), None)