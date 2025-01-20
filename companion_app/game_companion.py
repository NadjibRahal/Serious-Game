import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import json

# ---------------------- Predefined Game Data (JSON) ----------------------

# Define the factories, technologies, transportation types, and terrain tiles as JSON strings
FACTORIES_JSON = """
[
    {
        "name": "Timber Logging Camp",
        "construction_cost": 150,
        "operational_cost": 20,
        "pollution": 3,
        "output": {"Wood": 2},
        "resource_requirements": {},
        "allowed_terrain": ["Forest"],
        "workers_required": {"Technician": 1},
        "transportation_needed": []
    },
    {
        "name": "Crop Farm",
        "construction_cost": 200,
        "operational_cost": 25,
        "pollution": 2,
        "output": {"Water": 3},
        "resource_requirements": {},
        "allowed_terrain": ["Plains", "Coastal"],
        "workers_required": {"Universal Worker": 1},
        "transportation_needed": []
    },
    {
        "name": "Mine & Smelter",
        "construction_cost": 300,
        "operational_cost": 40,
        "pollution": 8,
        "output": {"Minerals": 2},
        "resource_requirements": {},
        "allowed_terrain": ["Mountain"],
        "workers_required": {"Technician": 1},
        "transportation_needed": ["Minerals"]
    },
    {
        "name": "Bioplastics Plant",
        "construction_cost": 250,
        "operational_cost": 30,
        "pollution": 5,
        "output": {"Plastics": 2},
        "resource_requirements": {"Wood": 1, "Water": 1},
        "allowed_terrain": ["Urban", "Plains", "Forest"],
        "workers_required": {"Environmental Advisor": 1},
        "transportation_needed": ["Wood", "Water"]
    },
    {
        "name": "Solar Panel Assembly",
        "construction_cost": 300,
        "operational_cost": 25,
        "pollution": 3,
        "output": {"Solar Panel": 2},
        "resource_requirements": {},
        "allowed_terrain": ["Urban", "Plains"],
        "workers_required": {"Engineer": 1},
        "transportation_needed": []
    },
    {
        "name": "Wind Turbine Factory",
        "construction_cost": 350,
        "operational_cost": 30,
        "pollution": 4,
        "output": {"Wind Turbine": 1},
        "resource_requirements": {},
        "allowed_terrain": ["Urban", "Plains"],
        "workers_required": {"Engineer": 1, "Technician": 1},
        "transportation_needed": []
    },
    {
        "name": "Recycling Center",
        "construction_cost": 200,
        "operational_cost": 20,
        "pollution": 4,
        "output": {"Recycled Materials": 1},
        "resource_requirements": {"Plastics": 1},
        "allowed_terrain": ["Urban"],
        "workers_required": {"Technician": 1},
        "transportation_needed": ["Plastics"]
    },
    {
        "name": "Urban Manufacturing Plant",
        "construction_cost": 300,
        "operational_cost": 35,
        "pollution": 6,
        "output": {"Manufactured Goods": 2},
        "resource_requirements": {"Minerals": 2, "Recycled Materials": 2},
        "allowed_terrain": ["Urban"],
        "workers_required": {"Engineer": 1, "Technician": 1},
        "transportation_needed": ["Minerals", "Recycled Materials"]
    },
    {
        "name": "Sustainable Fishery",
        "construction_cost": 250,
        "operational_cost": 20,
        "pollution": 2,
        "output": {"Fish": 2},
        "resource_requirements": {"Water": 1},
        "allowed_terrain": ["Coastal"],
        "workers_required": {"Universal Worker": 1},
        "transportation_needed": ["Water"]
    },
    {
        "name": "Eco-Consulting Agency",
        "construction_cost": 150,
        "operational_cost": 15,
        "pollution": 1,
        "output": {"Consultancy Services": 20},
        "resource_requirements": {},
        "allowed_terrain": ["Urban"],
        "workers_required": {"Environmental Advisor": 1},
        "transportation_needed": []
    }
]
"""

TECHNOLOGIES_JSON = """
[
    {
        "name": "Solar-Wind Hybrid Array",
        "category": "Renewable Energy",
        "cost": 250,
        "maintenance": 20,
        "effect": "Reduces a single factory’s operational cost by 10 and pollution by 3.",
        "prerequisites": []
    },
    {
        "name": "Advanced Automation Module",
        "category": "Process Optimization",
        "cost": 200,
        "maintenance": 15,
        "effect": "+20% production in that factory.",
        "prerequisites": ["Engineer"]
    },
    {
        "name": "Carbon Capture System",
        "category": "Pollution Control",
        "cost": 250,
        "maintenance": 20,
        "effect": "-6 pollution from the assigned factory each round.",
        "prerequisites": ["Environmental Advisor"]
    },
    {
        "name": "Bioplastic Synthesis Upgrade",
        "category": "Green Chemistry",
        "cost": 200,
        "maintenance": 10,
        "effect": "+10 EC per Bioplastics unit sold.",
        "prerequisites": []
    },
    {
        "name": "Industrial Recycling Unit",
        "category": "Waste Management",
        "cost": 200,
        "maintenance": 15,
        "effect": "Converts factory waste into Recycled Materials.",
        "prerequisites": ["Technician"]
    },
    {
        "name": "Closed-Loop Water System",
        "category": "Pollution Control",
        "cost": 150,
        "maintenance": 10,
        "effect": "-2 pollution from water pollution, saves 5 EC/round.",
        "prerequisites": ["Environmental Advisor"]
    },
    {
        "name": "Vertical Integration Logistics",
        "category": "Logistics",
        "cost": 300,
        "maintenance": 20,
        "effect": "Run up to 2 factories on the same tile. +5 EC/round in transport savings.",
        "prerequisites": []
    },
    {
        "name": "Urban Rooftop Farming",
        "category": "Agriculture / Urban",
        "cost": 100,
        "maintenance": 5,
        "effect": "+2 units of fresh produce with minimal pollution (+1 PP).",
        "prerequisites": []
    },
    {
        "name": "Electric Transport Network",
        "category": "Transportation",
        "cost": 200,
        "maintenance": 10,
        "effect": "Reduce transportation pollution by 50% for Electric Transport routes.",
        "prerequisites": []
    },
    {
        "name": "Fossil Fuel Subsidy",
        "category": "Economic Policy",
        "cost": 150,
        "maintenance": 5,
        "effect": "Reduce Fossil Fuel transportation costs by 10 EC per distance unit.",
        "prerequisites": []
    }
]
"""

TRANSPORTATION_JSON = """
[
    {
        "type": "Electric",
        "cost_per_distance": 50,
        "pollution_per_distance": 1
    },
    {
        "type": "Fossil Fuel",
        "cost_per_distance": 30,
        "pollution_per_distance": 3
    }
]
"""

# ---------------------- Data Classes ----------------------

@dataclass
class Technology:
    name: str
    category: str
    cost: int
    maintenance: int
    effect: str
    prerequisites: List[str] = field(default_factory=list)

@dataclass
class Worker:
    role: str  # Engineer, Technician, Environmental Advisor, Universal Worker
    salary: int
    benefit: str

@dataclass
class Factory:
    name: str
    construction_cost: int
    operational_cost: int
    pollution: int
    output: Dict[str, int]  # e.g., {'Wood': 2}
    resource_requirements: Dict[str, int]  # e.g., {'Wood':1}
    allowed_terrain: List[str]
    workers_required: Dict[str, int]
    transportation_needed: List[str]
    transportation: Dict[str, Dict[str, int]] = field(default_factory=dict)
    workers_assigned: Dict[str, int] = field(default_factory=dict)
    upgrades: List[str] = field(default_factory=list)

@dataclass
class Player:
    name: str
    ec: int = 1500
    pp: int = 0
    factories: List[Factory] = field(default_factory=list)
    technologies: List[Technology] = field(default_factory=list)
    workers: List[Worker] = field(default_factory=list)
    carbon_credits: int = 0

