import random
from constants import *

class Board:
    def __init__(self, resources_data):
        self.grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.resources = {}
        self.factories = {}
        self.resources_data = resources_data
        self.generate_resources()

    def generate_resources(self):
        if not self.resources_data or not self.resources_data.get("resources"):
            print("Warning: No resources data available")
            return

        resources_list = self.resources_data["resources"]
        if not resources_list:
            print("Warning: Empty resources list")
            return

        num_resources = random.randint(MIN_RESOURCES, MAX_RESOURCES)
        for _ in range(num_resources):
            x = random.randint(0, GRID_SIZE-1)
            y = random.randint(0, GRID_SIZE-1)
            while self.grid[y][x] is not None:
                x = random.randint(0, GRID_SIZE-1)
                y = random.randint(0, GRID_SIZE-1)
            resource_type = random.choice(resources_list)
            self.grid[y][x] = resource_type
            self.resources[(x, y)] = resource_type

    def get_tile_cost(self, x, y):
        # Calculate cost based on proximity to resources
        base_cost = 100
        for rx, ry in self.resources:
            distance = ((x - rx) ** 2 + (y - ry) ** 2) ** 0.5
            if distance < 3:  # Higher cost for tiles close to resources
                base_cost += (3 - distance) * 50
        return base_cost

    def is_tile_available(self, x, y):
        return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and self.grid[y][x] is None