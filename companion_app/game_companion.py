import tkinter as tk
from tkinter import ttk, messagebox

########################################################################
# 1. DATA DEFINITIONS
########################################################################

# We define a simplified set of Factories, Technologies, Workers, etc.
# You can expand these dictionaries to include all from your ruleset.

FACTORIES = {
    "Timber Logging Camp": {
        "construction_cost": 150,
        "operational_cost": 20,
        "base_pollution": 3,
        "output_type": "Timber",
        "output_per_round": 2,
        "terrain_requirement": ["Forest"],  # Example requirement
    },
    "Crop Farm": {
        "construction_cost": 200,
        "operational_cost": 25,
        "base_pollution": 2,
        "output_type": "Agriculture",
        "output_per_round": 3,
        "terrain_requirement": ["Plains", "Coastal"], 
    },
    "Mine & Smelter": {
        "construction_cost": 300,
        "operational_cost": 40,
        "base_pollution": 8,
        "output_type": "Mineral",
        "output_per_round": 2,
        "terrain_requirement": ["Mountain"],
    },
    "Bioplastics Plant": {
        "construction_cost": 250,
        "operational_cost": 30,
        "base_pollution": 5,
        "output_type": "Bioplastics",
        "output_per_round": 2,
        "input_needed": ["Timber", "Agriculture"], 
    },
    "Urban Manufacturing Plant": {
        "construction_cost": 300,
        "operational_cost": 35,
        "base_pollution": 6,
        "output_type": "ManufacturedGoods",
        "output_per_round": 2,  # requires Minerals or Recycled
        "terrain_requirement": ["Urban"],
    },
}

TECHNOLOGIES = {
    "Solar-Wind Hybrid Array": {
        "cost": 250,
        "maintenance": 20,
        "pollution_reduction": 3,   # applies to a single factory
        "op_cost_reduction": 10,   # reduces operational cost 
    },
    "Advanced Automation Module": {
        "cost": 200,
        "maintenance": 15,
        "production_bonus_percent": 20,  # +20% production
    },
    "Carbon Capture System": {
        "cost": 250,
        "maintenance": 20,
        "pollution_reduction": 6,  # drastically cuts pollution
    },
    "Industrial Recycling Unit": {
        "cost": 200,
        "maintenance": 15,
        "pollution_reduction": 3,  
        "extra_income": 5,         # e.g. from turning waste into resources
    },
}

WORKERS = {
    "Engineer": {
        "salary": 50,
        "production_bonus_percent": 20,  # advanced factories get +20% output
    },
    "Technician": {
        "salary": 30,
        "production_bonus_percent": 0,   # just ensures stable production
    },
    "Environmental Advisor": {
        "salary": 40,
        "pollution_reduction": 3,        # subtract from one factory's pollution
    },
    "Universal Worker": {
        "salary": 20,
        "production_bonus_percent": 0,
    },
}

ACTIONS = [
    "Buy Factory",
    "Buy Worker",
    "Buy Technology",
    "Buy Resource",
    "Sell Resource",
    "Do Nothing",
]

########################################################################
# 2. PLAYER & GAME STATE CLASSES
########################################################################

class Player:
    """
    Holds the state of a single player: capital, pollution, 
    owned factories, technologies, workers, and resources.
    """
    def __init__(self, name):
        self.name = name
        self.capital = 1500
        self.pollution = 0
        self.resources = {}  # e.g., {"Timber": 0, "Agriculture": 0, ...}
        self.factories = []  # each factory is a dict with details
        self.technologies = []
        self.workers = []
        self.terrain = []    # track which terrain tiles they own (optional)
        
    def add_resource(self, rtype, amount):
        self.resources[rtype] = self.resources.get(rtype, 0) + amount

    def remove_resource(self, rtype, amount):
        if rtype in self.resources:
            self.resources[rtype] = max(0, self.resources[rtype] - amount)
    
    def get_resource_amount(self, rtype):
        return self.resources.get(rtype, 0)

    def add_factory(self, factory_name, terrain_type=None):
        """
        Add a new factory to the player's list of factories.
        terrain_type is optional if you want to check requirement.
        """
        factory_data = FACTORIES[factory_name]
        self.factories.append({
            "name": factory_name,
            "terrain_type": terrain_type,
            "technologies": [],       # which tech modules are attached
            "assigned_worker": None,  # which single worker is assigned
        })
    
    def add_technology(self, tech_name):
        self.technologies.append({
            "name": tech_name,
        })

    def add_worker(self, worker_type):
        self.workers.append({
            "type": worker_type,
        })

########################################################################
# 3. MAIN GAME CLASS
########################################################################

