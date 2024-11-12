import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        mole_row = 0
        mole_col = 0
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = x // 32
                    col = y // 32
                    print(row, col)
                    if row == mole_row and col == mole_col:
                        mole_row = random.randrange(0, 20)
                        mole_col = random.randrange(0, 16)
                        print(mole_row, mole_col)

            screen.fill("light green")

            #Horizontal Lines
            for i in range(16):
                pygame.draw.line(screen, "black", (0, i * 32), (640, i * 32))
            #Vertical lines
            for i in range(20):
                pygame.draw.line(screen, "black", (i * 32, 0), (i * 32, 512))

            #Draw Mole
            screen.blit(mole_image, mole_image.get_rect(topleft = (mole_row * 32, mole_col * 32)))

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()