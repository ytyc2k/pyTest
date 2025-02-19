import pygame
import random
import time

# 初始化pygame
pygame.init()

# 设置窗口大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 使用支持音标的字体
font_path = "NotoSans-Regular-2.ttf"  # 假设字体文件在当前目录下
font = pygame.font.Font(font_path, 50)
score_font = pygame.font.Font(font_path, 30)
phonetic_font = pygame.font.Font(font_path, 30)

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 单词列表及其音标
words_with_phonetics = {
    "PYTHON": "/ˈpaɪθən/",
    "PROGRAM": "/ˈproʊɡræm/",
    "GITHUB": "/ˈɡɪthʌb/",
    "COMPUTER": "/kəmˈpjuːtər/",
    "KEYBOARD": "/ˈkiːbɔːrd/",
    "PYGAME": "/ˈpaɪɡeɪm/",
    "DEVELOPER": "/dɪˈvɛləpər/",
    "ALGORITHM": "/ˈælɡərɪðəm/"
}

word_speed = 2  # 降低文字的滚动速度

# 游戏主循环
running = True
word_pos = random.randint(0, screen_width - 150)  # 随机生成文字的初始位置
current_word = random.choice(list(words_with_phonetics.keys()))  # 随机选择单词
current_input = ""  # 玩家输入的内容
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
            if event.key == pygame.K_BACKSPACE:
                current_input = current_input[:-1]  # 删除最后一个字符
            elif event.key == pygame.K_RETURN:  # 按回车键检查拼写是否正确
                if current_input == current_word:
                    correct_count += 1  # 增加正确计数
                    word_pos = random.randint(0, screen_width - 150)
                    current_word = random.choice(list(words_with_phonetics.keys()))
                else:
                    wrong_count += 1  # 增加错误计数
                current_input = ""  # 重置输入框
            else:
                current_input += event.unicode  # 输入字符

    # 显示滚动单词
    text_surface = font.render(current_word, True, WHITE)
    screen.blit(text_surface, (word_pos, screen_height - 100))

    # 显示玩家输入的拼写
    input_surface = font.render(current_input, True, RED)
    screen.blit(input_surface, (word_pos, screen_height - 150))

    # 显示音标
    phonetic_surface = phonetic_font.render(words_with_phonetics[current_word], True, WHITE)
    screen.blit(phonetic_surface, (word_pos, screen_height - 200))

    # 文字下移
    word_pos += word_speed
    if word_pos > screen_height:
        word_pos = random.randint(0, screen_width - 150)
        current_word = random.choice(list(words_with_phonetics.keys()))

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