class EcoFactoryGame:
    """
    Manages the overall game state: players, rounds, and
    the end-of-round calculations (production, pollution, taxes).
    """
    def __init__(self):
        self.players = [
            Player("Player 1"),
            Player("Player 2"),
            Player("Player 3"),
            Player("Player 4"),
        ]
        self.round_number = 1
        self.max_rounds = 6  # end condition

    def perform_action(self, player_idx, action_type, sub_option):
        """
        Execute the chosen action for a given player.
        'sub_option' is typically the item name (factory, worker, tech, resource).
        """
        player = self.players[player_idx]

        if action_type == "Buy Factory":
            if sub_option in FACTORIES:
                cost = FACTORIES[sub_option]["construction_cost"]
                if player.capital >= cost:
                    player.capital -= cost
                    # (Optional) If terrain type matters, you can ask the user 
                    # which terrain tile they’re building on.
                    # For simplicity, we skip terrain checks here.
                    player.add_factory(sub_option)
                else:
                    messagebox.showwarning("Error", 
                        f"Not enough capital to build {sub_option}")
            else:
                messagebox.showinfo("Info", "Invalid factory selection.")

        elif action_type == "Buy Worker":
            if sub_option in WORKERS:
                salary = WORKERS[sub_option]["salary"]
                # No immediate cost besides salary each round, but you could 
                # decide that hiring also has an upfront cost. We’ll skip that.
                player.add_worker(sub_option)
            else:
                messagebox.showinfo("Info", "Invalid worker selection.")

        elif action_type == "Buy Technology":
            if sub_option in TECHNOLOGIES:
                cost = TECHNOLOGIES[sub_option]["cost"]
                if player.capital >= cost:
                    player.capital -= cost
                    player.add_technology(sub_option)
                else:
                    messagebox.showwarning("Error", 
                        f"Not enough capital to buy {sub_option}")
            else:
                messagebox.showinfo("Info", "Invalid technology selection.")

        elif action_type == "Buy Resource":
            # Example: Let’s assume a simple fixed cost for resources
            # (like 40 EC for 1 Timber, 25 EC for 1 Agriculture, etc.)
            # For demonstration only. Expand as needed.
            resource_prices = {
                "Timber": 40,
                "Agriculture": 25,
                "Mineral": 40,
                "Bioplastics": 50,
            }
            if sub_option in resource_prices:
                cost = resource_prices[sub_option]
                if player.capital >= cost:
                    player.capital -= cost
                    player.add_resource(sub_option, 1)
                else:
                    messagebox.showwarning("Error", 
                        f"Not enough capital to buy 1 unit of {sub_option}")
            else:
                messagebox.showinfo("Info", "Invalid resource selection.")

        elif action_type == "Sell Resource":
            # Sell 1 unit of the resource to the bank at a base price
            # This is a simple approach; you could open a numeric entry, etc.
            resource_sell_prices = {
                "Timber": 30,
                "Agriculture": 20,
                "Mineral": 40,
                "Bioplastics": 50,
                "ManufacturedGoods": 50,
            }
            if player.get_resource_amount(sub_option) > 0:
                price = resource_sell_prices.get(sub_option, 0)
                player.remove_resource(sub_option, 1)
                player.capital += price
            else:
                messagebox.showwarning("Error", 
                    f"You have no {sub_option} to sell.")

        # "Do Nothing" -> no action
        else:
            pass

    def end_round_calculations(self):
        """
        After all players have done their actions, we compute:
        - Production from factories (and apply worker & tech bonuses)
        - Pollution from factories (and apply worker & tech reductions)
        - Carbon tax
        - Worker salaries
        - Tech maintenance
        """
        for player in self.players:
            # 1) Production and pollution from each factory
            round_pollution = 0
            for f in player.factories:
                f_info = FACTORIES[f["name"]]
                base_poll = f_info["base_pollution"]
                op_cost = f_info["operational_cost"]

                # Check assigned worker
                assigned_worker_data = None
                if f["assigned_worker"] is not None:
                    # f["assigned_worker"] might store an index or name
                    # For simplicity, let's store the name of the worker
                    # in the factory dict. Then find the worker data:
                    assigned_worker_data = WORKERS.get(f["assigned_worker"], {})

                # Production (base)
                base_output = f_info.get("output_per_round", 0)

                # If factory requires an input resource, check if player has it
                # For demonstration, let's handle Bioplastics as an example
                needed = f_info.get("input_needed", [])
                can_produce = True
                if needed:
                    # The factory might require 1 unit of ANY input in needed
                    # We'll assume it requires 1 unit total for the round
                    has_input = False
                    for r in needed:
                        if player.get_resource_amount(r) > 0:
                            has_input = True
                            # consume it
                            player.remove_resource(r, 1)
                            break
                    if not has_input:
                        can_produce = False  # no production

                # Worker bonus
                if assigned_worker_data:
                    # Production bonus
                    bonus_pct = assigned_worker_data.get("production_bonus_percent", 0)
                else:
                    bonus_pct = 0

                # Technologies on factory
                tech_pollution_reduction = 0
                tech_opcost_reduction = 0
                tech_production_bonus = 0
                tech_extra_income = 0

                for tech_item in f["technologies"]:
                    t_data = TECHNOLOGIES[tech_item]
                    # accumulate effects
                    if "pollution_reduction" in t_data:
                        tech_pollution_reduction += t_data["pollution_reduction"]
                    if "op_cost_reduction" in t_data:
                        tech_opcost_reduction += t_data["op_cost_reduction"]
                    if "production_bonus_percent" in t_data:
                        tech_production_bonus += t_data["production_bonus_percent"]
                    if "extra_income" in t_data:
                        tech_extra_income += t_data["extra_income"]

                # If an Environmental Advisor is assigned
                env_advisor_reduce = 0
                if assigned_worker_data and "pollution_reduction" in assigned_worker_data:
                    env_advisor_reduce = assigned_worker_data["pollution_reduction"]

                # Final pollution for this factory
                final_factory_poll = base_poll - tech_pollution_reduction - env_advisor_reduce
                if final_factory_poll < 0:
                    final_factory_poll = 0

                round_pollution += final_factory_poll

                # Final operational cost
                final_op_cost = op_cost - tech_opcost_reduction
                if final_op_cost < 0:
                    final_op_cost = 0

                # Pay operational cost
                if player.capital >= final_op_cost:
                    player.capital -= final_op_cost
                else:
                    player.capital = 0  # or negative if you allow debt

                # Determine actual production
                if can_produce:
                    total_bonus = bonus_pct + tech_production_bonus
                    effective_output = base_output * (1 + total_bonus/100.0)
                    # simple rounding
                    produce_amount = int(round(effective_output))
                    
                    # Add the product to player resources
                    out_type = f_info["output_type"]
                    player.add_resource(out_type, produce_amount)

                    # Possibly add extra income from certain tech
                    if tech_extra_income > 0:
                        player.capital += tech_extra_income
                # else: no production due to missing input

            # 2) Summation of total pollution -> carbon tax
            player.pollution += round_pollution  # Accumulate pollution instead of resetting
            carbon_tax = 5 * player.pollution    # Calculate tax based on accumulated pollution
            if player.capital >= carbon_tax:
                player.capital -= carbon_tax
            else:
                player.capital = 0  # Or handle insufficient funds differently

            # 3) Pay worker salaries
            total_salaries = 0
            for w in player.workers:
                wtype = w["type"]
                total_salaries += WORKERS[wtype]["salary"]
            if player.capital >= total_salaries:
                player.capital -= total_salaries
            else:
                player.capital = 0

            # 4) Pay tech maintenance
            # Each tech the player owns has a maintenance cost
            total_tech_maintenance = 0
            for t in player.technologies:
                t_data = TECHNOLOGIES[t["name"]]
                if "maintenance" in t_data:
                    total_tech_maintenance += t_data["maintenance"]
            if player.capital >= total_tech_maintenance:
                player.capital -= total_tech_maintenance
            else:
                player.capital = 0

        # Increment round
        self.round_number += 1

    def assign_worker_to_factory(self, player_idx, factory_name, worker_name):
        """
        Quick utility to assign a worker to a factory. 
        In a more advanced UI, you’d select which worker 
        goes to which factory, etc.
        """
        player = self.players[player_idx]
        # find the factory and assign
        for f in player.factories:
            if f["name"] == factory_name:
                f["assigned_worker"] = worker_name
                break

    def check_end_game(self):
        """Check if we reached the last round or any other end condition."""
        if self.round_number > self.max_rounds:
            return True
        return False

    def compute_winner(self):
        """
        According to the revised rules, final score = capital / (1 + pollution).
        We’ll just read player.pollution from the last round. 
        """
        results = []
        for p in self.players:
            score = 0
            # If pollution is 0, score = capital / 1
            # Otherwise = capital / (1 + pollution)
            score = p.capital / (1 + p.pollution)
            results.append((p.name, p.capital, p.pollution, score))

        # Sort descending by score
        results.sort(key=lambda x: x[3], reverse=True)
        return results

