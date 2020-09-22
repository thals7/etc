# multiple enemy 클래스 정의
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # 스프라이트 생성 위해 무조건 필요함
        self.image = pygame.image.load("C:/Users/dfjun/workspace/somin_study/etc/나도코딩/pygame_basic/enemy.png")
        self.erect = self.image.get_rect() # 이미지와 동일한 직사각형 생성
        self.esize = self.rect.size # 적 사이즈
        self.width = self.size[0] # 적 가로
        self.height = self.size[1] # 적 세로
        self.x = random.randint(0, (screen_width - self.width)) # 적 생성시 x 위치
        self.y = 0 # 적 생성시 y 위치 (화면 가장 위)
        self.speed = random.uniform(0.1, 1.0) # 적 생성시 적의 스피드 (랜덤)
    def update(self):
        self.y = self.speed * clock.tick(30) (loop 한번 돌 때 적의 스피드)
        if self.y >= screen_height: #적이 화면에서 사라졌을때 다시 적 하나를 생성함
            self.x = random.randint(0, (screen_width - self.width))
            self.y = 0
            self.speed = random.uniform(0.1, 1.0)

e1 = Enemy()
e2 = Enemy()
e3 = Enemy()

enemies = [Enemy(e1), Enemy(e2), Enemy(e3)]

enemies_group = pygame.sprite.RenderPlain(*enemies)

    # 가로 경계값 처리

    if enemies_group.y >= screen_height:
        enemies_group.x = random.randint(0,(screen_width-enemies_group.width))
        enemies_group.y = 0

    # 4. 충돌 처리

    enemies_group.rect = enemies_group.image.get_rect()
    enemies_group.rect.left = enemies_group.x
    enemies_group.rect.top = enemies_group.y

    if character_rect.colliderect(e1.enemy_rect):
        print("Game Over")
        running = False

    # 5. 화면에 그리기
    screen.blit(e1, (enemies_group, enemies_group._x, enemies_group.y))
    pygame.display.update()
    pygame.display.update()