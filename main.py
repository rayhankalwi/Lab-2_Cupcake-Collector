import pygame
import asyncio  

pygame.init()
screen = pygame.display.set_mode((800, 600))

async def main(): 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill((0, 0, 0)) 
        pygame.display.flip()
        
        await asyncio.sleep(0) 

asyncio.run(main())