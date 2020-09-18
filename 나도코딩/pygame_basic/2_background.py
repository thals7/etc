import pygame

pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My Game")

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\dfjun\\Workspace\\somin_study\\etc\\나도코딩\\pygame_basic\\background.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    pygame.display.update()  # 게임 화면을 계속해서 그려주는 작업

pygame.quit()