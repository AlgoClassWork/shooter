from random import randint
from pygame import *

# Параметры игры
WINDOW_WIDTH = 700  # Ширина окна
WINDOW_HEIGHT = 500  # Высота окна

# Пути к изображениям
IMG_BACKGROUND = 'фон.png'  # Фон игры
IMG_PLAYER = 'ракета.png'  # Игрок (ракета)
IMG_BULLET = 'пуля.png'  # Пуля
IMG_ENEMY = 'враг.png'  # Враг

# Игровые переменные
score = 0  # Счёт игрока
lost = 0  # Количество потерянных врагов
goal = 10  # Цель игры (уничтожить 10 врагов)

finish = False  # Флаг завершения игры

# Классы для настройки персонажей

class GameSprite(sprite.Sprite):
    """Класс для общего поведения спрайтов (игроков, врагов, пуль)"""
    
    def __init__(self, img, width, height, x, y, speed):
        """
        Инициализация спрайта.
        :param img: Путь к изображению
        :param width: Ширина спрайта
        :param height: Высота спрайта
        :param x: Начальная позиция по оси X
        :param y: Начальная позиция по оси Y
        :param speed: Скорость движения
        """
        super().__init__()  # Инициализация родительского класса
        self.image = transform.scale(image.load(img), (width, height))  # Загрузка и масштабирование изображения
        self.rect = self.image.get_rect()  # Получаем прямоугольник для позиционирования
        self.rect.x = x  # Устанавливаем начальную позицию по X
        self.rect.y = y  # Устанавливаем начальную позицию по Y
        self.speed = speed  # Устанавливаем скорость

    def show(self):
        """Отображение спрайта на экране"""
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    """Класс для игрока"""
    
    def update(self):
        """
        Обновление позиции игрока в зависимости от нажатых клавиш.
        Игрок двигается влево и вправо.
        """
        keys = key.get_pressed()  # Получаем состояние клавиш
        if keys[K_a] and self.rect.x > 0:  # Если нажата клавиша 'A' и не выходит за пределы
            self.rect.x -= self.speed  # Двигаем влево
        if keys[K_d] and self.rect.x < 600:  # Если нажата клавиша 'D' и не выходит за пределы
            self.rect.x += self.speed  # Двигаем вправо

    def fire(self):
        bullet = Bullet(IMG_BULLET, 20, 40, self.rect.centerx - 10, self.rect.y , 10)
        bullets.add(bullet)

class Enemy(GameSprite):

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > WINDOW_HEIGHT:
            self.rect.x = randint(0, WINDOW_WIDTH - 120)
            self.rect.y = 0

class Bullet(GameSprite):

    def update(self):
        self.rect.y -= self.speed

# Создание объекта игрока
player = Player(IMG_PLAYER, 100, 100, 300, 400, 5)

bullets = sprite.Group()
enemys = sprite.Group()

for i in range(1, 6):
    enemy = Enemy(IMG_ENEMY, 120, 80, randint(0, WINDOW_WIDTH - 120), 0, i)
    enemys.add(enemy)

# Настройка экрана игры
window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Устанавливаем размеры окна
display.set_caption('Шутер')  # Устанавливаем заголовок окна

# Загрузка фона
background = transform.scale(image.load(IMG_BACKGROUND), (WINDOW_WIDTH, WINDOW_HEIGHT))

# Работа с текстом
font.init()  # Инициализация шрифтов
font1 = font.Font('Шрифт.ttf', 100)  # Шрифт для большого текста
font2 = font.Font('Шрифт.ttf', 50)  # Шрифт для текста среднего размера

# Игровой цикл
clock = time.Clock()  # Настройка таймера для FPS

while True:
    # Обработка событий
    for some_event in event.get():
        if some_event.type == QUIT:  # Если событие закрытия окна
            exit()  # Закрытие программы
        elif some_event.type == KEYDOWN:
            if some_event.key == K_SPACE:
                player.fire()

    # Отображение объектов
    window.blit(background, (0, 0))  # Отображаем фон

    player.show()  # Отображаем игрока
    bullets.draw(window)
    enemys.draw(window)

    # Обновление позиции объектов
    player.update()  # Обновляем позицию игрока
    bullets.update()
    enemys.update()

    if sprite.groupcollide(bullets, enemys, True, True):
        enemy = Enemy(IMG_ENEMY, 120, 80, randint(0, WINDOW_WIDTH - 120), 0, randint(1,5))
        enemys.add(enemy)
        score += 1
        
    text_score = font2.render(f'Счет {score}',1,(255,255,255))
    window.blit(text_score, (10,10))

    # Обновление экрана
    display.update()  # Обновляем экран
    clock.tick(100)  # Ограничиваем FPS до 100
