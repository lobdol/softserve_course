
import pygame
pygame.init()
gameDisplay=pygame.display.set_mode((400,300))
pygame.display.set_caption("My first game")
clock=pygame.time.Clock()
WHITE = (255, 255, 255)  
ORANGE = (255, 150, 100)

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
  # --- Main event loop
  for event in pygame.event.get(): # User did something
    if event.type == pygame.QUIT: # If user clicked close
        done = True # Flag that we are done so we exit this loop
  
  # --- Game logic should go here
  # --- Drawing code should go here
  # First, clear the screen to white. Don't put other drawing commands
  # above this, or they will be erased with this command.
  gameDisplay.fill(ORANGE)
  # --- Go ahead and update the screen with what we've drawn.
  pygame.display.update()
  # --- Limit to 60 frames per second
  clock.tick(60)
