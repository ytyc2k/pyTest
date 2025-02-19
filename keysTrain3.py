import pygame
import random
import time

# 初始化pygame
pygame.init()

# 设置窗口大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置字体
font = pygame.font.Font(None, 50)
score_font = pygame.font.Font(None, 30)

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 文字列表
words = ["UP", "DOWN", "LEFT", "RIGHT"]
word_speed = 5  # 文字的滚动速度

# 游戏主循环
running = True
word_pos = random.randint(0, screen_width - 150)  # 随机生成文字的初始位置
current_word = random.choice(words)
current_direction = None

# 统计正确和错误的次数
correct_count = 0
wrong_count = 0

# 游戏循环
while running:
    screen.fill(BLACK)
    
    # 获取事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_direction = "UP"
            elif event.key == pygame.K_DOWN:
                current_direction = "DOWN"
            elif event.key == pygame.K_LEFT:
                current_direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                current_direction = "RIGHT"

    # 显示滚动文字
    text_surface = font.render(current_word, True, WHITE)
    screen.blit(text_surface, (word_pos, screen_height - 100))
    
    # 如果玩家按下了正确的方向键，消除文字
    if current_direction == current_word:
        correct_count += 1  # 增加正确计数
        word_pos = random.randint(0, screen_width - 150)
        current_word = random.choice(words)
        current_direction = None  # 重置方向
    elif current_direction is not None:
        wrong_count += 1  # 增加错误计数
        current_direction = None  # 重置方向

    # 文字下移
    word_pos += word_speed
    if word_pos > screen_height:
        word_pos = random.randint(0, screen_width - 150)
        current_word = random.choice(words)

    # 显示得分和错误统计
    correct_text = score_font.render(f"Correct: {correct_count}", True, WHITE)
    wrong_text = score_font.render(f"Wrong: {wrong_count}", True, RED)
    
    screen.blit(correct_text, (10, 10))
    screen.blit(wrong_text, (10, 40))

    # 更新屏幕
    pygame.display.flip()
    pygame.time.Clock().tick(30)  # 设置帧率

# 退出游戏
pygame.quit()
