import pygame
from constants import *
from board import Board
from player import Player
from card import CardType

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Calculate layout dimensions
        self.board_area = pygame.Rect(20, 20, GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE)
        self.player_area = pygame.Rect(GRID_SIZE * CELL_SIZE + 40, 20, 300, 200)
        self.card_area = pygame.Rect(GRID_SIZE * CELL_SIZE + 40, 240, 300, 400)

    def draw_board(self, board):
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = pygame.Rect(
                    self.board_area.x + x * CELL_SIZE,
                    self.board_area.y + y * CELL_SIZE,
                    CELL_SIZE - 2,
                    CELL_SIZE - 2
                )
                pygame.draw.rect(self.screen, WHITE, rect, 1)
                
                # Draw resources
                if (x, y) in board.resources:
                    pygame.draw.circle(
                        self.screen,
                        GREEN,
                        (rect.centerx, rect.centery),
                        CELL_SIZE // 3
                    )

    def draw_player_info(self, player):
        pygame.draw.rect(self.screen, WHITE, self.player_area, 2)
        
        texts = [
            f"Player {player.id + 1}",
            f"Budget: ${player.budget}",
            f"Pollution: {player.pollution}",
            f"Score: {player.calculate_score():.2f}"
        ]
        
        for i, text in enumerate(texts):
            surface = self.font.render(text, True, WHITE)
            self.screen.blit(surface, (self.player_area.x + 10, self.player_area.y + 40 * i))

    def draw_cards(self, player):
        pygame.draw.rect(self.screen, WHITE, self.card_area, 2)
        title = self.font.render("Technologies", True, WHITE)
        self.screen.blit(title, (self.card_area.x + 10, self.card_area.y + 10))
        
        for i, tech in enumerate(player.technologies):
            card_rect = pygame.Rect(
                self.card_area.x + 10,
                self.card_area.y + 50 + i * (CARD_HEIGHT + 10),
                CARD_WIDTH,
                CARD_HEIGHT
            )
            pygame.draw.rect(self.screen, BLUE, card_rect)
            name = self.small_font.render(tech.name, True, WHITE)
            self.screen.blit(name, (card_rect.x + 5, card_rect.y + 5))

    def show_player_transition(self, next_player):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(128)
        self.screen.blit(overlay, (0, 0))
        
        text = self.font.render(f"Pass to Player {next_player + 1}", True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)

    def draw_game_over(self, winner):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(192)
        self.screen.blit(overlay, (0, 0))
        
        text = self.font.render(f"Winner: Player {winner.id + 1}", True, WHITE)
        score = self.font.render(f"Final Score: {winner.calculate_score():.2f}", True, WHITE)
        
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
        score_rect = score.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        
        self.screen.blit(text, text_rect)
        self.screen.blit(score, score_rect)

    def handle_click(self, pos, game):
        x = (pos[0] - self.board_area.x) // CELL_SIZE
        y = (pos[1] - self.board_area.y) // CELL_SIZE
        
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            if game.board.is_tile_available(x, y):
                cost = game.board.get_tile_cost(x, y)
                current_player = game.players[game.current_player]
                if current_player.buy_terrain(x, y, cost):
                    return True
        return False