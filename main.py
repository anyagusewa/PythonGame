import pygame
import random

# Запускаем все модули Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Камень, ножницы, бумага")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Шрифт
font = pygame.font.Font(None, 36)

# Загрузка изображений
rock_img = pygame.image.load("rock.png")
scissors_img = pygame.image.load("scissors.png")
paper_img = pygame.image.load("paper.png")

# Масштабирование изображений
rock_img = pygame.transform.scale(rock_img, (100, 100))
scissors_img = pygame.transform.scale(scissors_img, (100, 100))
paper_img = pygame.transform.scale(paper_img, (100, 100))

# Кнопки с изображениями
buttons = {
    "Камень": {"img": rock_img, "rect": pygame.Rect(50, 300, 100, 100)},
    "Ножницы": {"img": scissors_img, "rect": pygame.Rect(250, 300, 100, 100)},
    "Бумага": {"img": paper_img, "rect": pygame.Rect(450, 300, 100, 100)}
}

# Кнопка "Играть снова"
reset_button_rect = pygame.Rect(200, 420, 200, 50)

# Варианты выбора
choices = ["Камень", "Ножницы", "Бумага"]
images = {"Камень": rock_img, "Ножницы": scissors_img, "Бумага": paper_img}

# Переменные для хранения текущего состояния
player_choice = None
computer_choice = None
result = ""

# Переменные для счёта
player_score = 0
computer_score = 0

# Главный цикл игры
running = True
while running:
    screen.fill(WHITE)

    # Рисуем кнопки (изображения)
    for choice, data in buttons.items():
        screen.blit(data["img"], data["rect"].topleft)

    # Вывод текста
    player_text = font.render("Ваш выбор:", True, BLACK)
    computer_text = font.render("Компьютер выбрал:", True, BLACK)
    result_text = font.render(result, True, BLACK)

    screen.blit(player_text, (50, 65))
    screen.blit(computer_text, (350, 65))
    screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, 250))

    # Вывод счёта
    score_text = font.render(f"Счёт: Вы {player_score} - {computer_score} Компьютер", True, BLACK)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))  # В центре сверху

    # Отображение выбора
    if player_choice:
        screen.blit(images[player_choice], (50, 100))
    if computer_choice:
        screen.blit(images[computer_choice], (350, 100))

    # Рисуем кнопку "Играть снова"
    pygame.draw.rect(screen, GRAY, reset_button_rect)
    reset_text = font.render("Играть снова", True, BLACK)
    text_x = reset_button_rect.centerx - reset_text.get_width() // 2
    text_y = reset_button_rect.centery - reset_text.get_height() // 2
    screen.blit(reset_text, (text_x, text_y))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверяем выбор игрока
            for choice, data in buttons.items():
                if data["rect"].collidepoint(event.pos):    #проверяем кликнул ли игрок на кнопку
                    player_choice = choice
                    computer_choice = random.choice(choices)

                    # Определяем победителя
                    if player_choice == computer_choice:
                        result = "Ничья!"
                    elif (player_choice == "Камень" and computer_choice == "Ножницы") or \
                         (player_choice == "Ножницы" and computer_choice == "Бумага") or \
                         (player_choice == "Бумага" and computer_choice == "Камень"):
                        result = "Вы выиграли!"
                        player_score += 1  # Увеличиваем счёт игрока
                    else:
                        result = "Компьютер выиграл!"
                        computer_score += 1  # Увеличиваем счёт компьютера

            # Проверяем кнопку "Играть снова"
            if reset_button_rect.collidepoint(event.pos):
                player_choice = None
                computer_choice = None
                result = ""  # Обнуляем результат
                player_score = 0  # Обнуляем счёт игрока
                computer_score = 0  # Обнуляем счёт компьютера

    # Обновление экрана
    pygame.display.flip()

# Выход из Pygame
pygame.quit()
