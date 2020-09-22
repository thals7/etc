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

# multiple enemy 클래스 정의
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # 스프라이트 생성 위해 무조건 필요함
        self.image = pygame.image.load("C:/Users/dfjun/workspace/somin_study/etc/나도코딩/pygame_basic/enemy.png")
        self.rect = self.image.get_rect() # 이미지와 동일한 직사각형 생성
        self.size = self.rect.size # 적 사이즈
        self.width = self.size[0] # 적 가로
        self.height = self.size[1] # 적 세로
        self.x = random.randint(0, (screen_width - self.width)) # 적 생성시 x 위치
        self.y = 0 # 적 생성시 y 위치 (화면 가장 위)
        self.speed = random.uniform(0.1, 1.0) # 적 생성시 적의 스피드 (랜덤)
    def update(self):
        self.y = self.speed * clock.tick(30) # (loop 한번 돌 때 적의 스피드)
        if self.y >= screen_height: #적이 화면에서 사라졌을때 다시 적 하나를 생성함
            self.x = random.randint(0, (screen_width - self.width))
            self.y = 0
            self.speed = random.uniform(0.1, 1.0)

e1 = Enemy()
e2 = Enemy()
e3 = Enemy()

enemies = [e1, e2, e3]
enemies_group = pygame.sprite.RenderPlain(*enemies)

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

    # 가로 경계값 처리
    if character_x < 0:
        character_x = 0
    elif character_x > screen_width - character_width:
        character_x = screen_width - character_width

    # 적 재생성
    if enemies_group.y >= screen_height:
        enemies_group.x = random.randint(0, (screen_width - enemies_group.width))
        enemies_group.y = 0

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x
    character_rect.top = character_y

    enemies_group.rect = enemies_group.image.get_rect()
    enemies_group.rect.left = enemies_group.x
    enemies_group.rect.top = enemies_group.y


    if character_rect.colliderect(enemies_group.rect):
        print("Game Over")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x, character_y))
    screen.blit(e1, (enemies_group, enemies_group._x, enemies_group.y))
    pygame.display.update()

pygame.quit()