import pygame, math, random

pygame.init()

w = 1366
h = 768

dp = pygame.display.set_mode((w, h))

gr = (128, 128, 128)
wh = (255, 255, 255)
bl = (0, 0, 0)
rd = (240, 0, 0)
clrs = [gr, wh, rd]

clock = pygame.time.Clock()

circlex = random.randint(20, w - 20)
cirley  = random.randint(20, h - 20)
radius = random.randint(14, 20)
pygame.draw.circle(dp, random.choice(clrs), (circlex, cirley), radius)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            exit()
    
    mx = pygame.mouse.get_pos()[0]
    my = pygame.mouse.get_pos()[1]
    mc = pygame.mouse.get_pressed()

    sqcx = (mx - circlex)**2
    sqcy = (my - cirley)**2

    if math.sqrt(sqcx + sqcy) < radius and mc[0] == 1:
        dp.fill(bl)
        circlex = random.randint(20, w - 20)
        cirley  = random.randint(20, h - 20)
        radius = random.randint(14, 20)
        pygame.draw.circle(dp, random.choice(clrs), (circlex, cirley), radius)
    
    pygame.display.update()
    clock.tick()
