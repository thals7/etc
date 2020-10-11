# multiple enemy 클래스 정의
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # 스프라이트 생성 위해 무조건 필요함
        self.image = pygame.image.load("C:/Users/dfjun/workspace/somin_study/etc/나도코딩/pygame_basic/enemy.png")
        self.size = self.image.get_rect().size
        self.width = self.size[0] # 적 가로
        self.height = self.size[1] # 적 세로
        self.x = random.randint(0, (screen_width - self.width)) # 적 생성시 x 위치
        self.y = 0 # 적 생성시 y 위치 (화면 가장 위)
        self.speed = random.uniform(0.1, 1.0) # 적 생성시 적의 스피드 (랜덤)

    def update(self):
        self.y = self.speed * clock.tick(30)
        if self.y >= screen_height: #적이 화면에서 사라졌을때 다시 적 하나를 생성함
            self.x = random.randint(0, (screen_width - self.width))
            self.y = 0
            self.speed = random.uniform(0.1, 1.0)
        self.rect = self.image.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y

e1 = Enemy()
e2 = Enemy()
e3 = Enemy()

enemies = []
enemies.append(e1)
enemies.append(e2)
enemies.append(e3)



    # 가로 경계값 처리

    if enemies.y >= screen_height:
        enemies.x = random.randint(0,(screen_width-enemies.width))
        enemies.y = 0

    # 4. 충돌 처리

    enemies.rect = enemies.image.get_rect()
    enemies.rect.left = enemies.x
    enemies.rect.top = enemies.y

    if character_rect.colliderect(enemies.rect):
        print("Game Over")
        running = False

    # 5. 화면에 그리기
    screen.blit(enemies, (enemies.x, enemies.y))
    pygame.display.update()
    pygame.display.update()