########################################################################
# 4. TKINTER GUI
########################################################################

class EcoFactoryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Eco-Factory Challenge Companion App")

        self.game = EcoFactoryGame()

        # Create UI for each player's actions in separate frames
        self.player_frames = []
        self.action_vars = []
        self.subaction_vars = []
        
        self.create_gui()

    def create_gui(self):
        top_label = tk.Label(self, text="Eco-Factory Challenge Companion", 
                             font=("Arial", 16, "bold"))
        top_label.pack(pady=10)

        container = tk.Frame(self)
        container.pack()

        for i, player in enumerate(self.game.players):
            frame = tk.LabelFrame(container, text=player.name, padx=5, pady=5)
            frame.grid(row=i // 2, column=i % 2, padx=5, pady=5, sticky="nsew")

            # Action dropdown
            action_var = tk.StringVar(value=ACTIONS[0])
            action_label = tk.Label(frame, text="Choose Action:")
            action_label.pack()
            action_menu = ttk.Combobox(frame, textvariable=action_var, 
                                       values=ACTIONS, state="readonly")
            action_menu.pack()

            # Subaction dropdown (factories, workers, tech, resources)
            subaction_var = tk.StringVar(value="")
            subaction_label = tk.Label(frame, text="Select Item:")
            subaction_label.pack()
            subaction_menu = ttk.Combobox(frame, textvariable=subaction_var, 
                                          values=[], state="readonly")
            subaction_menu.pack()

            # Create closure for event handling
            def make_action_handler(menu, a_var, s_var):
                def handler(event):
                    selected = a_var.get()
                    if selected == "Buy Factory":
                        menu.config(values=list(FACTORIES.keys()))
                    elif selected == "Buy Worker":
                        menu.config(values=list(WORKERS.keys()))
                    elif selected == "Buy Technology":
                        menu.config(values=list(TECHNOLOGIES.keys()))
                    elif selected == "Buy Resource":
                        menu.config(values=["Timber","Agriculture","Mineral","Bioplastics"])
                    elif selected == "Sell Resource":
                        menu.config(values=["Timber","Agriculture","Mineral","Bioplastics","ManufacturedGoods"])
                    else:
                        menu.config(values=[])
                    s_var.set("")  # Reset selection
                return handler

            # Bind the handler
            action_menu.bind("<<ComboboxSelected>>", 
                            make_action_handler(subaction_menu, action_var, subaction_var))

            # A button to confirm the action
            def on_confirm_action(idx=i, a_var=action_var, s_var=subaction_var):
                act = a_var.get()
                sub = s_var.get()
                self.game.perform_action(idx, act, sub)
                self.refresh_ui()

            confirm_btn = tk.Button(frame, text="Confirm Action",
                                    command=on_confirm_action)
            confirm_btn.pack(pady=5)

            # Info label about capital, pollution, resources
            info_label = tk.Label(frame, text=self.get_player_info_text(i),
                                  justify="left")
            info_label.pack(pady=5)

            self.player_frames.append(frame)
            self.action_vars.append(action_var)
            self.subaction_vars.append(subaction_var)

        # Button to end the round
        end_round_btn = tk.Button(self, text="End Round & Calculate",
                                  command=self.end_round)
        end_round_btn.pack(pady=10)

        # A label to show current round
        self.round_label = tk.Label(self, text=f"Round: {self.game.round_number}")
        self.round_label.pack()

        # We’ll also keep a label for final results if the game ends
        self.final_result_label = tk.Label(self, text="", fg="blue")
        self.final_result_label.pack(pady=10)

        self.refresh_ui()

    def refresh_ui(self):
        """Refresh capital/pollution info for each player frame."""
        for i, frame in enumerate(self.player_frames):
            # The last widget inside is our info_label
            info_label = frame.winfo_children()[-1]
            info_label.config(text=self.get_player_info_text(i))

        self.round_label.config(text=f"Round: {self.game.round_number}")

    def get_player_info_text(self, idx):
        """Returns a text summary for the player's current state."""
        p = self.game.players[idx]
        resources_text = ", ".join(f"{k}:{v}" for k,v in p.resources.items() if v > 0)
        if not resources_text:
            resources_text = "None"
        info = (
            f"Capital: {p.capital}\n"
            f"Pollution: {p.pollution}\n"
            f"Resources: {resources_text}\n"
            f"Factories: {[f['name'] for f in p.factories]}\n"
            f"Workers: {[w['type'] for w in p.workers]}\n"
            f"Technologies: {[t['name'] for t in p.technologies]}"
        )
        return info

    def end_round(self):
        """Perform end-round calculations and check for game end."""
        self.game.end_round_calculations()
        self.refresh_ui()

        if self.game.check_end_game():
            # Show final scores
            results = self.game.compute_winner()
            result_str = "FINAL RESULTS:\n"
            rank = 1
            for r in results:
                name, cap, poll, score = r
                result_str += (f"{rank}) {name} | "
                               f"Capital={cap} | Pollution={poll} | "
                               f"Score={round(score,2)}\n")
                rank += 1
            
            self.final_result_label.config(text=result_str)
            messagebox.showinfo("Game Over", "The game has ended!")
            

########################################################################
# 5. MAIN ENTRY POINT
########################################################################

if __name__ == "__main__":
    app = EcoFactoryApp()
    app.mainloop()
