from pygame import *
# Параметры игры
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500

IMG_BACKGROUND = 'фон.png'
IMG_PLAYER = 'ракета.png'
IMG_BULLET = 'пуля.png'
IMG_ENEMY = 'враг.png'

score = 0
lost = 0
goal = 10

finish = False

# Классы для настройки персонажей
class GameSprite(sprite.Sprite):
    def __init__(self, img, width, height, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = GameSprite(IMG_PLAYER, 100, 100, 300, 400, 5)
# Работа с экраном
window = display.set_mode(( WINDOW_WIDTH, WINDOW_HEIGHT ))
display.set_caption('Шутер')

background =  transform.scale(image.load(IMG_BACKGROUND), (WINDOW_WIDTH, WINDOW_HEIGHT))
# Работа с текстом
font.init()
font1 = font.Font('Шрифт.ttf', 100)
font2 = font.Font('Шрифт.ttf', 50)

# Игровой цикл
clock = time.Clock()

while True:
    # Обработка событий
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()

    # Отображение обьектов
    window.blit(background, (0, 0))
    player.show()
    
    display.update()
    clock.tick(100)
