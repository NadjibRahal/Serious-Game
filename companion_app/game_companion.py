#!/usr/bin/env python3
"""
Eco-Factory Challenge (Companion App) - Revised Version with Drop-Down Menus
Author: YourName
Description:
    A Tkinter-based GUI application for 4 players in the Eco-Factory Challenge.
    Instead of free-form text, the user selects actions from drop-down menus:
      - Buy Terrain
      - Buy Resource
      - Buy Factory
      - Buy Technology
      - Buy Worker
      - Add Transportation

    For each action type, a secondary drop-down menu appears, letting the user
    pick specific options (e.g., which terrain, which resource, which factory).
    For transportation, the user picks Hydrocarbon or Electric and enters distance.
    The app auto-calculates cost in EC and pollution, then applies changes to the
    selected player's data.

Features:
    - 4 Player frames with money, pollution, resources, factories, tech, workers
    - Round system with Next Round button to consume resources & produce EC
    - Save/Load game session to JSON
    - Undo last action
    - End game computing final ratio = capital / (1 + pollution)
"""

import tkinter as tk
from tkinter import messagebox, filedialog
import json
import os

################################################################################
# DATA DEFINITIONS
################################################################################

# Terrains (20 total) with example prices:
# We can treat them like a grid or just name them T1..T20. 
# A real approach might store which player owns which, etc.
# For demonstration, we only track cost here; the user picks one to buy.
TERRAINS = {
    "T1": 200,
    "T2": 250,
    "T3": 300,
    "T4": 350,
    "T5": 200,
    "T6": 250,
    "T7": 300,
    "T8": 350,
    "T9": 200,
    "T10": 250,
    "T11": 300,
    "T12": 350,
    "T13": 200,
    "T14": 250,
    "T15": 300,
    "T16": 350,
    "T17": 200,
    "T18": 250,
    "T19": 300,
    "T20": 350,
}

# Resources
RESOURCES = {
    "Bois": 20,      # sample cost to buy 1 unit of Bois
    "Eau": 15,       # cost for 1 unit of Eau
    "Carbone": 30,   # cost for 1 unit of Carbone
    "PierreFer": 40, # cost for 1 unit of Pierre + Fer
    "Petrole": 50,   # cost for 1 unit of Petrole
}

# Factories
FACTORIES = {
    "AgroVerde": {
        "cost": 200,
        "pollution_per_round": 1,
        "min_workers": 2,
        "max_workers": 4,
        "income_per_round": 100,
        "resource_requirements": {"Bois": 1, "Eau": 1},
        "max_owned_per_player": 4
    },
    "AutoTech": {
        "cost": 500,
        "pollution_per_round": 4,
        "min_workers": 6,
        "max_workers": 10,
        "income_per_round": 250,
        "resource_requirements": {"PierreFer": 2, "Petrole": 1},
        "max_owned_per_player": 3
    },
    "Elektronix": {
        "cost": 350,
        "pollution_per_round": 3,
        "min_workers": 5,
        "max_workers": 8,
        "income_per_round": 200,
        "resource_requirements": {"Carbone": 1, "Petrole": 2},
        "max_owned_per_player": 5
    },
    "EcoCycle": {
        "cost": 300,
        "pollution_per_round": 2,
        "min_workers": 4,
        "max_workers": 6,
        "income_per_round": 150,
        "resource_requirements": {"Carbone": 1, "PierreFer": 1},
        "max_owned_per_player": 6
    },
}

# Technologies
TECHNOLOGIES = {
    "Solar-Wind Hybrid Array": {
        "cost": 250,
        "maintenance": 20,
        "pollution_mod": -3,  # Reduces one factory’s pollution by 3
        "note": "Reduces factory operational cost by 10 EC/round"
    },
    "Advanced Automation Module": {
        "cost": 200,
        "maintenance": 15,
        "pollution_mod": 0,   # no direct pollution effect
        "note": "+20% production, needs Engineer"
    },
    "Carbon Capture System": {
        "cost": 250,
        "maintenance": 20,
        "pollution_mod": -6,
        "note": "Requires Env Advisor"
    },
    "Bioplastic Synthesis Upgrade": {
        "cost": 200,
        "maintenance": 10,
        "pollution_mod": 0,
        "note": "+10 EC per product sold from that factory"
    },
    "Industrial Recycling Unit": {
        "cost": 200,
        "maintenance": 15,
        "pollution_mod": -3,
        "note": "+5 EC/round synergy, needs Technician"
    },
    "Closed-Loop Water System": {
        "cost": 150,
        "maintenance": 10,
        "pollution_mod": -2,
        "note": "Requires Env Advisor, saves 5 EC/round disposal"
    },
    "Vertical Integration Logistics": {
        "cost": 300,
        "maintenance": 20,
        "pollution_mod": 0,
        "note": "2 factories on same tile, +5 EC/round transport savings"
    },
    "Urban Rooftop Farming": {
        "cost": 100,
        "maintenance": 5,
        "pollution_mod": +1,
        "note": "+2 produce units on Urban tile"
    },
}