@dataclass
class TerrainTile:
    terrain_type: str
    purchase_cost: int
    resources: List[str]
    carbon_offset: int
    owned_by: Optional[str] = None

# ---------------------- Game State ----------------------

class GameState:
    def __init__(self):
        self.players: List[Player] = []
        self.terrain_tiles: List[TerrainTile] = self.initialize_terrain()
        self.current_round: int = 1
        self.max_rounds: int = 6
        self.transportation_types: List[Dict] = self.load_transportation()
        self.factories_data: List[Dict] = self.load_factories()
        self.technologies_data: List[Dict] = self.load_technologies()

    def load_factories(self) -> List[Dict]:
        return json.loads(FACTORIES_JSON)

    def load_technologies(self) -> List[Dict]:
        return json.loads(TECHNOLOGIES_JSON)

    def load_transportation(self) -> List[Dict]:
        return json.loads(TRANSPORTATION_JSON)

    def initialize_terrain(self) -> List[TerrainTile]:
        # Example initialization; in a real game, this could be randomized or set up differently
        return [
            TerrainTile("Plains", 200, ["Wood", "Water"], 5),
            TerrainTile("Forest", 250, ["Wood"], 10),
            TerrainTile("Mountain", 300, ["Minerals", "Oil"], 3),
            TerrainTile("Coastal", 250, ["Water", "Oil"], 7),
            TerrainTile("Urban", 350, ["Plastics", "Water"], 2),
            TerrainTile("Plains", 200, ["Wood", "Water"], 5),
            TerrainTile("Forest", 250, ["Wood"], 10),
            TerrainTile("Mountain", 300, ["Minerals", "Oil"], 3),
            TerrainTile("Coastal", 250, ["Water", "Oil"], 7),
            TerrainTile("Urban", 350, ["Plastics", "Water"], 2),
            TerrainTile("Plains", 200, ["Wood", "Water"], 5),
            TerrainTile("Forest", 250, ["Wood"], 10),
            TerrainTile("Mountain", 300, ["Minerals", "Oil"], 3),
            TerrainTile("Coastal", 250, ["Water", "Oil"], 7),
            TerrainTile("Urban", 350, ["Plastics", "Water"], 2),
            TerrainTile("Plains", 200, ["Wood", "Water"], 5),
            TerrainTile("Forest", 250, ["Wood"], 10),
            TerrainTile("Mountain", 300, ["Minerals", "Oil"], 3),
            TerrainTile("Coastal", 250, ["Water", "Oil"], 7),
            TerrainTile("Urban", 350, ["Plastics", "Water"], 2),
        ]

    def add_player(self, player_name: str):
        if len(self.players) >= 4:
            raise Exception("Maximum of 4 players reached.")
        self.players.append(Player(name=player_name))

# ---------------------- Companion App GUI (Overhauled Visuals Only) ----------------------

