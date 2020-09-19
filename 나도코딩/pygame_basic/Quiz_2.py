# Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

import pygame
import random

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥 피하기 게임")

# FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경화면
background = pygame.image.load("C:/Users/dfjun/workspace/somin_study/etc/나도코딩/pygame_basic/background.png")
# 캐릭터 불러오기
character = pygame.image.load("C:/Users/dfjun/workspace/somin_study/etc/나도코딩/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x = (screen_width / 2) - (character_width / 2)
character_y = screen_height - character_height

character_speed = 0.6
# enemy 불러오기
enemy = pygame.image.load("C:/Users/dfjun/workspace/somin_study/etc/나도코딩/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x = random.randint(0,(screen_width-enemy_width))
enemy_y = 0

enemy_speed = 0.4

# 이동할 좌표
to_x = 0

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 게임 캐릭터 위치 정의
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x += to_x * dt
    enemy_y += enemy_speed * dt

    # 가로 경계값 처리
    if character_x < 0:
        character_x = 0
    elif character_x > screen_width - character_width:
        character_x = screen_width - character_width

    if enemy_y >= screen_height:
        enemy_x = random.randint(0,(screen_width-enemy_width))
        enemy_y = 0

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x
    character_rect.top = character_y

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x
    enemy_rect.top = enemy_y

    if character_rect.colliderect(enemy_rect):
        print("Game Over")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x, character_y))
    screen.blit(enemy, (enemy_x, enemy_y))
    pygame.display.update()

pygame.quit()