# Workers (with cost if you want to track hiring cost):
WORKERS = {
    "Universal": 20,      # cost per worker (example) 
    "Engineer": 50,
    "Technician": 30,
    "Environmental": 40
}

# Transportation
TRANSPORTS = {
    "Hydrocarbon": {
        "cost_per_tile": 3,
        "pollution_per_tile": 1,
        "capacity": 3
    },
    "Electric": {
        "cost_per_tile": 6,
        "pollution_per_tile": 0.5,
        "capacity": 3
    }
}


################################################################################
# PLAYER DATA
################################################################################

class PlayerData:
    """
    Holds data for a single player:
      - money
      - pollution
      - resources
      - factories (list)
      - technologies
      - workers (dict)
      - action_history
    """
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.pollution = 0
        self.resources = {
            "Bois": 0,
            "Eau": 0,
            "Carbone": 0,
            "PierreFer": 0,
            "Petrole": 0
        }
        self.factories = []
        self.technologies = []
        self.workers = {
            "Universal": 0,
            "Engineer": 0,
            "Technician": 0,
            "Environmental": 0
        }
        self.action_history = []

    def to_dict(self):
        return {
            "name": self.name,
            "money": self.money,
            "pollution": self.pollution,
            "resources": self.resources,
            "factories": self.factories,
            "technologies": self.technologies,
            "workers": self.workers,
            "action_history": self.action_history
        }

    def from_dict(self, data):
        self.name = data["name"]
        self.money = data["money"]
        self.pollution = data["pollution"]
        self.resources = data["resources"]
        self.factories = data["factories"]
        self.technologies = data["technologies"]
        self.workers = data["workers"]
        self.action_history = data["action_history"]

################################################################################
# MAIN APP
################################################################################

class EcoFactoryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Eco-Factory Challenge Companion App")
        self.geometry("1200x650")
        self.resizable(False, False)

        # Game logic
        self.current_round = 1
        self.max_rounds = 6

        self.players = [
            PlayerData("Player A"),
            PlayerData("Player B"),
            PlayerData("Player C"),
            PlayerData("Player D"),
        ]

        self.undo_stack = []

        self.create_menu()
        self.create_main_frames()
        self.create_bottom_controls()
        self.update_all_displays()

    ############################
    # MENU
    ############################
    def create_menu(self):
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New / Reset", command=self.reset_game)
        file_menu.add_command(label="Save", command=self.save_game)
        file_menu.add_command(label="Load", command=self.load_game)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit_app)

        menubar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menubar)

    ############################
    # MAIN FRAMES
    ############################
    def create_main_frames(self):
        self.player_frames = []

        container = tk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True)

        for idx, player in enumerate(self.players):
            frame = tk.LabelFrame(container, text=player.name, padx=5, pady=5)
            frame.grid(row=0, column=idx, sticky='nsew', padx=5, pady=5)

            money_lbl = tk.Label(frame, text=f"Money (EC): {player.money}", font=("Arial", 10, "bold"))
            money_lbl.pack(anchor="w", pady=2)

            poll_lbl = tk.Label(frame, text=f"Pollution: {player.pollution}", font=("Arial", 10, "bold"))
            poll_lbl.pack(anchor="w", pady=2)

            res_lbl = tk.Label(frame, text=self._fmt_resources(player.resources), justify=tk.LEFT)
            res_lbl.pack(anchor="w", pady=2)

            fact_lbl = tk.Label(frame, text="Factories:\n(None)", justify=tk.LEFT)
            fact_lbl.pack(anchor="w", pady=2)

            tech_lbl = tk.Label(frame, text="Technologies:\n(None)", justify=tk.LEFT)
            tech_lbl.pack(anchor="w", pady=2)

            worker_lbl = tk.Label(frame, text=self._fmt_workers(player.workers), justify=tk.LEFT)
            worker_lbl.pack(anchor="w", pady=2)

            # Action input area (now with drop-down menus)
            input_frame = tk.Frame(frame)
            input_frame.pack(anchor="w", pady=5)

            # 1) Action Type
            tk.Label(input_frame, text="Action:").grid(row=0, column=0, sticky='w')
            action_type_var = tk.StringVar(value="Buy Terrain")
            action_type_options = [
                "Buy Terrain",
                "Buy Resource",
                "Buy Factory",
                "Buy Technology",
                "Buy Worker",
                "Add Transportation"
            ]
            action_type_menu = tk.OptionMenu(input_frame, action_type_var, *action_type_options)
            action_type_menu.grid(row=0, column=1, sticky='w', padx=5)

            # 2) Sub Drop-Down
            sub_type_var = tk.StringVar(value="T1")  # default
            sub_drop_menu = tk.OptionMenu(input_frame, sub_type_var, *TERRAINS.keys())
            sub_drop_menu.grid(row=1, column=1, sticky='w', padx=5)

            # 3) Additional Input (like distance or quantity)
            tk.Label(input_frame, text="Distance/Qte:").grid(row=2, column=0, sticky='w')
            extra_var = tk.StringVar(value="1")
            extra_entry = tk.Entry(input_frame, textvariable=extra_var, width=8)
            extra_entry.grid(row=2, column=1, sticky='w', padx=5)

            # We'll store references for usage
            # history box
            history_box = tk.Listbox(frame, height=8, width=26)
            history_box.pack(anchor="w", pady=5)

            # On change of action_type, we update sub_drop_menu options
            def on_action_type_change(*args, stv=sub_type_var):
                # Clear sub_type_var
                stv.set("")
                chosen = action_type_var.get()
                if chosen == "Buy Terrain":
                    menu_items = list(TERRAINS.keys())
                elif chosen == "Buy Resource":
                    menu_items = list(RESOURCES.keys())
                elif chosen == "Buy Factory":
                    menu_items = list(FACTORIES.keys())
                elif chosen == "Buy Technology":
                    menu_items = list(TECHNOLOGIES.keys())
                elif chosen == "Buy Worker":
                    menu_items = list(WORKERS.keys())
                elif chosen == "Add Transportation":
                    menu_items = list(TRANSPORTS.keys())
                else:
                    menu_items = []

                sub_drop_menu["menu"].delete(0, "end")
                for item in menu_items:
                    sub_drop_menu["menu"].add_command(
                        label=item, command=lambda value=item: stv.set(value)
                    )
                if menu_items:
                    stv.set(menu_items[0])

            action_type_var.trace("w", on_action_type_change)
            # initialize
            on_action_type_change()

            # Action Button
            add_btn = tk.Button(
                input_frame, text="Perform Action",
                command=lambda idx=idx,
                               at=action_type_var,
                               st=sub_type_var,
                               ex=extra_var: self.perform_action(idx, at, st, ex)
            )
            add_btn.grid(row=3, column=0, columnspan=2, pady=5)

            # store references
            self.player_frames.append({
                "frame": frame,
                "money_label": money_lbl,
                "poll_label": poll_lbl,
                "res_label": res_lbl,
                "fact_label": fact_lbl,
                "tech_label": tech_lbl,
                "worker_label": worker_lbl,
                "action_type_var": action_type_var,
                "sub_type_var": sub_type_var,
                "extra_var": extra_var,
                "history_box": history_box
            })

    def create_bottom_controls(self):
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        self.round_label = tk.Label(bottom_frame, text=f"Round: {self.current_round}")
        self.round_label.pack(side=tk.LEFT, padx=10)

        next_btn = tk.Button(bottom_frame, text="Next Round", command=self.next_round)
        next_btn.pack(side=tk.LEFT, padx=5)

        undo_btn = tk.Button(bottom_frame, text="Undo Last Action", command=self.undo_last_action)
        undo_btn.pack(side=tk.LEFT, padx=5)

        end_btn = tk.Button(bottom_frame, text="End Game", command=self.end_game)
        end_btn.pack(side=tk.LEFT, padx=5)

    ############################
    # ACTION MECHANICS
    ############################
    def perform_action(self, player_idx, action_type_var, sub_type_var, extra_var):
        """
        Called when user clicks 'Perform Action' in a player's frame.
        We parse the chosen action type, sub-type, and extra input (quantity or distance).
        Then we automatically calculate cost/pollution changes.
        """
        player = self.players[player_idx]
        old_state = self._snapshot_player(player)

        action_type = action_type_var.get()  # e.g. "Buy Terrain"
        sub_type = sub_type_var.get()        # e.g. "T5" or "Bois" or "AgroVerde"
        extra_text = extra_var.get().strip() # distance or quantity

        try:
            extra_val = int(extra_text)
        except ValueError:
            extra_val = 1

        action_log = f"{action_type} -> {sub_type} x {extra_val}"
        cost_delta = 0
        poll_delta = 0

        if action_type == "Buy Terrain":
            # sub_type is one of T1..T20, cost in TERRAINS
            if sub_type in TERRAINS:
                cost_delta = -TERRAINS[sub_type] * extra_val
            else:
                messagebox.showerror("Error", "Invalid terrain selected.")
                return

        elif action_type == "Buy Resource":
            # sub_type in RESOURCES
            if sub_type in RESOURCES:
                cost_per_unit = RESOURCES[sub_type]
                total_cost = cost_per_unit * extra_val * (-1)
                cost_delta = total_cost
                # Increase resource
                player.resources[sub_type] = player.resources[sub_type] + extra_val
            else:
                messagebox.showerror("Error", "Invalid resource selected.")
                return

        elif action_type == "Buy Factory":
            # sub_type in FACTORIES
            if sub_type in FACTORIES:
                fac_cost = FACTORIES[sub_type]["cost"] * extra_val
                cost_delta = -fac_cost
                # Add that many factories to player
                for _ in range(extra_val):
                    player.factories.append({"name": sub_type, "workers_assigned": 0})
            else:
                messagebox.showerror("Error", "Invalid factory selected.")
                return

        elif action_type == "Buy Technology":
            if sub_type in TECHNOLOGIES:
                tech_cost = TECHNOLOGIES[sub_type]["cost"] * extra_val
                cost_delta = -tech_cost
                # add the tech to player's list if not present multiple times
                for _ in range(extra_val):
                    player.technologies.append(sub_type)
            else:
                messagebox.showerror("Error", "Invalid technology selected.")
                return

        elif action_type == "Buy Worker":
            if sub_type in WORKERS:
                worker_cost = WORKERS[sub_type] * extra_val
                cost_delta = -worker_cost
                # increment worker count
                player.workers[sub_type] = max(player.workers[sub_type] + extra_val, 0)
            else:
                messagebox.showerror("Error", "Invalid worker type.")
                return

        elif action_type == "Add Transportation":
            # sub_type in TRANSPORTS
            if sub_type in TRANSPORTS:
                # extra_val is distance in tiles
                data = TRANSPORTS[sub_type]
                cost_per_tile = data["cost_per_tile"]
                poll_per_tile = data["pollution_per_tile"]
                cost_delta = -(cost_per_tile * extra_val)
                poll_delta = poll_per_tile * extra_val
            else:
                messagebox.showerror("Error", "Invalid transportation type.")
                return

        # Apply cost/pollution to player
        player.money += cost_delta
        player.pollution += poll_delta

        # build action record
        action_record = {
            "round": self.current_round,
            "action_text": action_log,
            "cost_delta": cost_delta,
            "poll_delta": poll_delta,
            "prev_state": old_state
        }
        player.action_history.append(action_record)
        self.undo_stack.append((player_idx, action_record))

        # record in history box
        self.player_frames[player_idx]["history_box"].insert(tk.END, f"R{self.current_round}: {action_log}")

        self.update_all_displays()

    def next_round(self):
        # each factory tries to consume resources; produce money, generate pollution
        for p in self.players:
            for f in p.factories:
                fname = f["name"]
                if fname not in FACTORIES:
                    continue
                specs = FACTORIES[fname]
                # check resource requirements
                can_produce = True
                for rtype, amt in specs["resource_requirements"].items():
                    if p.resources[rtype] < amt:
                        can_produce = False
                        break
                if can_produce:
                    # consume
                    for rtype, amt in specs["resource_requirements"].items():
                        p.resources[rtype] -= amt
                    # produce
                    p.money += specs["income_per_round"]
                    # pollution
                    p.pollution += specs["pollution_per_round"]
                    # apply any tech pollution mods
                    for tname in p.technologies:
                        if tname in TECHNOLOGIES:
                            p.pollution += TECHNOLOGIES[tname]["pollution_mod"]

        # carbon tax
        for p in self.players:
            if p.pollution < 0:
                p.pollution = 0
            tax = int(p.pollution * 5)
            p.money -= tax

        self.current_round += 1
        if self.current_round > self.max_rounds:
            self.end_game()
        else:
            self.update_all_displays()

    def end_game(self):
        results = []
        for p in self.players:
            ratio = p.money / (1 + p.pollution) if p.pollution >= 0 else p.money
            results.append((p.name, p.money, p.pollution, ratio))

        results.sort(key=lambda x: x[3], reverse=True)
        msg = "Final Results:\n\n"
        rank = 1
        for (name, money, pol, ratio) in results:
            msg += f"{rank}. {name} - Money: {money}, Pollution: {pol}, Ratio: {ratio:.2f}\n"
            rank += 1

        messagebox.showinfo("End of Game", msg)

    def undo_last_action(self):
        if not self.undo_stack:
            messagebox.showinfo("Undo", "No actions to undo.")
            return
        player_idx, action_record = self.undo_stack.pop()
        p = self.players[player_idx]
        # revert
        prev = action_record["prev_state"]
        p.money = prev["money"]
        p.pollution = prev["pollution"]
        p.resources = prev["resources"]
        p.factories = prev["factories"]
        p.technologies = prev["technologies"]
        p.workers = prev["workers"]
        if p.action_history and p.action_history[-1] == action_record:
            p.action_history.pop()

        # remove from listbox
        hb = self.player_frames[player_idx]["history_box"]
        if hb.size() > 0:
            hb.delete(tk.END)

        self.update_all_displays()

    ############################
    # STATE SNAPSHOTS
    ############################
    def _snapshot_player(self, p):
        return {
            "money": p.money,
            "pollution": p.pollution,
            "resources": dict(p.resources),
            "factories": [f.copy() for f in p.factories],
            "technologies": list(p.technologies),
            "workers": dict(p.workers)
        }

    ############################
    # UI UPDATES
    ############################
    def update_all_displays(self):
        for idx, pf in enumerate(self.player_frames):
            p = self.players[idx]
            pf["money_label"].config(text=f"Money (EC): {p.money}")
            pf["poll_label"].config(text=f"Pollution: {p.pollution}")
            pf["res_label"].config(text=self._fmt_resources(p.resources))
            pf["fact_label"].config(text=self._fmt_factories(p.factories))
            pf["tech_label"].config(text=self._fmt_techs(p.technologies))
            pf["worker_label"].config(text=self._fmt_workers(p.workers))
        self.round_label.config(text=f"Round: {self.current_round}")

    def _fmt_resources(self, d):
        lines = ["Resources:"]
        for k, v in d.items():
            lines.append(f"  {k}: {v}")
        return "\n".join(lines)

    def _fmt_factories(self, facts):
        if not facts:
            return "Factories:\n(None)"
        lines = ["Factories:"]
        for f in facts:
            lines.append(f"  - {f['name']} (workers: {f['workers_assigned']})")
        return "\n".join(lines)

    def _fmt_techs(self, tlist):
        if not tlist:
            return "Technologies:\n(None)"
        lines = ["Technologies:"]
        for t in tlist:
            lines.append(f"  - {t}")
        return "\n".join(lines)

    def _fmt_workers(self, wdict):
        lines = ["Workers:"]
        for wtype, count in wdict.items():
            lines.append(f"  {wtype}: {count}")
        return "\n".join(lines)

    ############################
    # SAVE / LOAD / RESET
    ############################
    def save_game(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON Files", "*.json")],
            title="Save Game Session"
        )
        if not file_path:
            return
        data = {
            "current_round": self.current_round,
            "players": [p.to_dict() for p in self.players],
            "undo_stack": self.undo_stack
        }
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            messagebox.showinfo("Save Successful", f"Game saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Save Error", f"Error saving file:\n{e}")

    def load_game(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".json",
            filetypes=[("JSON Files", "*.json")],
            title="Load Game Session"
        )
        if not file_path:
            return
        if not os.path.isfile(file_path):
            messagebox.showerror("Load Error", "File not found.")
            return
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.current_round = data.get("current_round", 1)
            p_dicts = data.get("players", [])
            self.undo_stack = data.get("undo_stack", [])
            for i, pd in enumerate(p_dicts):
                self.players[i].from_dict(pd)

            # clear listboxes
            for pf in self.player_frames:
                pf["history_box"].delete(0, tk.END)

            # rebuild action histories
            for i, p in enumerate(self.players):
                for act in p.action_history:
                    txt = f"R{act['round']}: {act['action_text']}"
                    self.player_frames[i]["history_box"].insert(tk.END, txt)

            self.update_all_displays()
            messagebox.showinfo("Load Successful", "Game session loaded.")
        except Exception as e:
            messagebox.showerror("Load Error", f"Error:\n{e}")

    def reset_game(self):
        confirm = messagebox.askyesno("Reset Game", "Are you sure you want to reset?")
        if confirm:
            self.current_round = 1
            self.undo_stack.clear()
            for idx, p in enumerate(self.players):
                n = p.name
                self.players[idx] = PlayerData(n)
                self.player_frames[idx]["history_box"].delete(0, tk.END)
            self.update_all_displays()

    def quit_app(self):
        self.destroy()


def main():
    app = EcoFactoryApp()
    app.mainloop()

if __name__ == "__main__":
    main()
