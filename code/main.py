from settings import *
from sys import exit
class Main:
    def __init__(self):

        # general
        pygame.init()
        self.display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Karl's Tetris")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # display
            self.display_surf.fill(GRAY)

            # updatig the game
            pygame.display.update()
            self.clock.tick()


if __name__ == "__main__":
    main = Main()
    main.run()