class CompanionApp(tk.Tk):
    def __init__(self, game_state: GameState):
        super().__init__()
        self.title("Enhanced ECO-FACTORY CHALLENGE Companion App")
        # New window size for a refreshed look
        self.geometry("1400x800")
        
        # Configure overall background color
        self.configure(bg="#F0F4F7")

        # Create a custom style for the entire application
        style = ttk.Style(self)
        # Choose a built-in theme to start with (e.g., 'clam')
        style.theme_use("clam")

        # Frame style
        style.configure("TFrame", background="#F0F4F7")

        # Label style
        style.configure("TLabel", background="#F0F4F7", font=("Arial", 10, "bold"), foreground="#2B2B2B")

        # Button style
        style.configure("TButton",
                        font=("Arial", 10, "bold"),
                        foreground="#FFFFFF",
                        background="#6699CC",
                        padding=6)

        # Notebook tab style
        style.configure("TNotebook", background="#F0F4F7")
        style.configure("TNotebook.Tab", background="#BED7F3", foreground="#000000", padding=(10, 5))

        # Treeview style
        style.configure("Treeview", 
                        background="#FFFFFF",
                        foreground="#2B2B2B",
                        rowheight=25,
                        fieldbackground="#FFFFFF")
        style.map("Treeview",
                  background=[("selected", "#5B9BD5")],
                  foreground=[("selected", "#FFFFFF")])

        # Scrollbar style
        style.configure("Vertical.TScrollbar", background="#BED7F3")

        # Messagebox styling is not natively customizable beyond system defaults,
        # but we keep a consistent color scheme in app elements.

        self.game_state = game_state
        self.selected_player: Optional[Player] = None

        # Load predefined data
        self.factories_list = self.load_factories()
        self.technologies_list = self.load_technologies()
        self.transportation_types = self.game_state.transportation_types

        # Create all widgets
        self.create_widgets()

    def load_factories(self) -> List[Factory]:
        factories = []
        for f in self.game_state.factories_data:
            factory = Factory(
                name=f["name"],
                construction_cost=f["construction_cost"],
                operational_cost=f["operational_cost"],
                pollution=f["pollution"],
                output=f["output"],
                resource_requirements=f["resource_requirements"],
                allowed_terrain=f["allowed_terrain"],
                workers_required=f["workers_required"],
                transportation_needed=f["transportation_needed"]
            )
            factories.append(factory)
        return factories

    def load_technologies(self) -> List[Technology]:
        technologies = []
        for t in self.game_state.technologies_data:
            tech = Technology(
                name=t["name"],
                category=t["category"],
                cost=t["cost"],
                maintenance=t["maintenance"],
                effect=t["effect"],
                prerequisites=t["prerequisites"]
            )
            technologies.append(tech)
        return technologies

    def create_widgets(self):
        # Player Selection Frame
        player_frame = ttk.Frame(self)
        player_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        ttk.Label(player_frame, text="Select Player:").pack(side=tk.LEFT)

        self.player_var = tk.StringVar()
        self.player_dropdown = ttk.Combobox(player_frame, textvariable=self.player_var, state="readonly")
        self.player_dropdown['values'] = [player.name for player in self.game_state.players]
        self.player_dropdown.bind("<<ComboboxSelected>>", self.update_selected_player)
        self.player_dropdown.pack(side=tk.LEFT, padx=5)

        ttk.Button(player_frame, text="Add Player", command=self.add_player_dialog).pack(side=tk.LEFT, padx=5)

        # Notebook for Tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=1, fill='both', padx=10, pady=10)

        # Dashboard Tab
        self.dashboard_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.dashboard_tab, text='Dashboard')
        self.create_dashboard_tab()

        # Terrain Tab
        self.terrain_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.terrain_tab, text='Terrain')
        self.create_terrain_tab()

        # Factories Tab
        self.factories_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.factories_tab, text='Factories')
        self.create_factories_tab()

        # Technologies Tab
        self.technologies_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.technologies_tab, text='Technologies')
        self.create_technologies_tab()

        # Workers Tab
        self.workers_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.workers_tab, text='Workers')
        self.create_workers_tab()

        # Resources Tab
        self.resources_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.resources_tab, text='Resources')
        self.create_resources_tab()

        # Pollution & Costs Tab
        self.pollution_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.pollution_tab, text='Pollution & Costs')
        self.create_pollution_tab()

    def add_player_dialog(self):
        def add_player():
            name = entry.get().strip()
            if name == "":
                messagebox.showerror("Error", "Player name cannot be empty.")
                return
            if name in [player.name for player in self.game_state.players]:
                messagebox.showerror("Error", "Player name already exists.")
                return
            try:
                self.game_state.add_player(name)
                self.player_dropdown['values'] = [player.name for player in self.game_state.players]
                add_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        add_window = tk.Toplevel(self)
        add_window.title("Add Player")
        add_window.geometry("300x150")
        add_window.configure(bg="#F0F4F7")

        ttk.Label(add_window, text="Player Name:").pack(padx=10, pady=10)
        entry = ttk.Entry(add_window)
        entry.pack(padx=10, pady=5)

        ttk.Button(add_window, text="Add", command=add_player).pack(padx=10, pady=10)

    def update_selected_player(self, event):
        player_name = self.player_var.get()
        self.selected_player = next((p for p in self.game_state.players if p.name == player_name), None)
        self.refresh_tabs()

    def create_dashboard_tab(self):
        self.dashboard_info = ttk.Label(
            self.dashboard_tab,
            text="Select a player to view dashboard.",
            justify=tk.LEFT,
            font=("Arial", 14, "bold"),
            foreground="#333333"
        )
        self.dashboard_info.pack(anchor=tk.W, padx=20, pady=20)

    def create_terrain_tab(self):
        frame = ttk.Frame(self.terrain_tab)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Terrain List
        self.terrain_tree = ttk.Treeview(
            frame,
            columns=("ID", "Terrain Type", "Purchase Cost", "Resources", "Carbon Offset", "Owned By"),
            show='headings'
        )
        for col in ("ID", "Terrain Type", "Purchase Cost", "Resources", "Carbon Offset", "Owned By"):
            self.terrain_tree.heading(col, text=col)
            self.terrain_tree.column(col, width=150, anchor=tk.CENTER)
        self.terrain_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.terrain_tree.yview)
        self.terrain_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        # Terrain Management Buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Button(btn_frame, text="Purchase Terrain", command=self.purchase_terrain_dialog).pack(pady=5)
        ttk.Button(btn_frame, text="Refresh Terrain", command=self.refresh_terrain).pack(pady=5)

        self.refresh_terrain()

    def create_factories_tab(self):
        frame = ttk.Frame(self.factories_tab)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Factory List
        self.factory_tree = ttk.Treeview(
            frame,
            columns=("Name", "Construction Cost", "Operational Cost", "Pollution", "Output", "Resources", "Transportation", "Workers"),
            show='headings'
        )
        for col in ("Name", "Construction Cost", "Operational Cost", "Pollution", "Output", "Resources", "Transportation", "Workers"):
            self.factory_tree.heading(col, text=col)
            self.factory_tree.column(col, width=120, anchor=tk.CENTER)
        self.factory_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.factory_tree.yview)
        self.factory_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        # Factory Management Buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Button(btn_frame, text="Add Factory", command=self.add_factory_dialog).pack(pady=5)
        ttk.Button(btn_frame, text="Remove Factory", command=self.remove_factory).pack(pady=5)
        ttk.Button(btn_frame, text="Refresh Factories", command=self.refresh_factories).pack(pady=5)

    def create_technologies_tab(self):
        frame = ttk.Frame(self.technologies_tab)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Technology List
        self.tech_tree = ttk.Treeview(
            frame,
            columns=("Name", "Category", "Cost", "Maintenance", "Effect", "Prerequisites"),
            show='headings'
        )
        for col in ("Name", "Category", "Cost", "Maintenance", "Effect", "Prerequisites"):
            self.tech_tree.heading(col, text=col)
            self.tech_tree.column(col, width=150, anchor=tk.CENTER)
        self.tech_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tech_tree.yview)
        self.tech_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        # Technology Management Buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Button(btn_frame, text="Purchase Technology", command=self.purchase_technology_dialog).pack(pady=5)
        ttk.Button(btn_frame, text="Remove Technology", command=self.remove_technology).pack(pady=5)
        ttk.Button(btn_frame, text="Refresh Technologies", command=self.refresh_technologies).pack(pady=5)

    def create_workers_tab(self):
        frame = ttk.Frame(self.workers_tab)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Worker List
        self.worker_tree = ttk.Treeview(
            frame,
            columns=("Role", "Salary", "Benefit"),
            show='headings'
        )
        for col in ("Role", "Salary", "Benefit"):
            self.worker_tree.heading(col, text=col)
            self.worker_tree.column(col, width=200, anchor=tk.CENTER)
        self.worker_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.worker_tree.yview)
        self.worker_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        # Worker Management Buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Button(btn_frame, text="Hire Worker", command=self.hire_worker_dialog).pack(pady=5)
        ttk.Button(btn_frame, text="Assign Worker", command=self.assign_worker_dialog).pack(pady=5)
        ttk.Button(btn_frame, text="Remove Worker", command=self.remove_worker).pack(pady=5)
        ttk.Button(btn_frame, text="Refresh Workers", command=self.refresh_workers).pack(pady=5)

    def create_resources_tab(self):
        frame = ttk.Frame(self.resources_tab)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Resource List
        self.resource_tree = ttk.Treeview(
            frame,
            columns=("Resource", "Produced", "Consumed", "Traded"),
            show='headings'
        )
        for col in ("Resource", "Produced", "Consumed", "Traded"):
            self.resource_tree.heading(col, text=col)
            self.resource_tree.column(col, width=150, anchor=tk.CENTER)
        self.resource_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.resource_tree.yview)
        self.resource_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        # Resource Management Buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Button(btn_frame, text="Trade Resources", command=self.trade_resources_dialog).pack(pady=5)
        ttk.Button(btn_frame, text="Refresh Resources", command=self.refresh_resources).pack(pady=5)

    def create_pollution_tab(self):
        frame = ttk.Frame(self.pollution_tab)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Pollution and Costs Display
        self.pollution_info = ttk.Label(
            frame,
            text="Select a player to view pollution and costs.",
            justify=tk.LEFT,
            font=("Arial", 14, "bold"),
            foreground="#333333"
        )
        self.pollution_info.pack(anchor=tk.W, padx=20, pady=20)

        ttk.Button(frame, text="Calculate Round", command=self.calculate_round).pack(pady=10)

    def refresh_tabs(self):
        self.refresh_dashboard()
        self.refresh_terrain()
        self.refresh_factories()
        self.refresh_technologies()
        self.refresh_workers()
        self.refresh_resources()
        self.refresh_pollution()

    def refresh_dashboard(self):
        if not self.selected_player:
            self.dashboard_info.config(text="Select a player to view dashboard.")
            return
        info = (
            f"Player: {self.selected_player.name}\n"
            f"Eco-Credits (EC): {self.selected_player.ec}\n"
            f"Pollution Points (PP): {self.selected_player.pp}\n"
            f"Carbon Credits: {self.selected_player.carbon_credits}"
        )
        self.dashboard_info.config(text=info)

    def refresh_terrain(self):
        for item in self.terrain_tree.get_children():
            self.terrain_tree.delete(item)
        for idx, tile in enumerate(self.game_state.terrain_tiles):
            owned_by = tile.owned_by if tile.owned_by else "None"
            resources_str = ", ".join(tile.resources)
            self.terrain_tree.insert("", tk.END, values=(
                idx + 1,
                tile.terrain_type,
                tile.purchase_cost,
                resources_str,
                tile.carbon_offset,
                owned_by
            ))

    def refresh_factories(self):
        for item in self.factory_tree.get_children():
            self.factory_tree.delete(item)
        if not self.selected_player:
            return
        for factory in self.selected_player.factories:
            output_str = ", ".join([f"{k}: {v}" for k, v in factory.output.items()])
            resources_str = ", ".join([f"{k}: {v}" for k, v in factory.resource_requirements.items()]) if factory.resource_requirements else "None"
            transportation = ", ".join([f"{res}: {trans['type']} ({trans['distance']})"
                                        for res, trans in factory.transportation.items()]) if factory.transportation else "N/A"
            workers = ", ".join([f"{role}: {count}" for role, count in factory.workers_assigned.items()]) if factory.workers_assigned else "None"
            self.factory_tree.insert("", tk.END, values=(
                factory.name,
                factory.construction_cost,
                factory.operational_cost,
                factory.pollution,
                output_str,
                resources_str,
                transportation,
                workers
            ))

    def refresh_technologies(self):
        for item in self.tech_tree.get_children():
            self.tech_tree.delete(item)
        if not self.selected_player:
            return
        for tech in self.selected_player.technologies:
            prereq = ", ".join(tech.prerequisites) if tech.prerequisites else "None"
            self.tech_tree.insert("", tk.END, values=(
                tech.name,
                tech.category,
                tech.cost,
                tech.maintenance,
                tech.effect,
                prereq
            ))

    def refresh_workers(self):
        for item in self.worker_tree.get_children():
            self.worker_tree.delete(item)
        if not self.selected_player:
            return
        for worker in self.selected_player.workers:
            self.worker_tree.insert("", tk.END, values=(
                worker.role,
                worker.salary,
                worker.benefit
            ))

    def refresh_resources(self):
        for item in self.resource_tree.get_children():
            self.resource_tree.delete(item)
        if not self.selected_player:
            return
        # Initialize all resources
        resource_summary = {
            'Minerals': {'Produced': 0, 'Consumed': 0, 'Traded': 0},
            'Wood': {'Produced': 0, 'Consumed': 0, 'Traded': 0},
            'Oil': {'Produced': 0, 'Consumed': 0, 'Traded': 0},
            'Water': {'Produced': 0, 'Consumed': 0, 'Traded': 0},
            'Plastics': {'Produced': 0, 'Consumed': 0, 'Traded': 0},
            'Bioplastics': {'Produced': 0, 'Consumed': 0, 'Traded': 0},
            'Solar Panel': {'Produced': 0, 'Consumed': 0, 'Traded': 0},
            'Wind Turbine': {'Produced': 0, 'Consumed': 0, 'Traded': 0},
            'Recycled Materials': {'Produced': 0, 'Consumed': 0, 'Traded': 0},
            'Manufactured Goods': {'Produced': 0, 'Consumed': 0, 'Traded': 0},
            'Fish': {'Produced': 0, 'Consumed': 0, 'Traded': 0},
            'Consultancy Services': {'Produced': 0, 'Consumed': 0, 'Traded': 0}
        }
        for factory in self.selected_player.factories:
            for res, qty in factory.output.items():
                if res in resource_summary:
                    resource_summary[res]['Produced'] += qty
            for res, qty in factory.resource_requirements.items():
                if res in resource_summary:
                    resource_summary[res]['Consumed'] += qty
        for res, data in resource_summary.items():
            self.resource_tree.insert("", tk.END, values=(
                res,
                data['Produced'],
                data['Consumed'],
                data['Traded']
            ))

    def refresh_pollution(self):
        if not self.selected_player:
            self.pollution_info.config(text="Select a player to view pollution and costs.")
            return
        total_pollution = self.calculate_total_pollution_for_player(self.selected_player)
        carbon_tax = 5 * total_pollution
        total_salary = sum(worker.salary for worker in self.selected_player.workers)
        total_maintenance = sum(tech.maintenance for tech in self.selected_player.technologies)
        info = (
            f"Total Pollution Points (PP): {total_pollution}\n"
            f"Carbon Tax (5 EC × PP): {carbon_tax} EC\n"
            f"Total Worker Salaries: {total_salary} EC\n"
            f"Total Technology Maintenance: {total_maintenance} EC"
        )
        self.pollution_info.config(text=info)

    def calculate_total_pollution_for_player(self, player: Player) -> int:
        total_pollution = 0
        for factory in player.factories:
            total_pollution += factory.pollution
            # Add pollution from transportation
            for trans in factory.transportation.values():
                trans_type = trans['type']
                distance = trans['distance']
                transport_info = next((t for t in self.transportation_types if t['type'] == trans_type), None)
                if transport_info:
                    pollution = transport_info['pollution_per_distance'] * distance
                    # Check for technology effects that reduce pollution
                    for tech in player.technologies:
                        if "Reduce transportation pollution by 50%" in tech.effect and trans_type == "Electric":
                            pollution = pollution // 2
                    total_pollution += pollution
        # Apply pollution reductions from technologies
        for tech in player.technologies:
            if "pollution" in tech.effect.lower():
                import re
                reductions = map(int, re.findall(r'-\d+', tech.effect))
                for reduction in reductions:
                    total_pollution += reduction  # reduction is negative
        # Apply pollution reductions from workers
        for worker in player.workers:
            if worker.role == "Environmental Advisor":
                # Assuming each advisor reduces pollution by 3
                total_pollution -= 3
        if total_pollution < 0:
            total_pollution = 0
        return total_pollution

    def calculate_round(self):
        # ---------------------- FIX START ----------------------
        if not self.game_state.players:
            messagebox.showerror("Error", "No players in the game.")
            return

        round_summary = ""
        game_end = False
        winner = None

        for player in self.game_state.players:
            # Calculate total pollution and apply carbon tax
            total_pollution = self.calculate_total_pollution_for_player(player)
            carbon_tax = 5 * total_pollution

            # Calculate total salaries and maintenance
            total_salary = sum(worker.salary for worker in player.workers)
            total_maintenance = sum(tech.maintenance for tech in player.technologies)

            # Calculate transportation costs
            transportation_cost = 0
            for factory in player.factories:
                for trans in factory.transportation.values():
                    trans_type = trans['type']
                    distance = trans['distance']
                    transport_info = next((t for t in self.transportation_types if t['type'] == trans_type), None)
                    if transport_info:
                        cost = transport_info['cost_per_distance'] * distance
                        # Check for technology effects that reduce transportation costs
                        for tech in player.technologies:
                            if "Reduce Fossil Fuel transportation costs by 10 EC per distance unit." in tech.effect and trans_type == "Fossil Fuel":
                                cost = max(cost - 10 * distance, 0)
                        transportation_cost += cost

            # Total expenses
            total_expenses = carbon_tax + total_salary + total_maintenance + transportation_cost

            # Deduct expenses from EC
            if player.ec < total_expenses:
                round_summary += f"{player.name} has insufficient Eco-Credits to cover the expenses this round.\n"
                continue  # Skip to next player
            player.ec -= total_expenses
            player.pp = total_pollution  # Update Pollution Points

            # Add production revenue
            production_revenue = 0
            for factory in player.factories:
                for res, qty in factory.output.items():
                    if res == "Consultancy Services":
                        production_revenue += qty  # Assuming 'Consultancy Services' are already valued
                    else:
                        production_revenue += qty * 50  # Base price
            player.ec += production_revenue

            round_summary += (
                f"{player.name}:\n"
                f"  Expenses: {total_expenses} EC\n"
                f"  Revenue: {production_revenue} EC\n"
                f"  Net Change: {production_revenue - total_expenses} EC\n"
                f"  Current EC: {player.ec} EC\n"
                f"  Current PP: {player.pp} PP\n\n"
            )

            # Check for new end condition (e.g., 3000 EC)
            if player.ec >= 3000:
                winner = player
                game_end = True
                break  # Exit the loop as the game should end immediately

        self.refresh_tabs()

        if game_end:
            round_summary += f"{winner.name} has reached 3000 EC! The game will now end.\n"
            self.end_game()
        else:
            round_summary += f"Round {self.game_state.current_round} completed.\n"
            self.game_state.current_round += 1
            if self.game_state.current_round > self.game_state.max_rounds:
                self.end_game()

        # Display the summary
        messagebox.showinfo("Round Calculated", round_summary)
        # ---------------------- FIX END ----------------------

    def calculate_total_pollution_for_player_fixed(self, player: Player) -> int:
        # This method ensures that pollution calculations are accurate per player
        total_pollution = 0
        for factory in player.factories:
            total_pollution += factory.pollution
            # Add pollution from transportation
            for trans in factory.transportation.values():
                trans_type = trans['type']
                distance = trans['distance']
                transport_info = next((t for t in self.transportation_types if t['type'] == trans_type), None)
                if transport_info:
                    pollution = transport_info['pollution_per_distance'] * distance
                    # Check for technology effects that reduce pollution
                    for tech in player.technologies:
                        if "Reduce transportation pollution by 50%" in tech.effect and trans_type == "Electric":
                            pollution = pollution // 2
                    total_pollution += pollution
        # Apply pollution reductions from technologies
        for tech in player.technologies:
            if "pollution" in tech.effect.lower():
                import re
                reductions = map(int, re.findall(r'-\d+', tech.effect))
                for reduction in reductions:
                    total_pollution += reduction  # reduction is negative
        # Apply pollution reductions from workers
        for worker in player.workers:
            if worker.role == "Environmental Advisor":
                # Assuming each advisor reduces pollution by 3
                total_pollution -= 3
        if total_pollution < 0:
            total_pollution = 0
        return total_pollution

    # ---------------------- Assign Worker Method Fix ----------------------

    def assign_worker_dialog(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return
        if not self.selected_player.workers:
            messagebox.showerror("Error", "No workers available to assign.")
            return
        if not self.selected_player.factories:
            messagebox.showerror("Error", "No factories available to assign workers.")
            return

        assign_window = tk.Toplevel(self)
        assign_window.title("Assign Worker")
        assign_window.geometry("500x300")
        assign_window.configure(bg="#F0F4F7")

        ttk.Label(assign_window, text="Select Worker:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        worker_var = tk.StringVar()
        workers = [f"{w.role} #{i + 1}" for i, w in enumerate(self.selected_player.workers)]
        worker_dropdown = ttk.Combobox(assign_window, textvariable=worker_var, state="readonly")
        worker_dropdown['values'] = workers
        worker_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(assign_window, text="Select Factory:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        factory_var = tk.StringVar()
        factories = [factory.name for factory in self.selected_player.factories]
        factory_dropdown = ttk.Combobox(assign_window, textvariable=factory_var, state="readonly")
        factory_dropdown['values'] = factories
        factory_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Button(
            assign_window,
            text="Assign",
            command=lambda: self.assign_worker(worker_var.get(), factory_var.get(), assign_window)
        ).grid(row=2, column=0, columnspan=2, pady=20)

    def assign_worker_fixed(self, worker_selection: str, factory_name: str, window):
        if not worker_selection or not factory_name:
            messagebox.showerror("Error", "Please select both worker and factory.")
            return
        # Extract worker index
        try:
            worker_index = int(worker_selection.split('#')[1]) - 1
            worker = self.selected_player.workers[worker_index]
        except (IndexError, ValueError):
            messagebox.showerror("Error", "Invalid worker selection.")
            return
        factory = next((f for f in self.selected_player.factories if f.name == factory_name), None)
        if not factory:
            messagebox.showerror("Error", "Invalid factory selected.")
            return
        # Normalize worker.role to ensure no leading/trailing spaces and correct casing
        worker_role = worker.role.strip()
        # Check if factory requires this worker role
        if worker_role not in factory.workers_required:
            messagebox.showerror("Error", f"{worker_role} is not required for {factory.name}.")
            return
        required = factory.workers_required.get(worker_role, 0)
        assigned = factory.workers_assigned.get(worker_role, 0)
        if assigned >= required:
            messagebox.showerror("Error", f"No need for more {worker_role}s in {factory.name}.")
            return
        # Assign worker
        factory.workers_assigned[worker_role] = assigned + 1
        self.refresh_factories()
        window.destroy()
        messagebox.showinfo("Success", f"{worker_role} assigned to {factory.name}.")

    # Replace the original assign_worker method with the fixed one
    assign_worker = assign_worker_fixed

    # ---------------------- End Game ----------------------

    def end_game(self):
        # Calculate final scores
        scores = []
        for player in self.game_state.players:
            score = player.ec / (1 + player.pp)
            scores.append((player.name, score))
        scores.sort(key=lambda x: x[1], reverse=True)
        winner = scores[0]
        game_over_message = "Game has ended.\n\nFinal Scores:\n"
        for name, score in scores:
            game_over_message += f"{name}: {score:.2f}\n"
        game_over_message += f"\nWinner: {winner[0]} with a score of {winner[1]:.2f}!"
        messagebox.showinfo("Game Over", game_over_message)
        self.destroy()

    # ---------------------- Terrain Management ----------------------

    def purchase_terrain_dialog(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return

        selected_items = self.terrain_tree.selection()
        if not selected_items:
            messagebox.showerror("Error", "No terrain tile selected.")
            return

        selected = self.terrain_tree.item(selected_items[0])
        terrain_id = int(selected['values'][0]) - 1
        terrain = self.game_state.terrain_tiles[terrain_id]

        if terrain.owned_by:
            messagebox.showerror("Error", "Terrain tile already owned.")
            return

        if self.selected_player.ec < terrain.purchase_cost:
            messagebox.showerror("Error", "Insufficient Eco-Credits to purchase this terrain.")
            return

        def confirm_purchase():
            try:
                self.selected_player.ec -= terrain.purchase_cost
                terrain.owned_by = self.selected_player.name
                self.refresh_terrain()
                self.refresh_tabs()
                messagebox.showinfo("Success", f"Terrain tile {terrain_id + 1} purchased successfully.")
                purchase_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        purchase_window = tk.Toplevel(self)
        purchase_window.title("Confirm Purchase")
        purchase_window.geometry("400x200")
        purchase_window.configure(bg="#F0F4F7")

        info = (
            f"Terrain ID: {terrain_id + 1}\n"
            f"Terrain Type: {terrain.terrain_type}\n"
            f"Purchase Cost: {terrain.purchase_cost} EC\n"
            f"Resources: {', '.join(terrain.resources)}\n"
            f"Carbon Offset: {terrain.carbon_offset}\n"
            f"Owned By: None"
        )
        ttk.Label(purchase_window, text="Confirm Purchase:", font=("Arial", 12, "bold")).pack(padx=10, pady=10)
        ttk.Label(purchase_window, text=info, justify=tk.LEFT).pack(padx=10, pady=5)

        ttk.Button(purchase_window, text="Confirm", command=confirm_purchase).pack(pady=10)
        ttk.Button(purchase_window, text="Cancel", command=purchase_window.destroy).pack()

    # ---------------------- Factory Management ----------------------

    def add_factory_dialog(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return

        add_window = tk.Toplevel(self)
        add_window.title("Add Factory")
        add_window.geometry("600x600")
        add_window.configure(bg="#F0F4F7")

        ttk.Label(add_window, text="Select Factory Type:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        factory_type_var = tk.StringVar()
        factory_types = [factory.name for factory in self.factories_list]
        factory_dropdown = ttk.Combobox(add_window, textvariable=factory_type_var, state="readonly")
        factory_dropdown['values'] = factory_types
        factory_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(add_window, text="Select Terrain Tile:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        terrain_var = tk.StringVar()
        owned_tiles = [
            f"{i + 1}. {tile.terrain_type}"
            for i, tile in enumerate(self.game_state.terrain_tiles)
            if tile.owned_by == self.selected_player.name
        ]
        if not owned_tiles:
            owned_tiles = ["No owned terrain tiles available."]
        terrain_dropdown = ttk.Combobox(add_window, textvariable=terrain_var, state="readonly")
        terrain_dropdown['values'] = owned_tiles
        terrain_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(add_window, text="Select Transportation Type for Each Resource Needed:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        transportation_frames = []

        def update_transportation_fields(event):
            factory_type = factory_type_var.get()
            for frame in transportation_frames:
                frame.destroy()
            transportation_frames.clear()
            factory = next((f for f in self.factories_list if f.name == factory_type), None)
            if factory and factory.transportation_needed:
                for idx, res in enumerate(factory.transportation_needed):
                    ttk.Label(add_window, text=f"{res}:").grid(row=3 + idx * 2, column=0, padx=20, pady=5, sticky=tk.W)
                    trans_var = tk.StringVar()
                    trans_dropdown = ttk.Combobox(add_window, textvariable=trans_var, state="readonly")
                    trans_dropdown['values'] = [t['type'] for t in self.transportation_types]
                    trans_dropdown.current(0)
                    trans_dropdown.grid(row=3 + idx * 2, column=1, padx=10, pady=5, sticky=tk.W)
                    transportation_frames.append(trans_dropdown)

        factory_dropdown.bind("<<ComboboxSelected>>", update_transportation_fields)

        ttk.Button(
            add_window,
            text="Add Factory",
            command=lambda: self.add_factory(factory_type_var.get(), terrain_var.get(), transportation_frames, add_window)
        ).grid(row=100, column=0, columnspan=2, pady=20)

    def add_factory(self, factory_name: str, terrain_selection: str, transportation_frames: List[ttk.Combobox], window):
        if not factory_name or not terrain_selection or terrain_selection == "No owned terrain tiles available.":
            messagebox.showerror("Error", "Please select both factory type and a valid terrain.")
            return
        factory = next((f for f in self.factories_list if f.name == factory_name), None)
        if not factory:
            messagebox.showerror("Error", "Invalid factory type selected.")
            return
        # Check if terrain allows the factory
        terrain_id = int(terrain_selection.split('.')[0]) - 1
        terrain = self.game_state.terrain_tiles[terrain_id]
        if terrain.terrain_type not in factory.allowed_terrain:
            messagebox.showerror("Error", f"{factory.name} cannot be placed on {terrain.terrain_type} terrain.")
            return
        # Check if player can afford
        if self.selected_player.ec < factory.construction_cost:
            messagebox.showerror("Error", "Insufficient Eco-Credits to construct this factory.")
            return
        # Deduct cost
        self.selected_player.ec -= factory.construction_cost
        # Create a copy of factory data
        new_factory = Factory(
            name=factory.name,
            construction_cost=factory.construction_cost,
            operational_cost=factory.operational_cost,
            pollution=factory.pollution,
            output=factory.output.copy(),
            resource_requirements=factory.resource_requirements.copy(),
            allowed_terrain=factory.allowed_terrain.copy(),
            workers_required=factory.workers_required.copy(),
            transportation_needed=factory.transportation_needed.copy()
        )
        # Assign transportation details
        if factory.transportation_needed:
            for idx, res in enumerate(factory.transportation_needed):
                trans_type = transportation_frames[idx].get()
                # Find nearest terrain tile with the resource
                distance, source_tile_index = self.find_nearest_resource(terrain_id, res)
                if source_tile_index is None:
                    # Prompt user to purchase a terrain tile that provides the missing resource
                    proceed = messagebox.askyesno(
                        "Resource Missing",
                        f"You do not own any terrain tile with the required resource: {res}.\n"
                        f"Do you want to purchase a terrain tile that provides {res}?"
                    )
                    if proceed:
                        # Open terrain purchase dialog filtered by resource
                        available_terrain = [
                            f"{i + 1}. {tile.terrain_type}"
                            for i, tile in enumerate(self.game_state.terrain_tiles)
                            if tile.owned_by is None and res in tile.resources
                        ]
                        if not available_terrain:
                            messagebox.showerror(
                                "Error",
                                f"No available terrain tiles provide the required resource: {res}."
                            )
                            # Refund factory construction cost
                            self.selected_player.ec += new_factory.construction_cost
                            return
                        purchase_window = tk.Toplevel(self)
                        purchase_window.title(f"Purchase Terrain for {res}")
                        purchase_window.geometry("500x300")
                        purchase_window.configure(bg="#F0F4F7")

                        ttk.Label(purchase_window, text=f"Select Terrain Tile that provides {res}:").pack(padx=10, pady=10)
                        terrain_var = tk.StringVar()
                        terrain_dropdown = ttk.Combobox(purchase_window, textvariable=terrain_var, state="readonly")
                        terrain_dropdown['values'] = available_terrain
                        terrain_dropdown.pack(padx=10, pady=10)

                        def confirm_purchase():
                            selected_terrain = terrain_dropdown.get()
                            if not selected_terrain:
                                messagebox.showerror("Error", "Please select a terrain tile.")
                                return
                            selected_id = int(selected_terrain.split('.')[0]) - 1
                            terrain_tile = self.game_state.terrain_tiles[selected_id]
                            if self.selected_player.ec < terrain_tile.purchase_cost:
                                messagebox.showerror("Error", "Insufficient Eco-Credits to purchase this terrain.")
                                return
                            self.selected_player.ec -= terrain_tile.purchase_cost
                            terrain_tile.owned_by = self.selected_player.name
                            self.refresh_terrain()
                            purchase_window.destroy()
                            # After purchasing, re-attempt to find the resource
                            distance_new, source_tile_index_new = self.find_nearest_resource(terrain_id, res)
                            if source_tile_index_new is not None:
                                new_factory.transportation[res] = {"type": trans_type, "distance": distance_new}
                                self.refresh_tabs()
                            else:
                                messagebox.showerror("Error", f"Failed to acquire the required resource: {res}.")
                                # Refund factory construction cost
                                self.selected_player.ec += new_factory.construction_cost
                                return

                        ttk.Button(purchase_window, text="Purchase", command=confirm_purchase).pack(pady=10)
                        ttk.Button(purchase_window, text="Cancel", command=purchase_window.destroy).pack()
                        self.wait_window(purchase_window)
                        # After purchase, check if resource is now available
                        distance_new, source_tile_index_new = self.find_nearest_resource(terrain_id, res)
                        if source_tile_index_new is not None:
                            new_factory.transportation[res] = {"type": trans_type, "distance": distance_new}
                        else:
                            messagebox.showerror("Error", f"Resource {res} still not available.")
                            # Refund factory construction cost
                            self.selected_player.ec += new_factory.construction_cost
                            return
                    else:
                        messagebox.showerror("Error", f"Cannot add factory without required resource: {res}.")
                        # Refund factory construction cost
                        self.selected_player.ec += new_factory.construction_cost
                        return
                else:
                    new_factory.transportation[res] = {"type": trans_type, "distance": distance}

        # Assign workers based on requirements
        for role, count in new_factory.workers_required.items():
            available_workers = [w for w in self.selected_player.workers if w.role == role]
            if len(available_workers) < count:
                messagebox.showwarning("Warning", f"Not enough {role}s to assign to this factory.")
            for i in range(min(count, len(available_workers))):
                worker = available_workers[i]
                new_factory.workers_assigned[role] = new_factory.workers_assigned.get(role, 0) + 1

        # Add the factory to player's list
        self.selected_player.factories.append(new_factory)
        self.refresh_factories()
        window.destroy()
        messagebox.showinfo("Success", f"{new_factory.name} added successfully.")

    def find_nearest_resource(self, factory_terrain_index: int, resource: str) -> tuple[int, Optional[int]]:
        min_distance = float('inf')
        source_tile_index = None
        for i, tile in enumerate(self.game_state.terrain_tiles):
            if tile.owned_by != self.selected_player.name:
                continue
            if resource in tile.resources:
                distance = self.calculate_distance(factory_terrain_index, i)
                if distance < min_distance:
                    min_distance = distance
                    source_tile_index = i
        return min_distance, source_tile_index

    def calculate_distance(self, index1: int, index2: int) -> int:
        # Assuming 4x5 grid, index from 0 to 19
        row1, col1 = divmod(index1, 5)
        row2, col2 = divmod(index2, 5)
        return abs(row1 - row2) + abs(col1 - col2)

    def remove_factory(self):
        selected_item = self.factory_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No factory selected.")
            return
        factory_name = self.factory_tree.item(selected_item, 'values')[0]
        factory = next((f for f in self.selected_player.factories if f.name == factory_name), None)
        if factory:
            # Refund construction cost
            self.selected_player.ec += factory.construction_cost
            # Remove factory
            self.selected_player.factories.remove(factory)
            self.factory_tree.delete(selected_item)
            self.refresh_factories()
            messagebox.showinfo("Success", f"{factory.name} removed successfully.")

    # ---------------------- Technology Management ----------------------

    def purchase_technology_dialog(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return

        add_window = tk.Toplevel(self)
        add_window.title("Purchase Technology")
        add_window.geometry("600x400")
        add_window.configure(bg="#F0F4F7")

        ttk.Label(add_window, text="Select Technology:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        tech_type_var = tk.StringVar()
        tech_names = [tech.name for tech in self.technologies_list]
        tech_dropdown = ttk.Combobox(add_window, textvariable=tech_type_var, state="readonly")
        tech_dropdown['values'] = tech_names
        tech_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # Display selected technology details
        tech_details = tk.Text(add_window, width=60, height=15, wrap='word')
        tech_details.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        def display_tech_details(event):
            selected_tech_name = tech_type_var.get()
            tech = next((t for t in self.technologies_list if t.name == selected_tech_name), None)
            if tech:
                details = (
                    f"Name: {tech.name}\n"
                    f"Category: {tech.category}\n"
                    f"Cost: {tech.cost} EC\n"
                    f"Maintenance: {tech.maintenance} EC/round\n"
                    f"Effect: {tech.effect}\n"
                    f"Prerequisites: {', '.join(tech.prerequisites) if tech.prerequisites else 'None'}"
                )
                tech_details.delete(1.0, tk.END)
                tech_details.insert(tk.END, details)

        tech_dropdown.bind("<<ComboboxSelected>>", display_tech_details)

        ttk.Button(
            add_window,
            text="Purchase",
            command=lambda: self.purchase_technology(tech_type_var.get(), add_window)
        ).grid(row=2, column=0, columnspan=2, pady=20)

    def purchase_technology(self, tech_name: str, window):
        if not tech_name:
            messagebox.showerror("Error", "Please select a technology.")
            return
        tech = next((t for t in self.technologies_list if t.name == tech_name), None)
        if not tech:
            messagebox.showerror("Error", "Invalid technology selected.")
            return
        # Check if player can afford
        if self.selected_player.ec < tech.cost:
            messagebox.showerror("Error", "Insufficient Eco-Credits to purchase this technology.")
            return
        # Check prerequisites
        for prereq in tech.prerequisites:
            if prereq not in [t.name for t in self.selected_player.technologies]:
                messagebox.showerror("Error", f"Prerequisite '{prereq}' not met.")
                return
        # Deduct cost
        self.selected_player.ec -= tech.cost
        # Add technology
        self.selected_player.technologies.append(tech)
        self.refresh_technologies()
        window.destroy()
        messagebox.showinfo("Success", f"{tech.name} purchased successfully.")

    def remove_technology(self):
        selected_item = self.tech_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No technology selected.")
            return
        tech_name = self.tech_tree.item(selected_item, 'values')[0]
        tech = next((t for t in self.selected_player.technologies if t.name == tech_name), None)
        if tech:
            # Refund half the cost (optional)
            refund = tech.cost // 2
            self.selected_player.ec += refund
            # Remove technology
            self.selected_player.technologies.remove(tech)
            self.tech_tree.delete(selected_item)
            self.refresh_technologies()
            messagebox.showinfo("Success", f"{tech.name} removed successfully. Refunded {refund} EC.")

    # ---------------------- Worker Management ----------------------

    def hire_worker_dialog(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return

        add_window = tk.Toplevel(self)
        add_window.title("Hire Worker")
        add_window.geometry("400x300")
        add_window.configure(bg="#F0F4F7")

        ttk.Label(add_window, text="Select Worker Role:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        worker_role_var = tk.StringVar()
        worker_roles = ["Engineer", "Technician", "Environmental Advisor", "Universal Worker"]
        worker_dropdown = ttk.Combobox(add_window, textvariable=worker_role_var, state="readonly")
        worker_dropdown['values'] = worker_roles
        worker_dropdown.current(0)
        worker_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # Display worker details
        worker_details = tk.Text(add_window, width=40, height=5, wrap='word')
        worker_details.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        def display_worker_details(event):
            selected_role = worker_role_var.get()
            worker_info = {
                "Engineer": {"salary": 50, "benefit": "+20% production in advanced factories, or +10% in basic factories."},
                "Technician": {"salary": 30, "benefit": "Maintains baseline production. Required for certain factories."},
                "Environmental Advisor": {"salary": 40, "benefit": "-3 pollution in the factory they’re assigned to."},
                "Universal Worker": {"salary": 20, "benefit": "Minimal production help; no special pollution or efficiency bonuses."}
            }
            if selected_role in worker_info:
                details = (
                    f"Role: {selected_role}\n"
                    f"Salary: {worker_info[selected_role]['salary']} EC/round\n"
                    f"Benefit: {worker_info[selected_role]['benefit']}"
                )
                worker_details.delete(1.0, tk.END)
                worker_details.insert(tk.END, details)

        worker_dropdown.bind("<<ComboboxSelected>>", display_worker_details)

        ttk.Button(
            add_window,
            text="Hire",
            command=lambda: self.hire_worker(worker_role_var.get(), add_window)
        ).grid(row=2, column=0, columnspan=2, pady=20)

    def hire_worker(self, role: str, window):
        worker_info = {
            "Engineer": {"salary": 50, "benefit": "+20% production in advanced factories, or +10% in basic factories."},
            "Technician": {"salary": 30, "benefit": "Maintains baseline production. Required for certain factories."},
            "Environmental Advisor": {"salary": 40, "benefit": "-3 pollution in the factory they’re assigned to."},
            "Universal Worker": {"salary": 20, "benefit": "Minimal production help; no special pollution or efficiency bonuses."}
        }
        if role not in worker_info:
            messagebox.showerror("Error", "Invalid worker role selected.")
            return
        worker = Worker(
            role=role,
            salary=worker_info[role]["salary"],
            benefit=worker_info[role]["benefit"]
        )
        # Check if player can afford
        if self.selected_player.ec < worker.salary:
            messagebox.showerror("Error", "Insufficient Eco-Credits to hire this worker.")
            return
        # Deduct salary
        self.selected_player.ec -= worker.salary
        self.selected_player.workers.append(worker)
        self.worker_tree.insert("", tk.END, values=(worker.role, worker.salary, worker.benefit))
        window.destroy()
        messagebox.showinfo("Success", f"{role} hired successfully.")

    def assign_worker_dialog_fixed(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return
        if not self.selected_player.workers:
            messagebox.showerror("Error", "No workers available to assign.")
            return
        if not self.selected_player.factories:
            messagebox.showerror("Error", "No factories available to assign workers.")
            return

        assign_window = tk.Toplevel(self)
        assign_window.title("Assign Worker")
        assign_window.geometry("500x300")
        assign_window.configure(bg="#F0F4F7")

        ttk.Label(assign_window, text="Select Worker:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        worker_var = tk.StringVar()
        workers = [f"{w.role} #{i + 1}" for i, w in enumerate(self.selected_player.workers)]
        worker_dropdown = ttk.Combobox(assign_window, textvariable=worker_var, state="readonly")
        worker_dropdown['values'] = workers
        worker_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(assign_window, text="Select Factory:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        factory_var = tk.StringVar()
        factories = [factory.name for factory in self.selected_player.factories]
        factory_dropdown = ttk.Combobox(assign_window, textvariable=factory_var, state="readonly")
        factory_dropdown['values'] = factories
        factory_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Button(
            assign_window,
            text="Assign",
            command=lambda: self.assign_worker(worker_var.get(), factory_var.get(), assign_window)
        ).grid(row=2, column=0, columnspan=2, pady=20)

    # Replace the original assign_worker_dialog with the fixed one
    assign_worker_dialog = assign_worker_dialog_fixed

    def assign_worker_fixed(self, worker_selection: str, factory_name: str, window):
        if not worker_selection or not factory_name:
            messagebox.showerror("Error", "Please select both worker and factory.")
            return
        # Extract worker index
        try:
            worker_index = int(worker_selection.split('#')[1]) - 1
            worker = self.selected_player.workers[worker_index]
        except (IndexError, ValueError):
            messagebox.showerror("Error", "Invalid worker selection.")
            return
        factory = next((f for f in self.selected_player.factories if f.name == factory_name), None)
        if not factory:
            messagebox.showerror("Error", "Invalid factory selected.")
            return
        # Normalize worker.role to ensure no leading/trailing spaces and correct casing
        worker_role = worker.role.strip()
        # Check if factory requires this worker role
        if worker_role not in factory.workers_required:
            messagebox.showerror("Error", f"{worker_role} is not required for {factory.name}.")
            return
        required = factory.workers_required.get(worker_role, 0)
        assigned = factory.workers_assigned.get(worker_role, 0)
        if assigned >= required:
            messagebox.showerror("Error", f"No need for more {worker_role}s in {factory.name}.")
            return
        # Assign worker
        factory.workers_assigned[worker_role] = assigned + 1
        self.refresh_factories()
        window.destroy()
        messagebox.showinfo("Success", f"{worker_role} assigned to {factory.name}.")

    # Replace the original assign_worker method with the fixed one
    assign_worker = assign_worker_fixed

    def remove_worker(self):
        selected_item = self.worker_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No worker selected.")
            return
        worker_role = self.worker_tree.item(selected_item, 'values')[0]
        # Find the first worker with the selected role
        worker = next((w for w in self.selected_player.workers if w.role == worker_role), None)
        if worker:
            # Remove worker from any factories
            for factory in self.selected_player.factories:
                if worker.role in factory.workers_assigned:
                    if factory.workers_assigned[worker.role] > 0:
                        factory.workers_assigned[worker.role] -= 1
                        if factory.workers_assigned[worker.role] == 0:
                            del factory.workers_assigned[worker.role]
            # Remove worker
            self.selected_player.workers.remove(worker)
            self.worker_tree.delete(selected_item)
            self.refresh_factories()
            messagebox.showinfo("Success", f"{worker.role} removed successfully.")

    # ---------------------- Resource Management ----------------------

    def trade_resources_dialog(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return

        trade_window = tk.Toplevel(self)
        trade_window.title("Trade Resources")
        trade_window.geometry("500x300")
        trade_window.configure(bg="#F0F4F7")

        ttk.Label(trade_window, text="Offer Resource:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        offer_var = tk.StringVar()
        offer_dropdown = ttk.Combobox(trade_window, textvariable=offer_var, state="readonly")
        offer_dropdown['values'] = [
            "Minerals", "Wood", "Oil", "Water", "Plastics",
            "Bioplastics", "Solar Panel", "Wind Turbine", "Recycled Materials",
            "Manufactured Goods", "Fish", "Consultancy Services"
        ]
        offer_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(trade_window, text="Offer Quantity:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        offer_qty_var = tk.StringVar()
        offer_qty_entry = ttk.Entry(trade_window, textvariable=offer_qty_var)
        offer_qty_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(trade_window, text="Request Resource:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        request_var = tk.StringVar()
        request_dropdown = ttk.Combobox(trade_window, textvariable=request_var, state="readonly")
        request_dropdown['values'] = [
            "Minerals", "Wood", "Oil", "Water", "Plastics",
            "Bioplastics", "Solar Panel", "Wind Turbine", "Recycled Materials",
            "Manufactured Goods", "Fish", "Consultancy Services"
        ]
        request_dropdown.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(trade_window, text="Request Quantity:").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        request_qty_var = tk.StringVar()
        request_qty_entry = ttk.Entry(trade_window, textvariable=request_qty_var)
        request_qty_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Button(
            trade_window,
            text="Trade",
            command=lambda: self.perform_trade(offer_var.get(), offer_qty_var.get(), request_var.get(), request_qty_var.get(), trade_window)
        ).grid(row=4, column=0, columnspan=2, pady=20)

    def perform_trade(self, offer_res: str, offer_qty: str, request_res: str, request_qty: str, window):
        try:
            offer_qty = int(offer_qty)
            request_qty = int(request_qty)
        except ValueError:
            messagebox.showerror("Error", "Quantities must be integers.")
            return
        if offer_qty <= 0 or request_qty <= 0:
            messagebox.showerror("Error", "Quantities must be positive.")
            return
        # Check if player has enough offer resource
        produced = self.get_produced_resource(offer_res)
        if produced < offer_qty:
            messagebox.showerror("Error", f"Not enough {offer_res} to offer.")
            return
        # Assume base price: 50 EC per unit
        offer_value = offer_qty * 50
        request_value = request_qty * 50
        # Check if player can afford the trade
        if self.selected_player.ec < request_value:
            messagebox.showerror("Error", "Insufficient Eco-Credits to fulfill the trade.")
            return
        # Execute trade
        self.selected_player.ec += offer_value
        self.selected_player.ec -= request_value
        self.refresh_resources()
        window.destroy()
        messagebox.showinfo("Trade", "Trade executed successfully.")

    def get_produced_resource(self, resource: str) -> int:
        produced = 0
        for factory in self.selected_player.factories:
            if resource in factory.output:
                produced += factory.output[resource]
        return produced

    # ---------------------- Overridden calculate_round for Pollution & Costs ----------------------

    def calculate_round_original(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return
        # Calculate total pollution and apply carbon tax
        total_pollution = self.calculate_total_pollution()
        carbon_tax = 5 * total_pollution

        # Calculate total salaries and maintenance
        total_salary = sum(worker.salary for worker in self.selected_player.workers)
        total_maintenance = sum(tech.maintenance for tech in self.selected_player.technologies)

        # Calculate transportation costs
        transportation_cost = 0
        for factory in self.selected_player.factories:
            for trans in factory.transportation.values():
                trans_type = trans['type']
                distance = trans['distance']
                transport_info = next((t for t in self.transportation_types if t['type'] == trans_type), None)
                if transport_info:
                    cost = transport_info['cost_per_distance'] * distance
                    # Check for technology effects that reduce transportation costs
                    for tech in self.selected_player.technologies:
                        if "Reduce Fossil Fuel transportation costs by 10 EC per distance unit." in tech.effect and trans_type == "Fossil Fuel":
                            cost = max(cost - 10 * distance, 0)
                    transportation_cost += cost

        # Total expenses
        total_expenses = carbon_tax + total_salary + total_maintenance + transportation_cost

        # Deduct expenses from EC
        if self.selected_player.ec < total_expenses:
            messagebox.showerror("Error", "Insufficient Eco-Credits to cover the expenses this round.")
            return
        self.selected_player.ec -= total_expenses
        self.selected_player.pp = total_pollution  # Update Pollution Points

        # Optionally, add production revenue
        production_revenue = 0
        for factory in self.selected_player.factories:
            for res, qty in factory.output.items():
                if res == "Consultancy Services":
                    production_revenue += qty
                else:
                    production_revenue += qty * 50
        self.selected_player.ec += production_revenue

        # Update dashboard and other tabs
        self.refresh_tabs()
        messagebox.showinfo("Round Calculated", f"Round {self.game_state.current_round} completed.\n"
                                               f"Expenses: {total_expenses} EC\n"
                                               f"Revenue: {production_revenue} EC\n"
                                               f"Net Change: {production_revenue - total_expenses} EC")
        self.game_state.current_round += 1
        if self.game_state.current_round > self.game_state.max_rounds:
            self.end_game()

    # The original calculate_round method is replaced by the fixed version above.

# ---------------------- Main Execution ----------------------

def main():
    game_state = GameState()
    # Uncomment below lines to add example players for demonstration
    # game_state.add_player("Player 1")
    # game_state.add_player("Player 2")

    app = CompanionApp(game_state)
    app.mainloop()

if __name__ == "__main__":
    main()
