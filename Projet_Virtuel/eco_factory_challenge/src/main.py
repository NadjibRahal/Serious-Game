import pygame
import sys
import json
import os
from constants import *
from game import Game
from ui import UI
from card_manager import CardManager

def load_game_data():
    # Get the path to the resources/data directory
    base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', 'data')
    
    # Load technologies.json instead of cards.json since that's what we have
    with open(os.path.join(base_path, 'technologies.json'), 'r') as f:
        technologies_data = json.load(f)
    with open(os.path.join(base_path, 'ressources.json'), 'r') as f:
        resources_data = json.load(f)
    return technologies_data, resources_data

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Eco-Factory Challenge")
    
    # Add clock initialization
    clock = pygame.time.Clock()
    
    card_manager = CardManager()
    resources_data = {"resources": card_manager.resources}
    game = Game(resources_data)
    ui = UI(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if ui.handle_click(event.pos, game):
                        game.next_turn()
                        ui.show_player_transition(game.current_player)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.next_turn()
                    ui.show_player_transition(game.current_player)

        # Clear screen
        screen.fill(BLACK)

        # Draw game elements
        ui.draw_board(game.board)
        ui.draw_player_info(game.players[game.current_player])
        ui.draw_cards(game.players[game.current_player])

        # Check game over condition
        if game.check_game_over():
            winner = game.get_winner()
            ui.draw_game_over(winner)
            pygame.display.flip()
            pygame.time.wait(5000)
            running = False

        # Update display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()